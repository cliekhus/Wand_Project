# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:33:32 2020

@author: chelsea
"""

import moosegesture as mg
import numpy as np
from unpack_process_data import unpack_pro_data
import matplotlib.pyplot as plt

spell_def = {("UR", "DR"): "lumos",
             ("DR", "DL"): "lumos",
             ("DL", "UL"): "lumos",
             ("UL", "UR"): "lumos",
             ("U", "D"): "lumos",
             ("D", "U"): "lumos",
             ("R", "L"): "lumos",
             ("L", "R"): "lumos",
             ("DL", "UR", "DL"): "stupefy",
             ("UL", "DR", "UL"): "stupefy",
             ("UR", "DL", "UR"): "stupefy",
             ("DR", "UL", "DR"): "stupefy",
             ("DR", "R", "UR", "D"): "wingardium_leviosa"}

spell_names = ["lumos", "stupefy", "wingardium_leviosa"]

num_train = 150

train_data, train_labels, test_data, test_labels = unpack_pro_data(spell_names, num_train)

train_pred = np.empty(np.shape(train_labels))

for ii, train_datum in enumerate(train_data):
    train_datum = train_datum[:,0:2]
#    plt.plot(*np.transpose(train_datum[:,0:2]))
    
#    train_datum = train_datum[train_datum[:,0] > 0,:]
    gesture = mg.getGesture(train_datum)
    closest = mg.findClosestMatchingGesture(gesture, spell_def, maxDifference=5)
    if closest != None:
        guess = spell_names.index(spell_def[closest[0]])
        train_pred[ii] = guess
    else:
        train_pred[ii] = 3
        
accuracy = np.mean((train_pred == train_labels).astype('int'))