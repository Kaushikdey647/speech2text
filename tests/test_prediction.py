'''
/tests/test_prediction.py

Purpose: Test the prediction logic

Created: 04/07/2021
Creator: https://github.com/Kaushikdey647
'''

import requests
import unittest


class testPrediction(unittest.TestCase):
    def test_endpoint_uptime_1(self):
        r = requests.post('http://localhost:5000/predict',files={'audio': open('docs/audio_1.wav', 'rb')})
        print(r.text)
        self.assertEqual(r.status_code, 200)

    def test_endpoint_uptime_2(self):
        r = requests.post('http://localhost:5000/predict',files={'audio': open('docs/audio_3.wav', 'rb')})
        print(r.text)
        self.assertEqual(r.status_code, 200)

    def test_endpoint_uptime_3(self):
        r = requests.post('http://localhost:5000/predict',files={'audio': open('docs/audio_5.wav', 'rb')})
        print(r.text)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
