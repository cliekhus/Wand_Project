#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 13:35:31 2020

@author: chelsea
"""

def matrix_config(file, scale):
    
    import numpy as np
    
    raw_data = np.genfromtxt(file, delimiter=',')
    raw_data = (raw_data-np.min(raw_data,0))
    
    pro_data = np.zeros((int(1000/scale),int(1000/scale),3))
    
    pixels = raw_data[:,0:2]
    pixels = (pixels/scale).astype('int')
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





def pad_config(file, max_length):
    
    import numpy as np
    
    raw_data = np.genfromtxt(file, delimiter=',')
    raw_data = (raw_data-np.min(raw_data,0))
    
    pad_length = max_length-np.shape(raw_data)[0]
    
    #pro_data = np.pad(raw_data, ((math.floor(pad_length/2),math.ceil(pad_length/2)),(0,0)), 'constant', constant_values = 0)

    pro_data = np.pad(raw_data/2000, ((0,pad_length),(0,0)), 'constant', constant_values = 0)

    #pro_data = np.append(raw_data/2000,  np.tile(raw_data[-1]/2000, (pad_length,1)), axis=0)
    return pro_data



def mg_config(file):
    
    import numpy as np
    import math
    
    raw_data = np.genfromtxt(file, delimiter=',')
    raw_data = (raw_data-np.min(raw_data,0))
    x = raw_data[:,0]
    y = raw_data[:,1]
    
    newy = math.cos(math.pi/4) * x - math.sin(math.pi/4) * y
    newx = math.sin(math.pi/4) * x + math.cos(math.pi/4) * y
    
    raw_data[:,0] = newx
    raw_data[:,1] = newy
    
    pro_data = raw_data
    
    return pro_data