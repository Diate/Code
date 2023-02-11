import tensorflow as tf
from tensorflow import keras
import numpy as np

from sklearn.utils import shuffle
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

from keras.models import Model
from keras.models import Sequential
from keras.layers import BatchNormalization
from keras.layers import AveragePooling2D
from keras.layers import MaxPool2D
from keras.layers import Conv2D
from keras.layers import Activation
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Input
from keras.layers import Dense
from keras.layers import concatenate
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
tf.config.list_physical_devices('GPU')
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images = training_images.reshape(training_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

training_images,training_labels = shuffle(training_images,training_labels)

training_images = training_images.astype("float")/255.0
test_images = test_images.astype("float")/255.0



lb = LabelBinarizer()
train_labels = lb.fit_transform(training_labels)


training_images, Valid_img , train_labels , Valid_lab = train_test_split(training_images,train_labels, train_size=0.85, test_size=0.15, random_state=0)
#print(Valid_img[0])
models = Sequential()

width = 28
height = 28
classes = 10
shape = (width, height, 1)
models.add(Conv2D(28, (3,3), padding="same", input_shape= shape))
models.add(Activation("relu"))
models.add(BatchNormalization())
models.add(Conv2D(28, (3,3), padding="same"))
models.add(Activation("relu"))
models.add(BatchNormalization())
models.add(MaxPool2D(pool_size=(2,2)))
models.add(Conv2D(56, (3,3), padding="same"))
models.add(Activation("relu"))
models.add(BatchNormalization())
models.add(Conv2D(56, (3,3), padding="same"))
models.add(Activation("relu"))
models.add(BatchNormalization())
models.add(MaxPool2D(pool_size=(2,2)))
models.add(Flatten())
models.add(Dense(392))
models.add(Activation("relu"))
models.add(BatchNormalization())
models.add(Dense(classes))
models.add(Activation("softmax"))

#print(models.summary())

aug = ImageDataGenerator(rotation_range=0.18, zoom_range=0.15, width_shift_range=0.2, height_shift_range=0.2, horizontal_flip=True)
learning_rate = 0.006
epose = 10
batch_size = 64
opt = SGD(learning_rate=learning_rate, momentum=0.85)
models.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])
print("Start traning")
'''print(training_images.shape[0])
print(train_labels[0])
plt.imshow(training_images[0])
plt.show()'''
H = models.fit_generator(aug.flow(training_images,train_labels, batch_size=batch_size), validation_data=(Valid_img,Valid_lab), steps_per_epoch=training_images.shape[0]//batch_size, epochs=epose, verbose=1)
models.save("acc9786.h5")



