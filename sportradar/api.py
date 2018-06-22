# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

import requests

class API(object):
	"""
	Sportradar API

	Currently only supports the "Soccer INTL Trial v3" API
	Will be generalized to support multiple APIs from Sportradar (e.g. NFL, NBA, etc.)

	"""	

	session = requests.Session()
	session.headers = {'application': "PythonAPI"}

	def __init__(self, api_key, format='json', timeout=5, language='en'):
		self._auth = {'api_key': api_key}
		self._LANGUAGE = language
		self._BASE_URL = 'https://api.sportradar.us/soccer-t3/intl/' + self._LANGUAGE + '/'
		self._FORMAT = "." + format.strip(".")
		self.timeout = timeout						
		""" API instance Constructor

		:param auth: API key provided by Sportradar
		:param format: response format to request from the API (json, xml)
		:param timeout: timeout for response (seconds)
		:param language: language of the response data
		"""

	def _make_request(self, path, method='GET'):
		"""Make a GET or POST request to the API"""
		full_uri = self._BASE_URL + path + self._FORMAT	
		response = self.session.request(method,
										full_uri,
										timeout=self.timeout,
										params=self._auth)		
		response.raise_for_status() # Raise error for bad status
		return response	

	def get_tournaments(self):
		"""Provides the list of International Soccer tournaments"""
		path = "tournaments"
		return self._make_request(path)

	def get_tournament_info(self, tournament_id):
		"""Provides information for International Soccer tournaments"""
		path = "tournaments/{_id}/info".format(_id=tournament_id)
		return self._make_request(path)

	def get_team_profile(self, team_id):
		"""Team information, including player roster information"""
		path = "teams/{_id}/profile".format(_id=team_id)
		return self._make_request(path)
	
	def get_player_profile(self, player_id):
		"""Provides player information"""
		path = "players/{_id}/profile.{_format}".format(_id=player_id)
		return self._make_request(path)                          
	