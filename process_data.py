#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:46:04 2020

@author: chelsea
"""

import data_config
from os import path
import pickle

config_choice = 'mg' #3d, 2d, mg

spell_name = "lumos"
#spell_name = "stupefy"
#spell_name = "wingardium_leviosa"

pro_data = []

ii = 0
possible_path = 'gesture_data/{}/{}_{}.csv'
while path.exists(possible_path.format(spell_name, spell_name, ii)):
    file = possible_path.format(spell_name, spell_name, ii)
    try:
        if config_choice == '3d':
            pro_data = pro_data + [data_config.matrix_config(file, 10)]
        elif config_choice == '2d':
            max_length = 100
            pro_data = pro_data + [data_config.pad_config(file, max_length)]
        elif config_choice == 'mg':
            pro_data = pro_data + [data_config.mg_config(file)]
    except:
        print('except: ' + file)
    ii += 1

with open('processed_data/' + spell_name + '.pkl', 'wb') as handle:
    pickle.dump(pro_data, handle)