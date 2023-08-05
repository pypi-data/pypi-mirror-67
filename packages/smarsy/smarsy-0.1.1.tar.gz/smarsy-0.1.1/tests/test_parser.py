from unittest.mock import patch, mock_open, MagicMock, Mock

import unittest
import subprocess
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '..',
                                             'smarsy')))
# excluding following line for linter as it complains that
# from import is supposed to be at the top of the file
from smarsy.parse import (validate_title, get_user_credentials,
                          open_json_file, validate_object_keys,
                          get_headers, login, Urls,
                          childs_page_return_right_login,
                          convert_to_date_from_russian_written,
                          )  # noqa


class TestsFileOperations(unittest.TestCase):
    @patch('smarsy.parse.open_json_file')
    def test_user_credentials_object_is_the_same_like_in_file(self,
                                                              mock_json_load):
        expected = {
            'language': 'UA',
            'username': 'user',
            'password': 'pass'
        }
        mock_json_load.return_value = expected
        actual = get_user_credentials()
        self.assertEqual(actual, expected)

    @patch('smarsy.parse.open_json_file')
    def test_user_credentials_fails_if_there_is_no_user(self,
                                                        mock_json_load):
        creds = {
            'language': 'UA',
            'notuser': 'user',
            'password': 'pass'
        }
        mock_json_load.return_value = creds
        with self.assertRaises(Exception) as ue:
            get_user_credentials()
        self.assertEqual(
            'Credentials are in the wrong format (username is missing)',
            str(ue.exception))

    @patch('smarsy.parse.open_json_file')
    def test_user_credentials_fails_if_there_is_no_language(self,
                                                            mock_json_load):
        creds = {
            'nolanguage': 'UA',
            'username': 'user',
            'password': 'pass'
        }
        mock_json_load.return_value = creds
        with self.assertRaises(Exception) as ue:
            get_user_credentials()
        self.assertEqual(
            'Credentials are in the wrong format (language is missing)',
            str(ue.exception))

    @patch('smarsy.parse.open_json_file')
    def test_user_credentials_fails_if_there_is_no_password(self,
                                                            mock_json_load):
        creds = {
            'language': 'UA',
            'username': 'user',
            'nopassword': 'pass'
        }
        mock_json_load.return_value = creds
        with self.assertRaises(Exception) as ue:
            get_user_credentials()
        self.assertEqual(
            'Credentials are in the wrong format (password is missing)',
            str(ue.exception))

    @patch('builtins.open')
    @patch('json.load')
    def test_json_load_gets_content_from_provided_file(self,
                                                       stream_mock,
                                                       mock_json_load):
        expected = 'some_path_to_file'
        stream_mock = MagicMock()
        stream_mock.__enter__.Name = MagicMock(get=MagicMock(Name=expected))
        open_json_file(expected)
        mock_json_load.assert_called_with(expected)

    def test_open_json_file_returns_object_from_provided_file(self):
        read_data = mock_open(read_data=json.dumps({'a': 1, 'b': 2, 'c': 3}))
        with patch('builtins.open', read_data):
            result = open_json_file('filename')
        self.assertEqual({'a': 1, 'b': 2, 'c': 3}, result)

    def test_open_json_file_raise_exception_with_non_existing_path(self):
        # test file does not exist
        with self.assertRaises(IOError) as context:
            open_json_file('null')
        self.assertEqual(
            'null does not exist.', str(context.exception))

    def test_open_json_file_raise_exception_when_invalid_json_in_file(self):
        # test file does not exist
        read_data = mock_open(read_data='')
        with patch("builtins.open", read_data):
            with self.assertRaises(ValueError) as context:
                open_json_file('filename')
            self.assertEqual(
                'filename is not valid JSON.', str(context.exception))

    def test_validate_object_keys_all_keys_exists(self):
        keys_list = ('language', 'username', 'password')
        creds = {
            'language': 'UA',
            'username': 'user',
            'password': 'pass'
        }
        self.assertTrue(validate_object_keys(keys_list, creds))

    def test_validate_object_keys_raise_exception_with_wrong_key(self):
        keys_list = ('language', 'username', 'password')
        creds = {
            'language': 'UA',
            'username': 'user',
            'nopassword': 'pass'
        }
        with self.assertRaises(Exception) as ke:
            validate_object_keys(keys_list, creds)
        self.assertEqual('Key is missing', str(ke.exception))

    @patch('smarsy.parse.open_json_file')
    def test_user_headers_object_is_the_same_like_in_file(self,
                                                          mock_json_load):
        expected = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        mock_json_load.return_value = expected
        actual = get_headers()
        self.assertEqual(actual, expected)


