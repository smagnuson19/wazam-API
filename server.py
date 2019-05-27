from flask import Flask, jsonify, request
from speech2text import *
from genius import *
from flask_cors import CORS
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


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
        print(lyrics)
        if(lyrics == None):
            return jsonify("No tracks matched, please try again.")
        else:
            songs = get_song_title(lyrics)
            for track in songs:
                spotifyURL = getSpotify(track['artist'], track['title'])
                track['spotify'] = spotifyURL
            return jsonify(songs)

def getSpotify(artist, trackName):
    client_credentials_manager = SpotifyClientCredentials(client_id='bfd32c7ebd164161b156849eed4a8ef9', client_secret='04e61280954a4819a08566ba515ad7e3')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    print(artist)
    print(trackName)
    results = sp.search(q='track:' + trackName , type='track', limit = 1)
    if len(results['tracks']['items']) > 0 :
        url = results['tracks']['items'][0]['external_urls']['spotify']
        return (url)
    else:
        return(None)

@app.route("/", methods = ['Get'])
def index():
    return "Welcome to our API"



if __name__ == "__main__":
    app.run()
