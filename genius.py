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

    title1 = re.sub('\xa0',' ', response['response']['hits'][0]['result']['full_title'])
    title2 = re.sub('\xa0',' ', response['response']['hits'][1]['result']['full_title'])
    title3 = re.sub('\xa0',' ', response['response']['hits'][2]['result']['full_title'])
    return [title1, title2, title3]


# testing the app: passing in audio file url, converting to lyrics, printing out likely song titles
# example_file = '/Users/kylehalloran/Desktop/heybrother.flac'
# lyrics = speech2text(example_file)
# pprint.pprint(get_song_title(lyrics))
