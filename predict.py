import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import os
import numpy as np

loaded_model = tf.keras.models.load_model('model.h5', custom_objects = {'KerasLayer':hub.KerasLayer})
print("loaded model and weights")
loaded_model.compile(loss = 'binary_crossentropy', optimizer = 'rmsprop', metrics = ['accuracy'])

#data preprocessing
data = [ 43, 64, 81, 127, 876, 3, 222, 33, 26, 164]
# 32, 81, 57, 432, 61, 516, 60, 245, 67, 350, 0
# 111, 8, 64, 81, 245, 202, 350, 154, 131, 113, 1
# 39, 145, 254, 98, 517, 78, 61, 80, 51, 64, 0
# 43, 64, 81, 127, 876, 3, 222, 33, 26, 164, 1
data = np.array(data)
data = data/1000
data = np.reshape(data, (-1, 10))

print(data.shape)
print(data)


predict = loaded_model.predict(data)

print(predict)