@patch('smarsy.parse.perform_post_request', return_value='Smarsy Login')
@patch('smarsy.parse.get_user_credentials', return_value={'u': 'name'})
@patch('smarsy.parse.get_headers', return_value={'h': '123'})
class TestsParse(unittest.TestCase):
    def test_login_gets_headers(self,
                                mock_headers,
                                user_credentials,
                                mock_request):
        login()
        self.assertTrue(mock_headers.called)

    def test_login_gets_credentials(self,
                                    mock_headers,
                                    user_credentials,
                                    mock_request):
        login()
        self.assertTrue(user_credentials.called)

    @patch('requests.Session', return_value='session')
    def test_login_uses_login_page_in_request(self,
                                              mock_session,
                                              mock_headers,
                                              user_credentials,
                                              mock_request):
        login()
        mock_request.assert_called_with(mock_session.return_value,
                                        Urls.LOGIN.value,
                                        user_credentials.return_value,
                                        mock_headers.return_value)

    @patch('requests.Session', return_value='session')
    def test_login_returns_post_request_text(self,
                                             mock_session,
                                             mock_headers,
                                             user_credentials,
                                             mock_request):
        self.assertEqual(login(), 'Smarsy Login')

    def test_if_empty_keys_raise_exception_with_empty_key(self,
                                                          mock_headers,
                                                          user_credentials,
                                                          mock_request):
        keys_list = ()
        creds = {
            'language': 'UA',
            'username': 'user',
            'nopassword': 'pass'
        }
        with self.assertRaises(Exception) as ke:
            validate_object_keys(keys_list, creds)
        self.assertEqual('Key is empty', str(ke.exception))

    @patch('requests.Session', return_value='session')
    def test_login_with_params_uses_in_request(self, mock_session,
                                               mock_headers,
                                               user_credentials,
                                               mock_request):
        expected = {'username': 'username',
                    'password': 'pass',
                    'language': 'UA'}
        login(username=expected['username'], password=expected['password'])
        mock_request.assert_called_with(mock_session.return_value,
                                        Urls.LOGIN.value,
                                        expected,
                                        mock_headers.return_value)

    @patch('requests.Session', return_value='session')
    def test_login_with_params_returns_post_request_text(self,
                                                         mock_session,
                                                         mock_headers,
                                                         user_credentials,
                                                         mock_request):
        user_credentials.return_value = {'username': 'username',
                                         'password': 'pass',
                                         'language': 'UA'}
        self.assertEqual(login(username='username', password='pass'),
                         mock_request.return_value)


class TestPageContent(unittest.TestCase):

    def test_login_page_has_expected_title(self):
        html = '<html><title>Smarsy - Смарсі - Україна</title></html>'
        actual = validate_title(html)
        self.assertTrue(actual)

    def test_childs_page_has_expected_username(self):
        response_string = '\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" \
                     "http://www.w3.org/TR/html4/strict.dtd">\n<HTML>\n \
                     <HEAD>\n<TITLE>login</TITLE>\n'
        self.assertTrue(childs_page_return_right_login(response_string,
                                                       'login'))

    def test_childs_page_raise_exception_with_unexpected_username(self):
        response_string = '\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" \
                     "http://www.w3.org/TR/html4/strict.dtd">\n<HTML>\n \
                     <HEAD>\n<TITLE>login</TITLE>\n'
        with self.assertRaises(ValueError) as error:
            childs_page_return_right_login(response_string, 'nologin')
        self.assertEqual('Invalid Smarsy Login', str(error.exception))

    @patch('locale.LC_TIME', 100)
    @patch('datetime.datetime')
    @patch('locale.setlocale')
    def test_ru_locale_is_used_when_date_is_formatted(self, mocked_locale,
                                                      mock_dt):
        convert_to_date_from_russian_written('24 февраля 2012 г.')
        mocked_locale.assert_called_with(100, 'ru_RU')

    @patch('datetime.datetime')
    @patch('locale.setlocale')
    def test_convert_to_date_called_with_expected_format_and_date(
        self, mocked_locale, mocked_date
    ):
        date_in_str = '24 февраля 2012 г.'
        convert_to_date_from_russian_written(date_in_str)
        mocked_date.strptime.assert_called_with('24 февраля 2012 г.',
                                                '%d %B %Y г.')

    @patch('locale.setlocale')
    def test_convert_to_date_raise_exeption_with_unexpected_date(
        self, mocked_locale
    ):
        date_in_str = '24 feb 2012'
        with self.assertRaises(ValueError) as error:
            convert_to_date_from_russian_written(date_in_str)
        self.assertEqual('Wrong date format', str(error.exception))

    @patch('datetime.datetime')
    @patch('locale.setlocale')
    def test_convert_to_date_cast_result_to_date(self, mocked_locale,
                                                 mock_dt):
        expected_output = 'casted'
        date_mock = Mock()
        date_mock.date.return_value = expected_output
        mock_dt.strptime.return_value = date_mock
        self.assertEqual(convert_to_date_from_russian_written('', ''),
                         expected_output)


if __name__ == '__main__':
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])
