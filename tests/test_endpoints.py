'''
/tests/test_endpoints.py

Purpose: Test the endpoints

Created: 04/07/2021
Creator: https://github.com/Kaushikdey647
'''

import requests
import unittest

class testEndpoints(unittest.TestCase):
    def test_get_main(self):
        r = requests.get('http://localhost:5000')
        self.assertEqual(r.status_code, 200)

    def test_post_predict(self):
        r = requests.post('http://localhost:5000/predict')
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()