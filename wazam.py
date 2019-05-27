# using the speech2text and get_song_titles functions to produce a list of three songs from an audio file
from speech2text import speech2text
from genius import get_song_title
import spotipy

def getSpotify(artist, trackName):
    sp = spotipy.Spotify()
    results = sp.search(q='track:' + trackName + '%20' + 'artist:' + artist, type='track', limit = 1)
    return results

def wazam(audio_file):
    something = get_song_title("I live my life I live my life on you")
    for i in something:
        print(getSpotify(i['artist'], i['title']))
    return (something)
# testing an example audio file
ex_file = '/Users/kylehalloran/Desktop/College_Park.flac'
print(wazam(ex_file))
