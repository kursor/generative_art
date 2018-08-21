#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:19:09 2018

@author: aaronpenne
"""

import wave

import os

import numpy as np
np.random.seed(1138)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import get_test_data

song_filepath = os.path.join('data', 'cello.wav')
with wave.open(song_filepath, 'rb') as song:
    params = song.getparams()
    for x in range(0,50):
        print(song.readframes(1))
    
#print(params)

song = wave.open(song_filepath, 'rb')
signal = song.readframes(-1)
signal = np.frombuffer(signal, np.int16)



from scipy.io import wavfile
from scipy import signal, fft
T, data = wavfile.read(song_filepath, mmap=True)

f, t, Sxx = signal.spectrogram(data[:,1], T)
plt.pcolormesh(t, f, Sxx)
plt.ylim((0,1000))


N = 300
yf = fft(data[:,0])
xf = np.linspace(0.0, 1000, len(yf))
plt.plot(xf, 2.0/N*np.abs(yf))
