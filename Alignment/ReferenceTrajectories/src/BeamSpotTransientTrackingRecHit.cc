/** \file BeamSpotTransientTrackingRecHit.cc
 *
 * Author     : Andreas Mussgiller
 * date       : 2010/08/30
 * last update: $Date: 2010/03/08 16:13:38 $
 * by         : $Author: mussgill $
 */

#include "BeamSpotTransientTrackingRecHit.h"

AlgebraicVector BeamSpotTransientTrackingRecHit::parameters() const
{
  AlgebraicVector result(1);
  result[0] = localPosition().x();
  return result;
}

AlgebraicSymMatrix BeamSpotTransientTrackingRecHit::parametersError() const
{
  LocalError le = localPositionError();
  AlgebraicSymMatrix m(1);
  m[0][0] = le.xx();
  return m;
}

void BeamSpotTransientTrackingRecHit::initialize() const
{
  theProjectionMatrix = AlgebraicMatrix( 1, 5, 0);
  theProjectionMatrix[0][3] = 1;
  
  isInitialized = true;
}

bool BeamSpotTransientTrackingRecHit::isInitialized(false);
AlgebraicMatrix BeamSpotTransientTrackingRecHit::theProjectionMatrix;
