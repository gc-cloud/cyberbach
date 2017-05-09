
import os
import sys

# Append paths to python files so we can import them
#sys.path.append('../')

# import python script to generate new music
import rnn_rbm_generate

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
cmd = "timidity newsong.mid -OwS2 -x'bank 0\n0 "+voices[6]+"'"
os.system(cmd)

# Play song to make sure all is ok
cmd2 = "play newsong.wav"
os.system(cmd2)

