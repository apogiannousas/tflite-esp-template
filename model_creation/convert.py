import tensorflow as tf
import numpy as np
import pandas as pd
import os
from pathlib import Path
import re

# convert from tflite to C array
tf_lite_path = Path("mobilenet_v1_1.0_224_quant.tflite")
os.system(f"xxd -i {tf_lite_path} > micro_model.cpp")
SRC_MODEL_PATH = Path("micro_model.cpp")
DEST_MODEL_PATH = Path("../main/src/micro_model.cpp")

# copy raw C array to embedded environment and add header
def read_len() -> int:
	"""read C-array length from file"""
	with open(SRC_MODEL_PATH) as f:
		for line in f:
			if line.startswith("unsigned int"):
				length = re.search("([0-9])+;", line)
				# take first match, remove semicolon, coerce
				length = int(length[0][:-1])
				return int(length)

def read_array() -> str:
	"""read C-array from file"""
	array = ""
	with open(SRC_MODEL_PATH) as f:
		for i, line in enumerate(f, 1):
			if i == 1: continue # start
			if line.startswith("};"): break # end
			array += line
	return array

def get_cfile_header(array_length) -> str:
	return (f"""
// We need to keep the data array aligned on some architectures.
#include "micro_model.h"

// memory management
#ifdef __has_attribute
#define HAVE_ATTRIBUTE(x) __has_attribute(x)
#else
#define HAVE_ATTRIBUTE(x) 0
#endif
#if HAVE_ATTRIBUTE(aligned) || (defined(__GNUC__) && !defined(__clang__))
#define DATA_ALIGN_ATTRIBUTE __attribute__((aligned(4)))
#else
#define DATA_ALIGN_ATTRIBUTE
#endif

const unsigned int micro_model_len = {array_length};
const unsigned char micro_model[] DATA_ALIGN_ATTRIBUTE = """ + "{\n"
)

def get_cfile_footer() -> str:
	return "};"

def compose_c_file() -> str:
	array_length = read_len()
	array = read_array()
	header = get_cfile_header(array_length)
	footer = get_cfile_footer()
	doc = header + array + footer
	return doc

def copy_to_mcu() -> None:
	doc = compose_c_file()
	with open(DEST_MODEL_PATH, "w") as f:
		f.write(doc)

copy_to_mcu()