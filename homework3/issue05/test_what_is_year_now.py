from what_is_year_now import what_is_year_now
from unittest.mock import patch
from unittest import TestCase
from io import StringIO


class TestWhatIsYearNow(TestCase):
    def test_year_first(self):
        with patch('what_is_year_now.urllib.request.urlopen') as mock_requests:
            resp = StringIO('{"currentDateTime" : "2021-10-07T13:09Z" , "other_param" : "other_value"}')
            mock_requests.return_value = resp
            actual = what_is_year_now()
            expected = 2021
            self.assertEqual(actual, expected)

    def test_year_last(self):
        with patch('what_is_year_now.urllib.request.urlopen') as mock_requests:
            resp = StringIO('{"currentDateTime" : "07.10.2021T13:09Z" , "other_param" : "other_value"}')
            mock_requests.return_value = resp
            actual = what_is_year_now()
            expected = 2021
            self.assertEqual(actual, expected)

    def test_invalid_format(self):
        with patch('what_is_year_now.urllib.request.urlopen') as mock_requests:
            resp = StringIO('{"currentDateTime" : "07-10-2021T13:09Z" , "other_param" : "other_value"}')
            mock_requests.return_value = resp
            with self.assertRaises(ValueError):
                what_is_year_now()
