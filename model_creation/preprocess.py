import argparse
from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import os

model_path = "mobilenet_v1_1.0_224_quant.tflite"
label_path = "labels_mobilenet_quant_v1_224.txt"

interpreter = Interpreter(model_path)
print("Model Loaded Successfully.")

interpreter.allocate_tensors()
_, height, width, _ = interpreter.get_input_details()[0]['shape']
print("Image Shape (", width, ",", height, ")")
FLAGS = None
parser = argparse.ArgumentParser()
parser.add_argument(
	'--input_dir',
	type=str,
	default='images',
	help='Absolute path to directory with images.'
)
parser.add_argument(
	'--ouput_dir',
	type=str,
	default='preprocessed_images',
	help='Absolute path to directory with images.'
)

FLAGS, unparsed = parser.parse_known_args()
# Load all images and transform them into the dimensions needed by the model
files = os.listdir(FLAGS.input_dir)
files = [f for f in files if os.path.isfile(FLAGS.input_dir + '/' + f)]
for file in files:
	image = Image.open(FLAGS.input_dir + '/' + file).convert('RGB').resize((width, height))
	image.save(FLAGS.ouput_dir + '/' + file)