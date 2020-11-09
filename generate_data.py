#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:35:02 2020

@author: chelsea
"""

from kano_wand.kano_wand import Shop, Wand, PATTERN
import moosegesture as mg
import csv


spell_name = 'lumos'

spell_def = {("DL", "R", "DL"): "stupefy",
             ("DR", "R", "UR", "D"): "wingardium_leviosa",
             ("UL", "UR"): "reducio",
             ("DR", "U", "UR", "DR", "UR"): "flipendo",
             ("R", "D"): "expelliarmus",
             ("UR", "U", "D", "UL", "L", "DL"): "incendio",
             ("UR", "U", "DR"): "lumos",
             ("U", "D", "DR", "R", "L"): "locomotor",
             ("DR", "DL"): "engorgio",
             ("UR", "R", "DR"): "aguamenti",
             ("UR", "R", "DR", "UR", "R", "DR"): "avis",
             ("D", "R", "U"): "reducto"}

inv_spell_def = {v: k for k, v in spell_def.items()}

direction = {"D": "Down", "L": "Left", "R": "Right", "U": "Up",
             "DL": "Down-Left", "DR": "Down-Right",
             "UL": "Up-Left", "UR": "Up-Right"}

print()
print('Do your best to make the following spell: {}'.format(spell_name))
print('It has the shape: {}'.format([direction[x] for x in inv_spell_def[spell_name]]))
print('Wait for \'In [2]:\' to pop up,')
print('then hold the button down when you cast the spell.')


def make_name(spell_name):
    from os import path
    
    ii = 0
    possible_path = 'gesture_data/{}/{}_{}.csv'
    while path.exists(possible_path.format(spell_name, spell_name, ii)):
        ii += 1
        
        
    return possible_path.format(spell_name, spell_name, ii)





class GestureWand(Wand):
    def post_connect(self):
        self.gestures = spell_def
        self.spell = None
        self.pressed = False
        self.positions = []
        self.wrists = []
        self.subscribe_button()
        self.subscribe_position()

    def on_position(self, x, y, pitch, roll):
        if self.pressed:
            self.positions.append(tuple([x, -1 * y]))
            self.wrists.append(tuple([x, -1 * y, pitch, roll]))

    def on_button(self, pressed):
        self.pressed = pressed

        if pressed:
            self.spell = None
        else:
            gesture = mg.getGesture(self.positions)
            
            closest = mg.findClosestMatchingGesture(gesture, self.gestures, maxDifference=1)

            if closest != None:
                self.spell = self.gestures[closest[0]]
            
            self.vibrate(PATTERN.SHORT)
            #print("You made the following spell: {}: {}".format(self.spell, gesture))
            
            file_name = make_name(spell_name)
            
            with open(file_name,'w') as out:
                csv_out=csv.writer(out)
                for row in self.wrists:
                    csv_out.writerow(row)
            self.positions = []
            self.wrists = []

shop = Shop(wand_class=GestureWand)
wands = []

try:
    while len(wands) == 0:
        print("Scanning...")
        wands = shop.scan(connect=True)

except KeyboardInterrupt as e:
    for wand in wands:
        wand.disconnect()