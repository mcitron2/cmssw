#ifndef gen_ExternalDecays_PhotosInterface_h
#define gen_ExternalDecays_PhotosInterface_h

// #include "HepPDT/ParticleDataTable.hh"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "HepMC/SimpleVector.h"

namespace HepMC 
{
class GenEvent;
class GenVertex;
}

namespace gen {

   class PhotosInterface
   {
      public:
      
      // ctor & dtor
      PhotosInterface(); 
      PhotosInterface( const edm::ParameterSet& );
      ~PhotosInterface() {}

      void init();
      const std::vector<std::string>& specialSettings() { return fSpecialSettings; }
      HepMC::GenEvent* apply( HepMC::GenEvent* );
      // --> void configureOnlyFor( int );
      void avoidTauLeptonicDecays() { fAvoidTauLeptonicDecays=true; return; }
      
      private: 
            
      struct Scaling {
         HepMC::ThreeVector weights;
	 int                flag;
	 Scaling( HepMC::ThreeVector vec, int flg ) 
	    : weights(HepMC::ThreeVector(1.,1.,1)), flag(1) { weights=vec; flag=flg; }
      };

      int                      fOnlyPDG;
      std::vector<std::string> fSpecialSettings; 
      bool                     fAvoidTauLeptonicDecays;  
      std::vector<Scaling>     fScaleFactors;
      std::vector<int>         fBarcodes;
      bool                     fIsInitialized;
      
      void attachParticles( HepMC::GenEvent*, HepMC::GenVertex*, int );
             
   };

}

#endif
