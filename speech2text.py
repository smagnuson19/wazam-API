# converting speech to text
from watson_developer_cloud import SpeechToTextV1
from MyRecognizeCallback import MyRecognizeCallback
from os.path import join, dirname


speech_to_text = SpeechToTextV1(
    iam_apikey='boED_50f9NKg5_1xaA9pKuLMP8ihPu7OxA-sW-3O--Le',
    url='https://stream.watsonplatform.net/speech-to-text/api'
)

speech_to_text.set_detailed_response(True)
myRecognizeCallback = MyRecognizeCallback()

ex_file = '/Users/kylehalloran/Desktop/College_Park.flac'

def speech2text(file):
    with open(join(dirname(__file__), './.', file),'rb') as audio_file:

        results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/wav',
            word_alternatives_threshold=0.9,
            keywords=['colorado', 'tornado', 'tornadoes'],
            keywords_threshold=0.5

        ).get_result()["results"][0]["alternatives"][0]["transcript"]

    return(results)

# print(speech2text(ex_file))


