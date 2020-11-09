#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:35:31 2020

@author: chelsea
"""

def data_config(file):
    
    import numpy as np
    
    raw_data = np.genfromtxt(file, delimiter=',')
    raw_data = (raw_data-np.min(raw_data,0))
    
    pro_data = np.zeros((550,550,3))
    
    pixels = raw_data[:,0:2].astype('int')
    tilt = raw_data[:,2]
    rot = raw_data[:,3]
    rate = np.empty(len(pixels))
    
    for ii in range(len(pixels)):
        
        if ii == 0:
            rate[ii] = 0
        else:
            rate[ii] = np.sqrt((pixels[ii,0]-pixels[ii-1,0])**2 + (pixels[ii,1]-pixels[ii-1,1])**2)
    
    tilt = tilt/np.max(tilt)
    rot = rot/np.max(rot)
    rate = rate-np.min(rate)
    rate = rate/np.max(rate)
    
    for ii in range(len(pixels)):
        
        pro_data[pixels[ii,0], pixels[ii,1], 0] = tilt[ii]
        pro_data[pixels[ii,0], pixels[ii,1], 1] = rot[ii]
        pro_data[pixels[ii,0], pixels[ii,1], 2] = rate[ii]

    return pro_data