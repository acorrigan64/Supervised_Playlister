<h1 align="center">
Supervised Playlister
</h1>

This project uses librosa and a Keras neural network to learn a classifier for your own playlists. Once learned the classifier can then automatically place new songs into the correct playlist.

It currently supports AIFF, WAV and MP3 files. 
<i>Although Windows operating systems may need to install [FFMPEG](https://ffmpeg.org/) to read mp3 files.</i>

This was created as a lockdown project, please let me know any questions and any bugs with the program!

<h2>
Usage
</h2>
To use your own files with the classifier you will need two simple steps.
<h3>
Step 1: Add your existing playlists
</h3>
First your playlist will need to be added, this is after all a supervised classifier!

You will need to create a folder for each playlist in the genre folder in the format: <i style="color:blue">/genres/your_playlist_name</i>
You can then add all of your songs to the individual playlist folder in the format: <i style="color:blue">/genres/your_playlist_name/your_song</i>

Once everything has been added you then need to run the train.py file, this will create four new files!

<b>genre_data.csv</b> This is the CSV data generated from your songs, for full documentation of what each value means have a look at the helpful librosa documentation [Here](https://librosa.org/doc/latest/index.html)

<b>encoder.p</b> A pickle file of the encoder. It transforms your playlists to numerical values, this is needed to transform the predictions from the model to an understandable genre.

<b>scaler.p</b> A pickle file used to scale the input data for unseen songs. This is essential as new songs are going to be run through the new classifier, if new songs were not put through same scalar the input weights to the neural network would be wrong.

<b>model.p</b> This is the neural network learned from the prior playlists.

All .p (Pickle) files are then loaded for step 2!


<h3>Step 2: Testing new songs</h3>
This is the simpler of the two steps.

All you have to do is add your songs that need to be classified in the <i style="color:blue">/New_songs/</i> folder and run the program.

The new songs will then be placed into one of the previosuly made playlists in the <i style="color:blue">/genres/</i> folder.

<h2>Dependancies</h2>
The project uses the following python packages

- Librosa
- Keras
- SKlearn
- Pandas
- Numpy
- OS
- Pickle

<h2>Future Developments</h2>
<h3>Integration for spotify playlists</h3>
<h3>Integration with spotify's music database for better classifiers</h3>
<h3>An unsupervised playlister!</h3>
