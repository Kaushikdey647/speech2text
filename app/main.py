from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

@app.route('/predict',methods=['POST'])
def predict():
    # LOAD AN AUDIO FILE
    # VECTORIZE THE AUDIO FILE
    # RETURN THE JSON DATA
    return jsonify({'success': True})
