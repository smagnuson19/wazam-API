from flask import Flask, jsonify, request
from speech2text import *
from genius import *
from flask_cors import CORS
import os
import spotipy


app = Flask(__name__)
CORS(app)

@app.route("/music", methods = ['Post'])
def music():
    if request.method == 'POST':
        file = request.files.to_dict()
        print(file['Blob'])

        file['Blob'].save("ITEM.webm")
        path = os.getcwd()
        track = path + "/ITEM.webm"

        lyrics = speech2text(track)
        if(lyrics == None):
            return("No tracks matched, please try again.")
        else:

            songs = get_song_title(lyrics)
            # for track in songs:
            #     spotifyInfo = getSpotify(track['artist'], track['title'])
            #     print(spotifyInfo)
            return jsonify(songs)

def getSpotify(artist, trackName):
    spotipy.Spotify()
    results = spotify.search(q='track:' + trackName + '%20' + 'artist:' + artist, type='track', limit = 1)
    return results

@app.route("/", methods = ['Get'])
def index():
    return "Welcome to our API"



if __name__ == "__main__":
    app.run()
