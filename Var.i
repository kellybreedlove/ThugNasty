%module Var
%{
#include "Var.h"
%}

%include "std_string.i"

%nodefaultctor Var;  // Disable the default constructor for class Var

namespace Camellia {
  enum Space { HGRAD, HCURL, HDIV, HGRAD_DISC, HCURL_DISC, HDIV_DISC, HDIV_FREE, L2, CONSTANT_SCALAR, VECTOR_HGRAD, VECTOR_HGRAD_DISC, VECTOR_L2, UNKNOWN_FS };
}

class Var {
public:
  //Var();
  int ID();
  // const string & name()
  string displayString();
  //  IntrepidExtendedTypes::EOperatorExtended op();
  int rank();
  Space space();
  VarType varType();
  //Camellia::EOperator op();
  LinearTermPtr termTraced();
  VarPrt grad();
  VarPtr div();
  VarPtr curl(int spaceDim);
  VarPtr dx();
  VarPtr dy();
  VarPtr x();
  VarPtr y();
};

class VarPtr {
public:
  Var* operator->();

  LinearTermPtr __mul__(double w) {
    return *self * w;
  }

  LinearTermPtr __rmul__(double w) {
    return *self * w:
  }

  LinearTermPtr __mul__(vector<double> w) {
    return *self * w;
  }

  LinearTermPtr __rmul__(vector<double> w) {
    return *self * w;
  }

  LinearTermPtr __add__(VarPtr v) {
    return *self + v;
  }

  LinearTermPtr __div__(double w) {
    return *self / w;
  }

  LinearTermPtr __div__(Function Ptr f) {
    return *self / f;
  }

  LinearTermPtr __sub__(VarPtr v) {
    return *self - v;
  }

  LinearTermPtr __sub__() {
    return - *self;
  }
};
