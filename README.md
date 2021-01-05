<h1 align="center">
Supervised Playlister
</h1>

This project uses librosa and a Keras neural network to learn a classifier for your own playlists. Once learned the classifier can then automatically place new songs into the correct playlist.

It can support AIFF, WAV and MP3.

This was created as a lockdown project, please let me know any questions and any bugs with the program!

<h2>
Usage
</h2>
To use your own files with the classifier you will need two simple steps.
<h3>
Step 1: Add your existing playlists
</h3>
First your playlist will need to be added, this is after all a supervised classifier!

You will need to create a folder for each playlist in the genre folder in the format: /genres/your_playlist_name
You can then add all of your songs to the individual playlist folder in the format: /genres/your_playlist_name/your_song

Once everything has been added you then need to run the train.py file, this will create four new files!

<b>genre_data.csv</b> This is the CSV data generated from your songs, for full documentation of what each value means have a look at the helpful librosa documentation [Here](https://librosa.org/doc/latest/index.html)

<b>encoder.p</b> A pickle file of the encoder. It transforms your playlists to numerical values, this is needed to transform the predictions from the model to an understandable genre.

<b>scaler.p</b> A pickle file used to scale the input data for unseen 

<b>model.p</b>


The project involved the use of the following technologies:

- Python
- Pandas
- TQDM
- Matplotlib
