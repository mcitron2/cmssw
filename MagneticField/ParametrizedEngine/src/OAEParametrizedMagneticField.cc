/** \file
 *
 *  \author N. Amapane - CERN
 */

#include <MagneticField/ParametrizedEngine/src/OAEParametrizedMagneticField.h>
#include <FWCore/ParameterSet/interface/ParameterSet.h>
#include <FWCore/MessageLogger/interface/MessageLogger.h>

#include "TkBfield.h"

using namespace std;
using namespace magfieldparam;

OAEParametrizedMagneticField::OAEParametrizedMagneticField(string T) : 
  theParam(T){}


OAEParametrizedMagneticField::OAEParametrizedMagneticField(const edm::ParameterSet& parameters) : 
  theParam(parameters.getParameter<string>("BValue")) {}


OAEParametrizedMagneticField::~OAEParametrizedMagneticField() {}


GlobalVector
OAEParametrizedMagneticField::inTesla(const GlobalPoint& gp) const {
  if (isDefined(gp)) {
    return inTeslaUnchecked(gp);
  } else {
    edm::LogWarning("MagneticField|FieldOutsideValidity") << " Point " << gp << " is outside the validity region of OAEParametrizedMagneticField";
    return GlobalVector();
  }
}

namespace {
  double ooh = 1./100;
}

GlobalVector
OAEParametrizedMagneticField::inTeslaUnchecked(const GlobalPoint& gp) const {
  double x[3] = {gp.x()*ooh, gp.y()*ooh, gp.z()*ooh};
  double B[3];
  theParam.getBxyz(x,B);
  return GlobalVector(B[0], B[1], B[2]);
}


bool
OAEParametrizedMagneticField::isDefined(const GlobalPoint& gp) const {
  return (gp.perp2()<(115.*115.) && fabs(gp.z())<280.);
}
