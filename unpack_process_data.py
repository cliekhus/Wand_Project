# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:51:43 2020

@author: chelsea
"""

import numpy as np
import pickle

def unpack_pro_data(spell_names, num_train):
    
    ii = 0    
    
    for spell_name in spell_names:
        
        with open('processed_data/' + spell_name + '.pkl', 'rb') as handle:
            pro_data = pickle.load(handle)
            
            pro_data = np.array(pro_data)
            
            if ii == 0:
                
                #train_data = pro_data[0:num_train,:,:,:]
                train_data = pro_data[0:num_train]
                train_labels = [ii]*num_train
                
                #test_data = pro_data[num_train-1:-1,:,:,:]
                test_data = pro_data[num_train-1:-1]
                test_labels = [ii]*(len(pro_data)-num_train)
                
            else:
                
                train_data = np.append(train_data, pro_data[0:num_train], axis=0)
                #train_data = np.append(train_data, pro_data[0:num_train,:,:,:], axis=0)
                train_labels = train_labels + [ii]*num_train
                
                test_data = np.append(test_data, pro_data[num_train-1:-1], axis=0)
                #test_data = np.append(test_data, pro_data[num_train-1:-1,:,:,:], axis=0)
                test_labels = test_labels + [ii]*(len(pro_data)-num_train)
            
            ii = ii + 1
            
    train_labels = np.array(train_labels)
    test_labels = np.array(test_labels)

    return (train_data, train_labels, test_data, test_labels)