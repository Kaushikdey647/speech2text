import warnings
from torch import argmax
from models import model, tokenizer
import librosa
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
def predict(audio_url):

    input_audio, _ = librosa.load(audio_url, sr=16000) # Sampling Rate: 16000 for word2vec

    input_value = tokenizer(input_audio, return_tensors='pt')['input_values'] #Input value is a dictionary

    predicted_indices = argmax(  model(input_value).logits , dim = -1 ) #get the prediction vector

    return tokenizer.batch_decode( predicted_indices )[0] #decode back to text

if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        print(predict('docs/audio_1.wav'))
        print(predict('docs/audio_2.wav'))
        print(predict('docs/audio_3.wav'))
        print(predict('docs/audio_4.wav'))
        print(predict('docs/audio_5.wav'))