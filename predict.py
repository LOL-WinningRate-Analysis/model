import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import os
import numpy as np

loaded_model = tf.keras.models.load_model('model.h5', custom_objects = {'KerasLayer':hub.KerasLayer})
print("loaded model and weights")
loaded_model.compile(loss = 'binary_crossentropy', optimizer = 'rmsprop', metrics = ['accuracy'])

#data preprocessing
data = [ 58, 523, 245, 141, 43, 25, 131, 106, 78, 51]
#y = 0
data = np.array(data)
data = np.reshape(data, (-1, 10))

print(data.shape)
print(data)


predict = loaded_model.predict(data)

print(predict)

