#!/home/sford/anaconda2/envs/tf1.1_py2.7/bin/python

import os
for file in os.listdir("../tensorweb/mp3files"):
    if file.endswith(".mp3"):
        print(file)
