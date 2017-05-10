#!/home/ubuntu/anaconda2/envs/tf1.1_py2.7/bin/python
import cgitb
import cgi

import os
import random
import rnn_rbm_generate
import subprocess


cgitb.enable()

# call to generate a new song
rnn_rbm_generate.main("parameter_checkpoints/pretrained.ckpt")

# Define an array with the path of favorite voices to use for conversion
# to wav files.  These voices were installed with timidity
voices=["Tone_000/101_Goblins--Unicorn.pat",
"Tone_000/004_Electric_Piano_1_Rhodes.pat",
"Tone_000/046_Harp.pat",
"Tone_000/016_Hammond_Organ.pat",
"Tone_000/053_Voice_Oohs.pat",
"Tone_000/088_New_Age.pat",
"Tone_000/094_Halo_Pad.pat"]

# Convert file from midi to .wav using external call to timidity
# and selecting a voice from the voices array
# -OwS2 indicates: Output wave, Stereo, 24 bit
# we use a random voice for the new song

voice = random.choice(voices)
cmd = "timidity music_outputs/newsong.mid -OwS2 -x'bank 0\n0 "+voice +"'"
#os.system(cmd)
subprocess.call(cmd, shell=False)

# Move the new song to the mp3files directory
cmd ="cp music_outputs/newsong.wav ../tensorweb/mp3files"
#os.system(cmd)
subprocess.call(cmd, shell=False)

# Play song to make sure all is ok. Comment out the next two lines in the server
# cmd2 = "play ../tensorweb/mp3files/newsong.wav"
# os.system(cmd2)


