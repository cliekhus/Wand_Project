#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:46:04 2020

@author: chelsea
"""

import data_config
from os import path
import pickle

spell_name = "lumos"
#spell_name = "stupefy"
#spell_name = "wingardium_leviosa"

pro_data = []

ii = 0
possible_path = 'gesture_data/{}/{}_{}.csv'
while path.exists(possible_path.format(spell_name, spell_name, ii)):
    file = possible_path.format(spell_name, spell_name, ii)
    try:
        pro_data = pro_data + [data_config.data_config(file)]
    except:
        print('except: ' + file)
    ii += 1

with open('processed_data/' + spell_name + '.pkl', 'wb') as handle:
    pickle.dump(pro_data, handle)