/*----------------------------------------------------------------------
----------------------------------------------------------------------*/
#include "FWCore/Framework/interface/InputSource.h"

#include "DataFormats/Provenance/interface/ProcessHistory.h"
#include "DataFormats/Provenance/interface/ProcessHistoryRegistry.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventPrincipal.h"
#include "FWCore/Framework/interface/FileBlock.h"
#include "FWCore/Framework/interface/InputSourceDescription.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "FWCore/Framework/interface/LuminosityBlockPrincipal.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/RunPrincipal.h"
#include "FWCore/Framework/src/PrincipalCache.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/ActivityRegistry.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"
#include "FWCore/Utilities/interface/do_nothing_deleter.h"
#include "FWCore/Utilities/interface/GlobalIdentifier.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "FWCore/Utilities/interface/TimeOfDay.h"

#include <cassert>
#include <fstream>
#include <iomanip>

namespace edm {

  namespace {
        std::string const& suffix(int count) {
          static std::string const st("st");
          static std::string const nd("nd");
          static std::string const rd("rd");
          static std::string const th("th");
          // *0, *4 - *9 use "th".
          int lastDigit = count % 10;
          if(lastDigit >= 4 || lastDigit == 0) return th;
          // *11, *12, or *13 use "th".
          if(count % 100 - lastDigit == 10) return th;
          return (lastDigit == 1 ? st : (lastDigit == 2 ? nd : rd));
        }
        template <typename T>
        boost::shared_ptr<T> createSharedPtrToStatic(T* ptr) {
          return boost::shared_ptr<T>(ptr, do_nothing_deleter());
        }

        ProcessHistoryID
        deleteFromProcessHistory(ProcessHistoryID const& phid, std::string const& processName) {
        // Delete the current process from the process history.  This must be done to maintain consistency
        // for runs or lumis when the principal cache is flushed, because the process history modified flag,
        // stored in the principal, is lost when the cache is flushed.
          if(!phid.isValid()) {
            return phid;
          }
          ProcessHistory ph;
          bool found = ProcessHistoryRegistry::instance()->getMapped(phid, ph);
          assert(found);
          ProcessHistory newPH;
          newPH.reserve(ph.size());
          for(ProcessHistory::const_iterator it = ph.begin(), itEnd = ph.end(); it != itEnd; ++it) {
            if(processName != it->processName()) {
              newPH.push_back(*it);
            }
          }
          ProcessHistoryRegistry::instance()->insertMapped(newPH);
          return newPH.id();
        }
  }

  InputSource::InputSource(ParameterSet const& pset, InputSourceDescription const& desc) :
      ProductRegistryHelper(),
      actReg_(desc.actReg_),
      principalCache_(desc.principalCache_),
      maxEvents_(desc.maxEvents_),
      remainingEvents_(maxEvents_),
      maxLumis_(desc.maxLumis_),
      remainingLumis_(maxLumis_),
      readCount_(0),
      processingMode_(RunsLumisAndEvents),
      moduleDescription_(desc.moduleDescription_),
      productRegistry_(createSharedPtrToStatic<ProductRegistry const>(desc.productRegistry_)),
      primary_(pset.getParameter<std::string>("@module_label") == std::string("@main_input")),
      processGUID_(primary_ ? createGlobalIdentifier() : std::string()),
      time_(),
      doneReadAhead_(false),
      state_(IsInvalid),
      runAuxiliary_(),
      lumiAuxiliary_(),
      runPrematurelyRead_(false),
      lumiPrematurelyRead_(false),
      statusFileName_() {

    if(pset.getUntrackedParameter<bool>("writeStatusFile", false)) {
      std::ostringstream statusfilename;
      statusfilename << "source_" << getpid();
      statusFileName_ = statusfilename.str();
    }

    // Secondary input sources currently do not have a product registry.
    if(primary_) {
      assert(desc.productRegistry_ != 0);
    }
    std::string const defaultMode("RunsLumisAndEvents");
    std::string const runMode("Runs");
    std::string const runLumiMode("RunsAndLumis");

    // The default value provided as the second argument to the getUntrackedParameter function call
    // is not used when the ParameterSet has been validated and the parameters are not optional
    // in the description.  As soon as all primary input sources and all modules with a secondary
    // input sources have defined descriptions, the defaults in the getUntrackedParameterSet function
    // calls can and should be deleted from the code.
    std::string processingMode = pset.getUntrackedParameter<std::string>("processingMode", defaultMode);
    if(processingMode == runMode) {
      processingMode_ = Runs;
    } else if(processingMode == runLumiMode) {
      processingMode_ = RunsAndLumis;
    } else if(processingMode != defaultMode) {
      throw Exception(errors::Configuration)
        << "InputSource::InputSource()\n"
        << "The 'processingMode' parameter for sources has an illegal value '" << processingMode << "'\n"
        << "Legal values are '" << defaultMode << "', '" << runLumiMode << "', or '" << runMode << "'.\n";
    }
  }

