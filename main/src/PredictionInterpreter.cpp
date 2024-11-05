#include "PredictionInterpreter.h"

Prediction PredictionInterpreter::GetResult(TfLiteTensor* model_output) {
	int8_t goldfish_score = model_output->data.uint8[Prediction::GOLDFISH];
	int8_t bison_score = model_output->data.uint8[Prediction::BISON];

	float goldfish_score_f =
		(goldfish_score - model_output->params.zero_point) * model_output->params.scale;
	float bison_score_f =
		(bison_score - model_output->params.zero_point) * model_output->params.scale;
	
	if (goldfish_score_f >= bison_score_f) {
		return Prediction::GOLDFISH;
	}
	else{
		return Prediction::BISON;
	}
}