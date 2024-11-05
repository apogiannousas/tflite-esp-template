#pragma once

#include <vector>
#include <optional>
#include <cstdint>
#include "tensorflow/lite/c/common.h"

class DataProvider {
	public:
	DataProvider() = default;
	~DataProvider() = default;
	bool Init();
	int Read(TfLiteTensor* modelInput);

	private:
};
