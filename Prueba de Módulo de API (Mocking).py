# api_client.py
import requests

def get_user_info(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# test_api_client.py
import unittest
from unittest.mock import patch
from api_client import get_user_info

class TestApiClient(unittest.TestCase):

    @patch('api_client.requests.get')
    def test_get_user_info(self, mock_get):
        mock_get.return_value.json.return_value = {'id': 1, 'name': 'John Doe'}
        user_info = get_user_info(1)
        self.assertEqual(user_info['name'], 'John Doe')

if __name__ == '__main__':
    unittest.main()

