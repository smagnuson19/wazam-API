from flask import Flask, jsonify, request
from speech2text import *
from genius import *
from flask_cors import CORS
import os


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
        title = get_song_title(lyrics)

    return jsonify(title)

@app.route("/", methods = ['Get'])
def index():
    return "Welcome to our API"



if __name__ == "__main__":
    app.run()
