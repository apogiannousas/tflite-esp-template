#include "PredictionHandler.h"

void PredictionHandler::Update(Prediction prediction) {
	switch (prediction) {
		case Prediction::GOLDFISH:
			std::cout << "Detected goldfish\n";
			break;
		case Prediction::BISON:
			std::cout << "Detected bison\n";
			break;
		default:
			std::cout << "Detected uknown object\n";
			break;
	}
}