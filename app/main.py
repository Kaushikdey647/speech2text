'''
/main.py

Purpose: Store the server logic

Created: 04/07/2021
Creator: https://github.com/Kaushikdey647
'''

from flask import Flask, render_template, request, jsonify
from app.utils import predict as process_audio
from app.models import tokenizer, model

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':

        # audio = None
        # try:
        #     audio = request.files.get['audio']
        # except:
        #     pass
        audio = request.files.get('audio')
        print('audio: ', audio)
        if audio is None or audio.filename == '':
            return jsonify({'message': 'No audio file provided'}), 400
        # if audio.content_type != 'audio/wav':
        #     return jsonify({'message': 'Invalid audio file type'})
        try:
            prediction = process_audio(audio, tokenizer, model)
            print('prediction: ', prediction)
            return jsonify({'prediction': prediction}), 200
        except:
            return jsonify({'message': 'Error processing audio file'}), 500


if __name__ == '__main__':
    app.run(debug=True)