# using the speech2text and get_song_titles functions to produce a list of three songs from an audio file
from speech2text import speech2text
from genius import get_song_titles

def wazam(audio_file):
    lyrics = speech2text(audio_file)
    return get_song_titles(lyrics)


# testing an example audio file
ex_file = '/Users/kylehalloran/Desktop/College_Park.flac'
pprint.pprint(wazam(ex_file))
