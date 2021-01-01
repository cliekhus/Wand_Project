# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:50:54 2020

@author: chelsea
"""

import numpy as np
from unpack_process_data import unpack_pro_data
from sklearn import svm

spell_names = ["lumos", "stupefy", "wingardium_leviosa"]

num_train = 150

train_data, train_labels, test_data, test_labels = unpack_pro_data(spell_names, num_train)

train_data = np.reshape(train_data, (np.shape(train_data)[0], np.shape(train_data)[1]*np.shape(train_data)[2]))
test_data = np.reshape(test_data, (np.shape(test_data)[0], np.shape(test_data)[1]*np.shape(test_data)[2]))

clf = svm.SVC(decision_function_shape = 'ovo')
clf.fit(train_data, train_labels)

predictions = clf.predict(test_data)

accuracy = np.mean((predictions == test_labels).astype('int'))

print('Test accuracy: {}'.format(accuracy))