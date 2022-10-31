#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:35:02 2020

@author: chelsea
"""
#2018
#sudo ./fix_bluetooth.sh
#sudo hciconfig hci0 down && sudo hciconfig hci0 up
from kano_wand.kano_wand import Shop, Wand, PATTERN
import moosegesture as mg
import csv
import time
import subprocess as sp
from playsound import playsound
import os

wand_address = 'F5:FA:A9:BF:E0:6B'

spell_name = 'lumos'

spell_def = {("DL", "R", "DL"): "stupefy",
             ("DR", "R", "UR", "D"): "wingardium_leviosa",
             ("UL", "UR"): "reducio",
             ("DR", "U", "UR", "DR", "UR"): "flipendo",
             ("R", "D"): "expelliarmus",
             ("UR", "U", "D", "UL", "L", "DL"): "incendio",
             ("UR", "U", "DR"): "lumos",
             ("U", "R"): "lumos",
             ("UR", "DR"): "lumos",
             ("U", "D"): "lumos",
             ("U", "UR", "DR"): "lumos",
             ("U", "UR", "DR"): "lumos",
             ("U", "D", "DR", "R", "L"): "locomotor",
             ("DR", "DL"): "engorgio",
             ("UR", "R", "DR"): "aguamenti",
             ("UR", "R", "DR", "UR", "R", "DR"): "avis",
             ("U", "UR", "R", "DR", "D", "U", "UR", "R", "DR"): "avis",
             ("D", "R", "U"): "reducto"}

inv_spell_def = {v: k for k, v in spell_def.items()}

direction = {"D": "Down", "L": "Left", "R": "Right", "U": "Up",
             "DL": "Down-Left", "DR": "Down-Right",
             "UL": "Up-Left", "UR": "Up-Right"}

print()
print('Starting geocache')


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
            print(x, y)
            self.positions.append(tuple([x, -1*y]))
            self.wrists.append(tuple([x, -1 * y, pitch, roll]))

    def on_button(self, pressed):
        self.pressed = pressed

        if pressed:
            self.spell = None
        else:
            self.vibrate(PATTERN.SHORT)
            
            gesture = mg.getGesture(self.positions)
            print(self.positions)
            
            closest = mg.findClosestMatchingGesture(gesture, self.gestures, maxDifference=2)
            print('test')
            if closest != None:
                print('in')
                self.spell = self.gestures[closest[0]]
                #print('/audio/{}.mp3'.format(self.spell))
                playsound('audio/{}.mp3'.format(self.spell))
            else:
                playsound('audio/nospell.mp3')
            
            print("You made the following spell: {}: {}".format(self.spell, gesture))

            self.positions = []
            self.wrists = []

def run_forever():
    shop = Shop(wand_class=GestureWand)
    wands = []

    try:
        while True:
            while len(wands) == 0:
                print("Scanning...")
                wands = shop.scan(connect=True)
        
            wand = wands[0]
        
            while wand.connected:
                print('still connected')
                stdoutdata = sp.getoutput("hcitool con")
                wand_on = wand_address in stdoutdata
                if not(wand_on):
                    wand.disconnect()
                time.sleep(1)
        
            print('wand disconnected')
            wands = []

    except KeyboardInterrupt as e:
        for wand in wands:
            wand.disconnect()
            
    except:
    	if 'wands' in locals():
            for wand in wands:
                wand.disconnect()
                
    	command = 'sudo ./fix_bluetooth.sh'
    	os.popen("sudo -S %s"%(command), 'w').write('sheba738')
    	time.sleep(5)
    	run_forever()
    	
    	
run_forever()
        
        
        
        
        
        
