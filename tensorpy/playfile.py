#!/home/ubuntu/anaconda2/envs/tf1.1_py2.7/bin/python
import cgitb
import cgi
import os
import random
import rnn_rbm_generate
import subprocess
import time

cgitb.enable()

# Create our web page
print("Content-type: text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>TensorWeb Music</title>")

print("<meta charset=\"utf-8\"/>")

print(
"<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/css/swipebox.min.css\">")
print("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.min.css\"/>")
print("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css\"/>")
print("<link rel=\"stylesheet\" href=\"../tensorweb/css/main.css\">")
print("<link rel=\"stylesheet\" href=\"../tensorweb/css/gallery.css\">")

print("<script src=\"https://code.jquery.com/jquery-1.11.3.min.js\"></script>")
print(
"<script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/js/jquery.swipebox.min.js\"></script>")
print("<script>")
print("$('.swipebox').swipebox();")
print("</script>")

print("</head>")

print("<body>")

print("<div class=\"header\"> ")
print("<h1>TensorWeb Music</h1>")
print("<p style=\"color:blue\">Your Song is Ready!</p>")
print("</div>")

# ------------------------  Start Processing Composition ------------------
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

print("<pre>")

voice = random.choice(voices)
cmd = "/usr/bin/timidity /home/ubuntu/cyberbach/tensorpy/music_outputs/newsong.mid -OwS2 -x'bank 0\n0 "+voice +"' > t.out 2>&1"
subprocess.call(cmd, shell=True)

# Move the new song to the mp3files directory
cmd ="/bin/cp music_outputs/newsong.wav /home/ubuntu/cyberbach/tensorweb/mp3files/"
subprocess.call(cmd, shell=True)

time.sleep(3)
print("</pre>")


# ------------------------  End Processing  Composition ------------------

print("<div class=\"formsubmit\">")
print("<iframe name=\"mp3frame\" src=\"/tensorweb/mp3files/newsong.wav\">Play Your Song</iframe>")
print("</div>")

print("<div class=\"footer\">")
print(
"<p><a href=\"../tensorweb/index.html\">Create New Song</a> </p>")
print("</div>")

print("</body>")

print("</html>")
