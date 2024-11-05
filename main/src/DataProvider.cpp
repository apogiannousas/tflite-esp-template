#include "DataProvider.h"

#define IMAGE_COUNT 4
static uint8_t *image_database[IMAGE_COUNT];

constexpr int kNumCols = 224;
constexpr int kNumRows = 224;
constexpr int kMaxImageSize = kNumCols * kNumRows;

extern const uint8_t bison1_jpg_start[]		asm("_binary_bison1_jpg_start");
extern const uint8_t bison2_jpg_start[]		asm("_binary_bison2_jpg_start");
extern const uint8_t goldfish1_jpg_start[]	asm("_binary_goldfish1_jpg_start");
extern const uint8_t goldfish2_jpg_start[]	asm("_binary_goldfish2_jpg_start");

int DataProvider::Read(TfLiteTensor* modelInput) {
	static int data_index = 0;

	// There are no other data for inference
	if (data_index >= IMAGE_COUNT) {
		return 1;
	}

	std::copy(image_database[data_index], image_database[data_index] + kMaxImageSize, modelInput->data.uint8);
	data_index++;

	return 0;
}

bool DataProvider::Init()
{
	image_database[0] = (uint8_t *) bison1_jpg_start;
	image_database[1] = (uint8_t *) bison1_jpg_start;
	image_database[2] = (uint8_t *) bison1_jpg_start;
	image_database[3] = (uint8_t *) bison1_jpg_start;
	
	return true;
}