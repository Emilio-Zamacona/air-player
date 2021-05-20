import mido
import keyboard
import time
import rtmidi
from rtmidi.midiutil import open_midiinput
import cv2 as cv
import numpy as np





count =45
mul = 1
other_count = 0
key_change = 0
print(mido.get_output_names())

with mido.open_output(mido.get_output_names()[1]) as inport:
    while not keyboard.is_pressed("q"):
        msg = mido.Message('note_on', note=count+key_change)
        msg2 = mido.Message('note_on', note=count+key_change+7)
        msg3 = mido.Message('note_on', note=count+key_change+12)
        time.sleep(0.15)
        if keyboard.is_pressed("m"):
            print("msg sent "+str(count+key_change))
            inport.send(msg)
            inport.send(msg2)
            inport.send(msg3)
            count+=19*mul
            if count <40 or count >94:
                mul = mul*-1
            other_count +=1
            if other_count >=16:
                other_count=0
                if key_change == 2:
                    key_change = 0
                else:
                    key_change = 2
