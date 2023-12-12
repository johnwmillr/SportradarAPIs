# Sportradar APIs
# Copyright 2018 John W. Miller
# Updated 2023 by Michael Adams (github.com/mad4ms)

# See LICENSE for details.

"""
API details and documentation: https://developer.sportradar.com/io-docs
"""

import requests
import time


class API(object):
    """Sportradar API"""

    # Create a persistent requests connection
    session = requests.Session()
    session.headers = {'application': 'PythonWrapper'}

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        """ Sportradar API Constructor

        :param api_key: key provided by Sportradar, specific to the sport's API
        :param format_: response format to request from the API (json, xml)
        :param language: language of the response data
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests, (free min is 1 second)
        """

        assert api_key != '', 'Must supply a non-empty API key.'
        self.api_key = {'api_key': api_key}
        self.api_root = 'http://api.sportradar.us/'
        self.FORMAT = "." + format_.strip(".")
        self.timeout = timeout
        self._sleep_time = sleep_time

    def _make_request(self, path, method='GET', params=None):
        """Make a GET or POST request to the API

        :param path: the API endpoint path
        :param method: the HTTP method to use (GET, POST)
        :param params: additional parameters to include in the request
        :return: the response from the API
        """
        time.sleep(self._sleep_time)  # Rate limiting
        full_uri = self.api_root + path + self.FORMAT
        print(path)  # Print the path for debugging
        print(full_uri)  # Print the full URI for debugging

        # Update the parameters with the API key

        # Attention: Sportradar has changed some of their API in Handball and possibly other sports too.
        # There is now a limit (100) on how many summaries can be requested at once.
        # Have a look at the get_season_summaries method in Handball.py to see an example.
        if params is None:
            params = {}
        params.update(self.api_key)

        response = self.session.request(method,
                                        full_uri,
                                        timeout=self.timeout,
                                        params=params)
        # response.raise_for_status()  # Raise error for bad status
        return response
