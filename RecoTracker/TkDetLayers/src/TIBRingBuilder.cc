#include "RecoTracker/TkDetLayers/interface/TIBRingBuilder.h"

using namespace edm;
using namespace std;

TIBRing* TIBRingBuilder::build(const vector<const GeometricDet*>& detsInRing,
			       const TrackerGeometry* theGeomDetGeometry){
  vector<const GeomDet*> theGeomDets;
  for(vector<const GeometricDet*>::const_iterator it=detsInRing.begin();
      it!=detsInRing.end();it++){

    const GeomDet* theGeomDet = theGeomDetGeometry->idToDet( (*it)->geographicalID() );
    theGeomDets.push_back(theGeomDet);    
  }
  
  return new TIBRing(theGeomDets);  
}