  InputSource::~InputSource() {}

  void
  InputSource::fillDescriptions(ConfigurationDescriptions& descriptions) {
    ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
  }

  static std::string const kBaseType("Source");

  std::string const&
  InputSource::baseType() {
    return kBaseType;
  }

  void
  InputSource::fillDescription(ParameterSetDescription& desc) {
    std::string defaultString("RunsLumisAndEvents");
    desc.addUntracked<std::string>("processingMode", defaultString)->setComment(
    "'RunsLumisAndEvents': process runs, lumis, and events.\n"
    "'RunsAndLumis':       process runs and lumis (not events).\n"
    "'Runs':               process runs (not lumis or events).");
    desc.addUntracked<bool>("writeStatusFile", false)->setComment("Write a status file. Intended for use by workflow management.");
  }

  EventPrincipal* const
  InputSource::eventPrincipalCache() {
    return &principalCache().eventPrincipal();
  }

  // This next function is to guarantee that "runs only" mode does not return events or lumis,
  // and that "runs and lumis only" mode does not return events.
  // For input sources that are not random access (e.g. you need to read through the events
  // to get to the lumis and runs), this is all that is involved to implement these modes.
  // For input sources where events or lumis can be skipped, getNextItemType() should
  // implement the skipping internally, so that the performance gain is realized.
  // If this is done for a source, the 'if' blocks in this function will never be entered
  // for that source.
  InputSource::ItemType
  InputSource::nextItemType_() {
    ItemType itemType = getNextItemType();
    if(itemType == IsEvent && processingMode() != RunsLumisAndEvents) {
      readEvent_();
      return nextItemType_();
    }
    if(itemType == IsLumi && processingMode() == Runs) {
      // QQQ skipLuminosityBlock_();
      return nextItemType_();
    }
    return itemType;
  }

  InputSource::ItemType
  InputSource::nextItemType() {
    if(doneReadAhead_) {
      return state_;
    }
    doneReadAhead_ = true;
    ItemType oldState = state_;
    if(eventLimitReached()) {
      // If the maximum event limit has been reached, stop.
      state_ = IsStop;
    } else if(lumiLimitReached()) {
      // If the maximum lumi limit has been reached, stop
      // when reaching a new file, run, or lumi.
      if(oldState == IsInvalid || oldState == IsFile || oldState == IsRun || processingMode() != RunsLumisAndEvents) {
        state_ = IsStop;
      } else {
        ItemType newState = nextItemType_();
        if(newState == IsEvent) {
          assert (processingMode() == RunsLumisAndEvents);
          state_ = IsEvent;
        } else {
          state_ = IsStop;
        }
      }
    } else {
      ItemType newState = nextItemType_();
      if(newState == IsStop) {
        state_ = IsStop;
      } else if(newState == IsFile || oldState == IsInvalid) {
        state_ = IsFile;
      } else if(newState == IsRun || oldState == IsFile) {
        runAuxiliary_ = readRunAuxiliary();
        state_ = IsRun;
      } else if(newState == IsLumi || oldState == IsRun) {
        assert (processingMode() != Runs);
        lumiAuxiliary_ = readLuminosityBlockAuxiliary();
        state_ = IsLumi;
      } else {
        assert (processingMode() == RunsLumisAndEvents);
        state_ = IsEvent;
      }
    }
    if(state_ == IsStop) {
      lumiAuxiliary_.reset();
      runAuxiliary_.reset();
    }
    return state_;
  }

