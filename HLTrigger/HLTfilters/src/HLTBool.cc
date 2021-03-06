/** \class HLTBool
 *
 * See header file for documentation
 *
 *  $Date: 2007/08/28 01:17:49 $
 *  $Revision: 1.2 $
 *
 *  \author Martin Grunewald
 *
 */


#include "HLTrigger/HLTfilters/interface/HLTBool.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

//
// constructors and destructor
//
HLTBool::HLTBool(const edm::ParameterSet& iConfig) :
  result_(iConfig.getParameter<bool> ("result"))
{
  LogDebug("HLTBool") << " configured result is: " << result_;
}

HLTBool::~HLTBool()
{
}

//
// member functions
//

// ------------ method called to produce the data  ------------
bool
HLTBool::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   return result_;
}
