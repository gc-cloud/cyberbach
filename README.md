# Cyberbach
# Harvard Extension School - Final Project CSCIE63

This repository contains the code to host a web app that takes .midi files
as inputs and generates a new .midi file using recurrent neural networks in tensorflow.  


This solution is **heavily based** on Dab Shiebler's [Musical TensorFlow](http://danshiebler.com/2016-08-17-musical-tensorflow-part-two-the-rnn-rbm/) 
article for generating long sequences of polyphonic music by using an RNN_RBM in TensorFlow. 

The original solution was upgraded to work with Tensorflow 11, accept user provided  midi files, automatically generate
new music and play the new music online

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

$ conda create -n tf10_py2.7 python=2.7

$ source activate tf10_py2.7

## Install tensorflow 11

If you have a Mac:   
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.10.0-py2-none-any.whl

If you are using linux   
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl

$ pip install --upgrade $TF_BINARY_URL

## Regenerate protobuf
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
python weight_initializations.py
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
will generate music by using the weights stored in the `path_to_ckpt_file`. You can use the provided file `parameter_checkpoints/pretrained.ckpt`, or you can use one of the ckpt files that you create. When you run `train_rnn_rbm.py`, the model creates a `epoch_<x>.ckpt` file in the parameter_checkpoints directory every couple of epochs. 


## To-dos
add calls to rnn_rbm_train and rnn_rbm_generate from weight_initializations.py so everything 
is executed with one call
set independent name for trained ckpt for a given run