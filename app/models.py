import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

if __name__ == '__main__':
    print('Loading Models...')

tokenizer = Wav2Vec2Tokenizer.from_pretrained('models/tokenizer')
model = Wav2Vec2ForCTC.from_pretrained('models/model')

if __name__ == '__main__':
    print(model.eval())