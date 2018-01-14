import subprocess
import time
from os import listdir

# This file is used to implement the logic in sound.py only
# on any other machine than a raspberry pi

# Directory where all the sounds we play can be found
SOUNDS_DIR = "/Users/tparsons/dev/git/rasp-sound-machine/sounds"

# Name of the app used to play the sound
SOUND_APP = "sox-macosx/play"

'''
INITIAL SETUP
'''

# Get an array of all the sound files
files = listdir(SOUNDS_DIR)    

# Get the total number of files
totalFiles = len(files)

# Keeps track of what file in the list we're playing
curFilePos = 0

# Keeps track of the PID for the currently playing sound
curPID = 0

'''
TODO: When a button is pressed, do the following:
Play a sound for 20 minutes
If a sound is already playing, play another sound
If at end of sound list, stop playing
'''

'''
LOOP, WAITING FOR BUTTON PRESS
'''
while True:
    # Emulate our button on the Raspberry pi
    text = input("Press a button")

    print("Button Pressed")
    
    # File this is the last file, kill the sound, reset our count and restart the loop
    if curFilePos == totalFiles:
        curPID.kill()
        curFilePos = 0
        continue

    # Kill the old sound if it's playing
    if curPID != 0:
        curPID.kill()
    
    # Spawn a child process to play button
    curPID = subprocess.Popen([SOUND_APP, "-q", SOUNDS_DIR + "/" + files[curFilePos]])

    # Print out PID
    print("PID: %d" % curPID.pid)

    # Increment the current file position
    curFilePos += 1

    # sleep for 500ms to ensure button isn't clicked too quickly
    time.sleep(.5)