  void
  InputSource::doBeginJob() {
    this->beginJob();
  }

  void
  InputSource::doEndJob() {
    endJob();
  }

  void
  InputSource::registerProducts() {
    if(!typeLabelList().empty()) {
      addToRegistry(typeLabelList().begin(), typeLabelList().end(), moduleDescription(), productRegistryUpdate());
    }
  }

  // Return a dummy file block.
  boost::shared_ptr<FileBlock>
  InputSource::readFile() {
    assert(doneReadAhead_);
    assert(state_ == IsFile);
    assert(!limitReached());
    doneReadAhead_ = false;
    boost::shared_ptr<FileBlock> fb = readFile_();
    return fb;
  }

  void
  InputSource::closeFile(boost::shared_ptr<FileBlock> fb) {
    fb->close();
    closeFile_();
    return;
  }

  // Return a dummy file block.
  // This function must be overridden for any input source that reads a file
  // containing Products.
  boost::shared_ptr<FileBlock>
  InputSource::readFile_() {
    return boost::shared_ptr<FileBlock>(new FileBlock);
  }

  boost::shared_ptr<RunPrincipal> const
  InputSource::runPrincipal() const {
    return principalCache_->runPrincipalPtr();
  }

  boost::shared_ptr<LuminosityBlockPrincipal> const
  InputSource::luminosityBlockPrincipal() const {
    return principalCache_->lumiPrincipalPtr();
  }

  void
  InputSource::readAndCacheRun() {
    if(runPrematurelyRead_) {
      runPrematurelyRead_ = false;
      return;
    }
    RunSourceSentry(*this);
    bool merged = principalCache_->merge(runAuxiliary(), productRegistry_);
    if(!merged) {
      boost::shared_ptr<RunPrincipal> rp(new RunPrincipal(runAuxiliary(), productRegistry_, processConfiguration()));
      principalCache_->insert(rp);
    }
    readRun_(principalCache_->runPrincipalPtr());
  }

  int
  InputSource::markRun() {
    assert(doneReadAhead_);
    assert(state_ == IsRun);
    assert(!limitReached());
    doneReadAhead_ = false;
    return principalCache_->runPrincipal().run();
  }

  void
  InputSource::readAndCacheLumi() {
    if(lumiPrematurelyRead_) {
      lumiPrematurelyRead_ = false;
      return;
    }
    LumiSourceSentry(*this);
    bool merged = principalCache_->merge(luminosityBlockAuxiliary(), productRegistry_);
    if(!merged) {
      boost::shared_ptr<LuminosityBlockPrincipal> lb(
        new LuminosityBlockPrincipal(luminosityBlockAuxiliary(),
                                     productRegistry_,
                                     processConfiguration(),
                                     principalCache_->runPrincipalPtr()));
      principalCache_->insert(lb);
    }
    readLuminosityBlock_(principalCache_->lumiPrincipalPtr());
  }

  int
  InputSource::markLumi() {
    assert(doneReadAhead_);
    assert(state_ == IsLumi);
    assert(!limitReached());
    doneReadAhead_ = false;
    --remainingLumis_;
    assert(principalCache_->lumiPrincipal().luminosityBlock() == luminosityBlockAuxiliary()->luminosityBlock());
    return principalCache_->lumiPrincipal().luminosityBlock();
  }

  boost::shared_ptr<RunPrincipal>
  InputSource::readRun_(boost::shared_ptr<RunPrincipal> rpCache) {
    // Note: For the moment, we do not support saving and restoring the state of the
    // random number generator if random numbers are generated during processing of runs
    // (e.g. beginRun(), endRun())
    rpCache->fillRunPrincipal();
    return rpCache;
  }

