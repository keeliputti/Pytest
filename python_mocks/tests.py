import unittest
from unittest.mock import MagicMock, patch

import requests.exceptions
from requests.exceptions import Timeout

from main import add, len_joke, get_joke, get_pro_joke

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,2), 4)

class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('main.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value' : 
        {'joke': 'hello world'}}

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), 'hello world')

    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        mock_response.json.return_value = {'value' : 
        {'joke': 'hello world'}}

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), 'No jokes')
    
    @patch('main.requests')
    def test_get_joke_timeout_exception(self, mock_requests):
        #fix: for bellow mentioned mainblem
        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout('Seems that the server is down')
        # TypeError: catching classes thst do not inherit frim the BaseException is not allowed.
        # MagicMock class/obj is not subclass of BaseException class
        self.assertEqual(get_pro_joke(), 'No jokes')

if __name__ == '__main__':
    unittest.main()
    