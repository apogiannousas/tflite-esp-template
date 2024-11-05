#pragma once

#include "tensorflow/lite/c/common.h"

enum Prediction {
	UNKNOWN = 0,
	GOLDFISH = 2,
	BISON = 348,
};

class PredictionInterpreter {
 public:
  PredictionInterpreter() = default;
  ~PredictionInterpreter() = default;
  virtual Prediction GetResult(TfLiteTensor* model_output);
};