  boost::shared_ptr<LuminosityBlockPrincipal>
  InputSource::readLuminosityBlock_(boost::shared_ptr<LuminosityBlockPrincipal> lbCache) {
    lbCache->fillLuminosityBlockPrincipal();
    return lbCache;
  }

  EventPrincipal*
  InputSource::readEvent(boost::shared_ptr<LuminosityBlockPrincipal> lbCache) {
    assert(doneReadAhead_);
    assert(state_ == IsEvent);
    assert(!eventLimitReached());
    doneReadAhead_ = false;

    EventPrincipal* result = readEvent_();
    if(result != 0) {
      assert(lbCache->run() == result->run());
      assert(lbCache->luminosityBlock() == result->luminosityBlock());
      Event event(*result, moduleDescription());
      postRead(event);
      if(remainingEvents_ > 0) --remainingEvents_;
      ++readCount_;
      setTimestamp(result->time());
      issueReports(result->id());
    }
    return result;
  }

  EventPrincipal*
  InputSource::readEvent(EventID const& eventID) {
    EventPrincipal* result = 0;

    if(!limitReached()) {
      result = readIt(eventID);
      if(result != 0) {
        Event event(*result, moduleDescription());
        postRead(event);
        if(remainingEvents_ > 0) --remainingEvents_;
        ++readCount_;
        issueReports(result->id());
      }
    }
    return result;
  }

  void
  InputSource::skipEvents(int offset) {
    doneReadAhead_ = false;
    this->skip(offset);
  }

  bool
  InputSource::goToEvent(EventID const& eventID) {
    doneReadAhead_ = false;
    return this->goToEvent_(eventID);
  }

  void
  InputSource::issueReports(EventID const& eventID) {
    if(isInfoEnabled()) {
      LogVerbatim("FwkReport") << "Begin processing the " << readCount_
                               << suffix(readCount_) << " record. Run " << eventID.run()
                               << ", Event " << eventID.event()
                               << ", LumiSection " << eventID.luminosityBlock()
                               << " at " << std::setprecision(3) << TimeOfDay();
    }
    if(!statusFileName_.empty()) {
      std::ofstream statusFile(statusFileName_.c_str());
      statusFile << eventID << " time: " << std::setprecision(3) << TimeOfDay() << '\n';
      statusFile.close();
    }

    // At some point we may want to initiate checkpointing here
  }

  EventPrincipal*
  InputSource::readIt(EventID const&) {
    throw Exception(errors::LogicError)
      << "InputSource::readIt()\n"
      << "Random access is not implemented for this type of Input Source\n"
      << "Contact a Framework Developer\n";
  }

  void
  InputSource::setRun(RunNumber_t) {
    throw Exception(errors::LogicError)
      << "InputSource::setRun()\n"
      << "Run number cannot be modified for this type of Input Source\n"
      << "Contact a Framework Developer\n";
  }

  void
  InputSource::setLumi(LuminosityBlockNumber_t) {
    throw Exception(errors::LogicError)
      << "InputSource::setLumi()\n"
      << "Luminosity Block ID cannot be modified for this type of Input Source\n"
      << "Contact a Framework Developer\n";
  }

  void
  InputSource::skip(int) {
    throw Exception(errors::LogicError)
      << "InputSource::skip()\n"
      << "Random access is not implemented for this type of Input Source\n"
      << "Contact a Framework Developer\n";
  }

  bool
  InputSource::goToEvent_(EventID const& eventID) {
    throw Exception(errors::LogicError)
      << "InputSource::goToEvent_()\n"
      << "Random access is not implemented for this type of Input Source\n"
      << "Contact a Framework Developer\n";
    return true;
  }


  void
  InputSource::rewind_() {
    throw Exception(errors::LogicError)
      << "InputSource::rewind()\n"
      << "Rewind is not implemented for this type of Input Source\n"
      << "Contact a Framework Developer\n";
  }

  void
  InputSource::decreaseRemainingEventsBy(int iSkipped) {
    if(-1 == remainingEvents_) {
      return;
    }
    if(iSkipped < remainingEvents_) {
      remainingEvents_ -= iSkipped;
    } else {
      remainingEvents_ = 0;
    }
  }

