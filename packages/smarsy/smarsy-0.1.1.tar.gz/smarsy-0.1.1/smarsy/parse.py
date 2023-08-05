import json
import locale
import os
import datetime
from typing import List, Tuple, Union

import requests
from bs4 import BeautifulSoup

from enums import Urls


def perform_get_request(session, url, params=None, headers=None):
    r = session.get(url=url, params=params, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        raise requests.HTTPError("Error code - {}".format(r.status_code))


def perform_post_request(session, url, data=None, headers=None, encoding=None):
    """
    Performs post request.

    :param session: `Request` session
    :param url: URL for `Request` object
    :param data: (optional) Dictionary, list of tuples, bytes, or
      file-like object to send in the body of the `Request`
    :param headers: (optional) HTTP headers
    :returns: Response text
    :raises HTTPError: raises on reponse status code <> 200
    """
    r = session.post(url=url, data=data, headers=headers)
    r.encoding = encoding
    if r.status_code == 200:
        return r.text
    else:
        raise requests.HTTPError("Error code - {}".format(r.status_code))


def validate_title(html):
    if BeautifulSoup(html, 'html.parser').title.text == \
            'Smarsy - Смарсі - Україна':
        return True
    else:
        raise Exception


def open_json_file(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except IOError:
        raise IOError('{} does not exist.'.format(filename))
    except ValueError:
        raise ValueError('{} is not valid JSON.'.format(filename))


def validate_object_keys(keys: Union[Tuple[str], List[str]], test_json):
    if len(keys):
        for key in keys:
            if key in test_json.keys():
                continue
            raise Exception('Key is missing')
        return True
    else:
        raise Exception('Key is empty')


def get_user_credentials():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '..', 'cfg', 'login.json'))
    login = open_json_file(file_path)
    em = 'Credentials are in the wrong format ({} is missing)'
    for key in ('language', 'username', 'password'):
        if key in login.keys():
            continue
        raise Exception(em.format(key))
    return login


def get_headers():
    """
    Headers for HTTP request.

    :returns: Headers for HTTP request
    """
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '..', 'cfg', 'headers.json'))
    return open_json_file(file_path)


def childs_page_return_right_login(response_page, smarsy_login):
    """
    Receive HTML page from login function and check we've got expected source
    """
    if smarsy_login in response_page:
        return True
    else:
        raise ValueError('Invalid Smarsy Login')


def convert_to_date_from_russian_written(date_in_str, format='%d %B %Y г.'):
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    try:
        date_with_time = datetime.datetime.strptime(date_in_str, format)
        return date_with_time.date()
    except:
        raise ValueError('Wrong date format')


def login(username=None, password=None):
    """
    Perform login to Smarsy.

    :returns: true on succesful login
    """
    session = requests.Session()
    if username and password:
        user_credentials = {'username': username,
                            'password': password,
                            'language': 'UA'}
    else:
        user_credentials = get_user_credentials()
    response = perform_post_request(session,
                                    Urls.LOGIN.value,
                                    user_credentials,
                                    get_headers())
    return response


class Person(object):
    def __init__(self, first_name, second_name,
                 middle_name, person_type, birth_date):
        self.first_name = first_name
        self.second_name = second_name
        self.middle_name = middle_name
        self.person_type = person_type
        self.birth_date = birth_date
