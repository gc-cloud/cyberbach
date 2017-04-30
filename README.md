# Cyberbach
# Harvard Extension School - Final Project CSCIE63
# Gerardo Castaneda & Stephen Ford

This repository contains the code to host a web app that takes .midi files
as inputs and generates a new .midi file using recurrent neural networks in tensorflow.  


This solution is **heavily based** on Dab Shiebler's [Musical TensorFlow](http://danshiebler.com/2016-08-17-musical-tensorflow-part-two-the-rnn-rbm/) 
article for generating long sequences of polyphonic music by using an RNN_RBM in TensorFlow. 

The original solution was upgraded to work with Tensorflow 1.1  accept user provided  midi files, automatically generate
new music and play the new music online.  See log of major changes below for changes to core code from Dab Shiebler's

To see a demo of our live solution checkout [http://cyberbach.com](cyberbach.com)



# Installation
The instructions below assume that you have installed [anaconda](https://www.continuum.io/downloads) and know how 
virtual environments work.  If you are not familiar with virtual environments it is **highly recommended** that 
you familiarize yourself with them first.    

## Clone this repository
$ git clone git@github.com:gc-cloud/cyberbach.git

## Move to the cyberbach folder

$ cd cyberbach

## Create and activate a conda environment with python 2.7

$ conda create -n tf1.1_py2.7 python=2.7

$ source activate tf1.1_py2.7

## Install tensorflow 1.1

If you have a Mac:   
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.1.0-py3-none-any.whl

If you are using linux   
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp27-none-linux_x86_64.whl

$ pip install --upgrade $TF_BINARY_URL

## Regenerate protobuf ( this step may not be necessary...)
$pip2 install --force-reinstall --upgrade protobuf


## Install dependencies (pandas, tqdm, patplotlib, midi)
$ conda install pandas   
$ conda install -c conda-forge tqdm   
$ conda install matplotlib   
$ pip install python-midi   

# Generating Music with RNN_RBM
### TLDR:
You can generate music by running:
```
python rnn_rbm_generate.py parameter_checkpoints/pretrained.ckpt
```
This will populate the music_outputs directory with midi files that you can play with an application like GuitarBand.

### Training
To train the model, first run the following command to initialize the parameters of the RBM.
```
python weight_initializations.py <source_music_folder>
```
Then, run the following command to train the RNN_RBM model:
```
python rnn_rbm_train.py <num_epochs>
```
`num_epochs` can be any integer. Set it between 50-500, depending on the hyperparameters.

### Generation:
The command:
```
python rnn_rbm_generate.py <path_to_ckpt_file>
```
will generate music by using the weights stored in the `path_to_ckpt_file`. You can use the provided 
file `parameter_checkpoints/pretrained.ckpt`, or you can use one of the ckpt files that you create. When you 
run `train_rnn_rbm.py`, the model creates a `epoch_<x>.ckpt` file in the parameter_checkpoints directory every 
couple of epochs. 


## To-dos
add calls to rnn_rbm_train and rnn_rbm_generate from weight_initializations.py so everything 
is executed with one call
set independent name for trained ckpt for a given run


## Log of major changes

Steps to upgrade original code to  Tensorflow 1.1:   


1) Upgraded all  python scripts using the [tensorflow upgrade utility](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/tools/compatibility)   

2) In midi_manipulation.py changed get_song to remove float32 vs int32 inconsistency   
```
def get_song(path):
    #Load the song and reshape it to place multiple timesteps next to each other
    song = np.array(midiToNoteStateMatrix(path))
    song = song[:int(np.floor(song.shape[0]/num_timesteps)*num_timesteps)]
    song = np.reshape(song, [song.shape[0]/num_timesteps, song.shape[1]*num_timesteps])
    return song
```

3) In RBM.py replaced the call to deprecated control_flow_ops   

```
#[_, _, x_sample] = control_flow_ops.While(lambda count, num_iter, *args: count < num_iter,
    #                                     gibbs_step, [ct, tf.constant(k), x], 1, False)
    # [_, _, x_sample] = tf.while_loop(lambda count, num_iter, *args: count < num_iter, gibbs_step,


    [_, _, x_sample] = tf.while_loop(lambda count, num_iter, *args: count < num_iter, gibbs_step,
                                     [ct, tf.constant(k), x], parallel_iterations=1, back_prop=False)
```

4) In rnn_rbm.py resolved float32 vs int32 issue, replaced call to deprecated control_flow_ops, and 
added explicit shape_invariants declaration 

```
   def generate(num, x=x, size_bt=size_bt, u0=u0, n_visible=n_visible, prime_length=100):
        """
            This function handles generating music. This function is one of the outputs of the build_rnnrbm function
            Args:
                num (int): The number of time steps to generate
                x (tf.placeholder): The data vector. We can use feed_dict to set this to the music primer. 
                size_bt (tf.float32): The batch size
                u0 (tf.Variable): The initial state of the RNN
                n_visible (int): The size of the data vectors
                prime_length (int): The number of times teps into the primer song that we use befoe beginning to generate music
            Returns:
                The generated music, as a tf.Tensor

        """
        Uarr = tf.scan(rnn_recurrence, x, initializer=u0)
        # U = Uarr[np.floor(prime_length/midi_manipulation.num_timesteps), :, :]
        U = Uarr[int(np.floor(prime_length / midi_manipulation.num_timesteps)), :, :]
        # [_, _, _, _, _, music] = control_flow_ops.While(lambda count, num_iter, *args: count < num_iter,
        #                                                  generate_recurrence, [tf.constant(1, tf.int32), tf.constant(num), U,
        #                                                  tf.zeros([1, n_visible], tf.float32), x,
        #                                                 tf.zeros([1, n_visible],  tf.float32)])

        time_steps = tf.constant(1, tf.int32)
        iterations = tf.constant(num)
        u_t = tf.zeros([1, n_visible], tf.float32)
        music = tf.zeros([1, n_visible], tf.float32)
        loop_vars = [time_steps, iterations, U, u_t, x, music]

        [_, _, _, _, _, music] = tf.while_loop(lambda count, num_iter, *args: count < num_iter, generate_recurrence,
                                               loop_vars,
                                               shape_invariants=[time_steps.get_shape(), iterations.get_shape(),
                                                                 U.get_shape(), u_t.get_shape(),
                                                                 x.get_shape(), tf.TensorShape([None, 780])])

        return music
```