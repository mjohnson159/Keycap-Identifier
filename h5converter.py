# convert .h5 to tflite
from tensorflow.contrib import lite
converter = lite.TFLiteConverter.from_keras_model_file('keycapidentifier.h5')
tfmodel = converter.convert()
open("model.tflite", "wb").write(tfmodel)
