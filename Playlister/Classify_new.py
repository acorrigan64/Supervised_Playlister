import pickle
import os
import pandas as pd
import numpy as np
import shutil
# Preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler

#Keras
import keras


#Custom Functions
import Funct


#Loading the model, labels and scaler
encoder = pickle.load(open( "encoder.p", "rb" ) )
scaler = pickle.load(open( "scaler.p", "rb" ) )
model = pickle.load(open( "model.p", "rb" ) )

#Generating data for new songs

def clean_songnames(folder):

    path = folder
    for filename in os.listdir(path):
        #print(filename)
        os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ', '_').lower())) 

def generate_csv(file,CSV_name):
    Funct.new_file(CSV_name)
    for filename in os.listdir(file):
        if not filename.startswith('.') and os.path.isfile(os.path.join(file, filename)):
            song_name = f'./{file}/{filename}'
            Funct.get_data(song_name,CSV_name,30,'NA',True,True)
        
def make_playlists(file,CSV_name):
    

    generate_csv(file,CSV_name)
    Names, Classes = load_and_normalize(CSV_name,False)
    for i in range(len(Names)):
        print(os.path.basename(Names[i]))
        shutil.move(Names[i], f'./genres_2/{Classes[i]}/{os.path.basename(Names[i])}')
       
def remove_spaces(file):
    path = file
    for filename in os.listdir(path):
        #print(filename)
        os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ', '_').lower()))
    
    

def load_and_normalize(target_file,debug):
    
    data=pd.read_csv(target_file)
    data.head
    Song_Names = data.filename.to_list()
    data = data.drop(['filename'],axis=1)
    data.head()
    if debug == True:
        print(data)
    # normalizing
    x = np.array(data.iloc[:, :-1], dtype = float)
    X_new = scaler.transform(x)
    if debug == True:
        print(X_new)
    Y_new = model.predict_classes(X_new)
    Classes = encoder.inverse_transform(Y_new.tolist()) 
    for i in range(len(Classes)):
        print("Song= %s, Predicted= %s" % (Song_Names[i],Classes[i]))
    return Song_Names, Classes
    
