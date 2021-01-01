# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:17:12 2020

@author: chelsea
"""

import tensorflow as tf
from unpack_process_data import unpack_pro_data
import numpy as np

print(tf.__version__)

spell_names = ["lumos", "stupefy", "wingardium_leviosa"]

num_train = 150

train_data, train_labels, test_data, test_labels = unpack_pro_data(spell_names, num_train)


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (2,2), activation='relu', input_shape=np.shape(test_data[0])),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(3)
])

model.summary()
    
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


model.fit(train_data, train_labels, epochs=10)


test_loss, test_acc = model.evaluate(test_data,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)


probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_data)

    