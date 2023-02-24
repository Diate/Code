import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras import models
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images = training_images.reshape(training_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
save_model = models.load_model("acc9786.h5")
plt.imshow(test_images[11])
plt.show()
resule = save_model.predict(test_images[11:12])
final = np.argmax(resule)
print(test_images[11:12])
print(resule)
print(final)
print(save_model.layers[0].get_bias()[0])