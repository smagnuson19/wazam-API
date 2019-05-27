# getting song titles from genius search api
from speech2text import speech2text
import requests
import pprint
import re


def get_song_title(lyrics):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + 'H0nKs-NteAExDITisOgp2z-akFjlMXpOH9ztkXTl9AWN2QrN8TBBmnygAXsJXvDs'}
    search_url = base_url + '/search'
    data = {'q': lyrics}
    response = requests.get(search_url, data=data, headers=headers).json()

    songList = []
    for i in range(0,3):
        songAttrs = {}
        songAttrs['title'] = re.sub('\xa0',' ', response['response']['hits'][i]['result']['title'])
        songAttrs['artist'] = re.sub('\xa0',' ', response['response']['hits'][i]['result']['primary_artist']['name'])
        songAttrs['image'] = re.sub('\xa0',' ', response['response']['hits'][i]['result']['header_image_thumbnail_url'])
        songList.append(songAttrs)
    return songList


# testing the app: passing in audio file url, converting to lyrics, printing out likely song titles
# example_file = '/Users/kylehalloran/Desktop/heybrother.flac'
# lyrics = speech2text(example_file)
# pprint.pprint(get_song_title(lyrics))
