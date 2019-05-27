# using the speech2text and get_song_titles functions to produce a list of three songs from an audio file
from speech2text import speech2text
from genius import get_song_title
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

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

def wazam(audio_file):
    something = get_song_title("Needles to say i keep a check")
    print(something)
    for i in something:
        song = getSpotify(i['artist'], i['title'])
        print(song)

# testing an example audio file
ex_file = '/Users/kylehalloran/Desktop/College_Park.flac'
print(wazam(ex_file))
