import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle
import os
# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
#Keras
import keras
import string

#Custom Functions
import Funct


#genres = 'blues classical country disco hiphop jazz metal pop reggae rock'.split()
def clean_files(file):
    filenames = os.listdir(file)
    for filename in filenames:
        os.rename(filename, filename.replace(" ", "-").lower())

def generate_genre_data(target_file,csv_name,debug):
    Funct.new_file(csv_name) 
    genre = [ f.name for f in os.scandir(target_file) if f.is_dir() ]
    if debug == True:
        print(genre)
    Funct.replace(target_file)
    
    for g in genre:
        if debug == True:
            print(g)
        file = target_file+f'{g}'
        for filename in os.listdir(file):
            if not filename.startswith('.') and os.path.isfile(os.path.join(file, filename)):
                songname = file+f'/{filename}'
                Funct.get_data(songname,csv_name,20,g,False,True)

def load_and_train(data_csv,debug):
    data = pd.read_csv(data_csv)
    data.head()

    # Dropping unneccesary columns
    data = data.drop(['filename'],axis=1)
    data.head()
    genre_list = data.iloc[:, -1]
    encoder = LabelEncoder()
    y = encoder.fit_transform(genre_list)


    # normalizing
    scaler = StandardScaler()
    x = np.array(data.iloc[:, :-1], dtype = float)
    scaler.fit(x)
    X = scaler.transform(x)
    #print(X)

    # spliting of dataset into train and test dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    from keras import models
    from keras import layers

    # creating a model
    model = models.Sequential()
    model.add(layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)))

    model.add(layers.Dense(128, activation='relu'))

    model.add(layers.Dense(64, activation='relu'))

    model.add(layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(X_train,
                        y_train,
                        epochs=20,
                        batch_size=128)

    # calculate accuracy
    test_loss, test_acc = model.evaluate(X_test,y_test)
    print('test_acc: ',test_acc)
    # predictions
    predictions = model.predict(X_test)
    np.argmax(predictions[0])

    pickle.dump( encoder, open( "encoder.p", "wb" ) )
    pickle.dump( scaler, open( "scaler.p", "wb" ) )
    pickle.dump( model, open( "model.p", "wb" ) )


generate_genre_data('./genres/','genre_data.csv',True)
load_and_train('genre_data.csv',False)
