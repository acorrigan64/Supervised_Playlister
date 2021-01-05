import librosa
import pandas as pd
import csv
import string
import matplotlib.pyplot as plt
import numpy as np
import os


def new_file(name):
    header = 'filename chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
    for i in range(1, 21):
        header += f' mfcc{i}'
    header += ' label'
    header = header.split()
    file = open(name, 'w', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(header)

        
def get_data(songname,target_file,start_time,genre,test,debug):
    if debug == True:
        print(songname)
    y, sr = librosa.load(songname, mono=True,offset=start_time, duration=10)
    title= songname.translate({ord(c): None for c in string.whitespace})
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    rmse = librosa.feature.rms(y=y)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{title} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'  
    
    if debug == True:
        print(to_append)
        
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    if test == True:
        to_append += ' NA'
    else:
        to_append += f' {genre}'
    file = open(target_file, 'a', newline='')
    with file:
        writer = csv.writer(file)
        writer.writerow(to_append.split())
        
def replace(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '_')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '_')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name
