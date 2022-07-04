'''
/models.py

Purpose: Stores the models to be used in the API

Created: 04/07/2021
Creator: https://github.com/Kaushikdey647
'''

import warnings



if __name__ == '__main__':
    print('Fetching Libraries...')

from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

if __name__ == '__main__':
    print('Loading Models...')

#Catching deprecation warnings [ NOT HEALTHY ]
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        tokenizer = Wav2Vec2Tokenizer.from_pretrained('models/tokenizer')
        model = Wav2Vec2ForCTC.from_pretrained('models/model')
    except:
        tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
        model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

if __name__ == '__main__':
    print(model.eval())