  void
  InputSource::postRead(Event& event) {
    Service<RandomNumberGenerator> rng;
    if(rng.isAvailable()) {
      rng->postEventRead(event);
    }
  }

  void
  InputSource::doBeginRun(RunPrincipal& rp) {
    Run run(rp, moduleDescription());
    beginRun(run);
    run.commit_();
  }

  void
  InputSource::doEndRun(RunPrincipal& rp) {
    rp.setEndTime(time_);
    Run run(rp, moduleDescription());
    endRun(run);
    run.commit_();
    runPrematurelyRead_ = false;
  }

  void
  InputSource::doBeginLumi(LuminosityBlockPrincipal& lbp) {
    LuminosityBlock lb(lbp, moduleDescription());
    beginLuminosityBlock(lb);
    lb.commit_();
  }

  void
  InputSource::doEndLumi(LuminosityBlockPrincipal& lbp) {
    lbp.setEndTime(time_);
    LuminosityBlock lb(lbp, moduleDescription());
    endLuminosityBlock(lb);
    lb.commit_();
    lumiPrematurelyRead_ = false;
  }

  void
  InputSource::doPreForkReleaseResources() {
    preForkReleaseResources();
  }

  void
  InputSource::doPostForkReacquireResources(boost::shared_ptr<multicore::MessageReceiverForSource> iReceiver) {
    postForkReacquireResources(iReceiver);
  }

  void
  InputSource::wakeUp_() {}

  void
  InputSource::beginLuminosityBlock(LuminosityBlock&) {}

  void
  InputSource::endLuminosityBlock(LuminosityBlock&) {}

  void
  InputSource::beginRun(Run&) {}

  void
  InputSource::endRun(Run&) {}

  void
  InputSource::beginJob() {}

  void
  InputSource::endJob() {}

  void
  InputSource::preForkReleaseResources() {}

  void
  InputSource::postForkReacquireResources(boost::shared_ptr<multicore::MessageReceiverForSource>) {}

  bool
  InputSource::randomAccess_() const {
    return false;
  }

  ProcessingController::ForwardState
  InputSource::forwardState_() const {
    return ProcessingController::kUnknownForward;
  }

  ProcessingController::ReverseState
  InputSource::reverseState_() const {
    return ProcessingController::kUnknownReverse;
  }

  ProcessHistoryID const&
  InputSource::processHistoryID() const {
    assert(runAuxiliary());
    return runAuxiliary()->processHistoryID();
  }

  RunNumber_t
  InputSource::run() const {
    assert(runAuxiliary());
    return runAuxiliary()->run();
  }

  LuminosityBlockNumber_t
  InputSource::luminosityBlock() const {
    assert(luminosityBlockAuxiliary());
    return luminosityBlockAuxiliary()->luminosityBlock();
  }

  InputSource::SourceSentry::SourceSentry(Sig& pre, Sig& post) : post_(post) {
    pre();
  }

  InputSource::SourceSentry::~SourceSentry() {
    post_();
  }

  InputSource::EventSourceSentry::EventSourceSentry(InputSource const& source) :
     sentry_(source.actReg()->preSourceSignal_, source.actReg()->postSourceSignal_) {
  }

  InputSource::LumiSourceSentry::LumiSourceSentry(InputSource const& source) :
     sentry_(source.actReg()->preSourceLumiSignal_, source.actReg()->postSourceLumiSignal_) {
  }

  InputSource::RunSourceSentry::RunSourceSentry(InputSource const& source) :
     sentry_(source.actReg()->preSourceRunSignal_, source.actReg()->postSourceRunSignal_) {
  }

  InputSource::FileOpenSentry::FileOpenSentry(InputSource const& source) :
     sentry_(source.actReg()->preOpenFileSignal_, source.actReg()->postOpenFileSignal_) {
  }

  InputSource::FileCloseSentry::FileCloseSentry(InputSource const& source) :
     sentry_(source.actReg()->preCloseFileSignal_, source.actReg()->postCloseFileSignal_) {
  }
}
