#ifndef HcalSimAlgos_HcalShape_h
#define HcalSimAlgos_HcalShape_h
#include<vector>
  
#include "SimCalorimetry/CaloSimAlgos/interface/CaloVShape.h"
  
/**

   \class HcalShape

   \brief  shaper for Hcal (not for HF)
   
*/

class HcalShape : public CaloVShape
{
public:
  
  HcalShape();
  
  HcalShape(const HcalShape&d);

  virtual ~HcalShape(){}
  
  virtual double operator () (double time) const;
  virtual double       timeToRise()         const  ;
  void display () const {}

  void computeShape();

 private:
  
  int nbin_;
  std::vector<float> nt_;
  
};

#endif
  
  
