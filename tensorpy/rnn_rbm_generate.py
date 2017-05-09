import sys

import tensorflow as tf
from tqdm import tqdm

import rnn_rbm
import midi_manipulation

"""
    This file contains the code for running a tensorflow session to generate music
"""

# The number of songs to generate
num = 1
# The path to the song to use to prime the network
primer_song = 'Pop_Music_Midi/Every Time We Touch - Chorus.midi'


def main(saved_weights_path):
    # This function takes as input the path to the weights of the network
    # First we build and get the parameters odf the network
    x, cost, generate, W, bh, bv, x, lr, Wuh, Wuv, Wvu, Wuu, bu, u0 = rnn_rbm.rnnrbm()

    tvars = [W, Wuh, Wuv, Wvu, Wuu, bh, bv, bu, u0]

    # We use this saver object to restore the weights of the model
    saver = tf.train.Saver(tvars)

    song_primer = midi_manipulation.get_song(primer_song) 

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        # load the saved weights of the network
        saver.restore(sess, saved_weights_path)
        # We generate num songs
        for i in tqdm(range(num)):
            # Prime the network with song primer and generate an original song
            generated_music = sess.run(generate(300), feed_dict={x: song_primer})
            # The new song will be saved here
            #new_song_path = "music_outputs/{}_{}".format(i, primer_song.split("/")[-1])
            new_song_path = "music_outputs/newsong"
            midi_manipulation.write_song(new_song_path, generated_music)

if __name__ == "__main__":
    # Alternate option to run from IDE
    #path_to_ckpt = 'parameter_checkpoints/crystal.ckpt'
    #main(path_to_ckpt)

    main(sys.argv[1])
