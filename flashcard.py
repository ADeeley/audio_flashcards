# import simple audio, random, pickle, time
import os
import simpleaudio as sa
import random

#-----Audio Flashcards v0.1 - Alpha-----
#
#   **CURRENT ISSUES TO BE RESOLVED:**
#       1. Engine or choose_pair producing the same random file n times.
#       2. Not yet playing files


audFileOne = "F:\mystuff\soundbytes\\eng\\"
audFileTwo = "F:\mystuff\soundbytes\\rus\\"

def gen_soundbyte_dict(eng, rus):
    ''' Generates a dictionary of Russian to English soundbyte key+value pairings. 
        - eng: file path as a string
        - rus: file path as a string
    Notes:
    -Must be an even number of soundbyte pairings
        '''
   
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
    
    # creates a random number to select a pairing from SBD keys
    randomiser = random.randint(0, len(SBDkeys)-1)
    return (SBDkeys[randomiser], SBD[SBDkeys[randomiser]])
    
def engine():
    ''' Function to manage the home screen. Gives options of new round, run again, quit'''
    
    sound_dict = gen_soundbyte_dict(audFileOne, audFileTwo)
    
    iter = int(input("How many do you want?"))
    assert(type(iter) == int), "iter must be an int"
    
    while iter >0:
        x = choose_pair(sound_dict)
        play_audio(audFileTwo + x[0])
        play_audio(audFileOne + x[1])
        iter -= 1

    
    #play_audio(a)

def play_audio(file):
    '''plays the audio files given.
        - file: a tuple containing two file name pairings as a string'''
        
    wave_obj = sa.WaveObject.from_wave_file(file)
    play_obj = wave_obj.play()
    play_obj.wait_done()

engine()



#manage_soundbites(audioFiles)


# variables 

# creates a dictionary pairing of English and Russian phrases



# function to read and play audio files randomly. Always plays key+value from dict

