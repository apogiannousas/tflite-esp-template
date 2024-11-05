#pragma once

#include "PredictionInterpreter.h"
#include <iostream>

class PredictionHandler {
 public:
  PredictionHandler() = default;
  ~PredictionHandler() = default;
  void Update(Prediction prediction);

 private:
};