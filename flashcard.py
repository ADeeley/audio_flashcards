# import simple audio, random, pickle, time
import os
import simpleaudio as sa
import random

def gen_soundbyte_dict(eng, rus):
    ''' Generates a dictionary of Russian to English soundbyte pairings. 
    - Must be an even number of soundbyte pairings'''
   
    SBD = {}
    SBDkeys = []
    iter = 0
    
    engDir = os.listdir(eng)
    rusDir = os.listdir(rus)
    assert(len(engDir) == len(rusDir)), "Lists must be of equal length."
    
    for s in range(len(rusDir)):
        SBD[rusDir[s]] = engDir[s]
        
    for key in SBD:
        SBDkeys.append(key)
        
    return (SBD, SBDkeys)

def choose_pair(soundbyte_tuples):
    ''' Chooses a random pairing of soundbytes and returns a tuple'''
    SBD = soundbyte_tuples[0]
    SBDkeys = soundbyte_tuples[1]
    
    randomiser = random.randint(0, len(SBDkeys))
    return (SBDkeys[1], SBD[SBDkeys[1]])
    
def engine():
    ''' Function to manage the home screen. Gives options of new round, run again, quit'''
    
    iter = input("How many do you want?")
    assert(iter == int), "iter must be an int"
    
    while iter >0:
        print(choose_pair(gen_soundbyte_dict("F:\mystuff\soundbytes\\eng", "F:\mystuff\soundbytes\\rus")))
        iter -= 1
    
    
    #play_audio(a)

def play_audio(file):
    wave_obj = sa.WaveObject.from_wave_file(file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

engine()



#manage_soundbites(audioFiles)


# variables 

# creates a dictionary pairing of English and Russian phrases



# function to read and play audio files randomly. Always plays key+value from dict

