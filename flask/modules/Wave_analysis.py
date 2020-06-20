#!/usr/bin/env python
# coding: utf-8


import librosa
import librosa.display
import soundfile
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
import keras
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import rmsprop
from keras.models import load_model
import matplotlib.pyplot as plt

class Wave_analysis:
    def __init__ (self):
        self.emotions = {'0':'부정적','1':'긍정적'}
        self.loaded_wave = load_model('./model/CNN_by_Wav.h5')
        self.result = 0
        self.r_img='./static/img/'
        print('파형분석을 실행합니다.')

    def extract_feature(self, file_name, mfcc=True,chroma=True,mel=True):
        sf = soundfile.SoundFile(file_name)
        X = sf.read(dtype = 'float32')
        if X.ndim > 1:
            return np.array([])
        sr = sf.samplerate
        if chroma:
            stft = np.abs(librosa.stft(X))
        result = np.array([])
        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X,sr=sr,n_mfcc=40).T,axis=0)
            result = np.hstack((result,mfccs))
            #print(result.shape)
        if chroma:
            chromas = np.mean(librosa.feature.chroma_stft(S=stft,sr=sr).T,axis=0)
            result = np.hstack((result,chromas))
            #print(result.shape)
        if mel:
            mels = np.mean(librosa.feature.melspectrogram(X,sr=sr).T,axis=0)
            result = np.hstack((result,mels))
            #print(result.shape)
        sf.close()
        return result



    def file_load(self, filepath):
        x = glob.glob(filepath)
        t1 = [self.extract_feature(x[0])]
        return self.loaded_wave.predict(np.expand_dims(np.array(t1),-1),batch_size=100)


    def result_wave(self, analysis_wave):
        max_emo = max(analysis_wave[0])
        emo_W = str(analysis_wave.tolist()[0].index(max_emo))
        percent = max_emo * 100
        emo_W = self.emotions[emo_W]
        return emo_W, percent


    def emo_cross(self,emo_t,emo_w,percent_t,percent_w):
        if emo_t == emo_w:
            self.result = (200-(max(percent_t,percent_w) - min(percent_t,percent_w)))//2
        else:
            self.result = (200-(max(percent_t,percent_w) + min(percent_t,percent_w)))//2
        if self.result <= 20:
            self.r_img += '20%.png'
        elif 20 < self.result <= 40:
            self.r_img += '40%.png'
        elif 40 < self.result <= 60:
            self.r_img += '60%.png'
        elif 60 < self.result <= 80:
            self.r_img += '80%.png'
        else:
            self.r_img += '100%.png'
        return self.result,self.r_img
'''
    def save_wave_form(self,filename):
        # filename == f.filename
        y, sr = librosa.load(filename, duration=10)
        plt.figure()
        librosa.display.waveplot(y, sr=sr)
        plt.title('Monophonic')
        plt.savefig('./static/img/wave_fig.jpg')
        return './static/img/wave_fig.jpg'
'''
