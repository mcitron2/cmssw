#ifndef DataMixingSiPixelWorker_h
#define SimDataMixingSiPixelWorker_h

/** \class DataMixingSiPixelWorker
 *
 * DataMixingModule is the EDProducer subclass 
 * that overlays rawdata events on top of MC,
 * using real data for pileup simulation
 * This class takes care of the Si Pixel information
 *
 * \author Mike Hildreth, University of Notre Dame
 *
 * \version   1st Version October 2007
 *
 ************************************************************/

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventPrincipal.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Selector.h"

#include "DataFormats/Provenance/interface/ProductID.h"
#include "DataFormats/Common/interface/Handle.h"
//Data Formats
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSet.h"
#include "DataFormats/SiPixelDigi/interface/PixelDigi.h"

#include <map>
#include <vector>
#include <string>


namespace edm
{
  class DataMixingSiPixelWorker
    {
    public:

      DataMixingSiPixelWorker();

     /** standard constructor*/
      explicit DataMixingSiPixelWorker(const edm::ParameterSet& ps);

      /**Default destructor*/
      virtual ~DataMixingSiPixelWorker();

      void putSiPixel(edm::Event &e) ;
      void addSiPixelSignals(const edm::Event &e); 
      void addSiPixelPileups(const int bcr, edm::EventPrincipal*,unsigned int EventId);


    private:
      // data specifiers

      edm::InputTag pixeldigi_collectionSig_ ; // secondary name given to collection of SiPixel digis
      edm::InputTag pixeldigi_collectionPile_ ; // secondary name given to collection of SiPixel digis
      std::string PixelDigiCollectionDM_  ; // secondary name to be given to new SiPixel digis

      // 

      typedef std::multimap<int, PixelDigi> OneDetectorMap;   // maps by pixel ID for later combination - can have duplicate pixels
      typedef std::map<uint32_t, OneDetectorMap> SiGlobalIndex; // map to all data for each detector ID

      SiGlobalIndex SiHitStorage_;


      //      unsigned int eventId_; //=0 for signal, from 1-n for pileup events

      Selector * sel_;
      std::string label_;

    };
}//edm

#endif
