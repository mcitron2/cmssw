#include "CalibFormats/HcalObjects/interface/HcalCalibrationWidths.h"

/** \class HcalCalibrationWidths
    
    Container for retrieving uncertainties of calibration constants for HCAL
   $Author: ratnikov
   $Date: 2005/08/02 01:31:24 $
   $Revision: 1.1 $
*/

HcalCalibrationWidths::HcalCalibrationWidths (const float fGain [4], const float fPedestal [4]) {
  int iCap = 4;
  while (--iCap >= 0) {
    mGain [iCap] = fGain [iCap];
    mPedestal [iCap] = fPedestal [iCap];
  }
}
