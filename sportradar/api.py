# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

import requests

class API(object):
	"""Sportradar API"""	

	session = requests.Session()

	def __init__(self, auth, format='json', timeout=5):
		self.__FORMAT = format.strip(".")
		self.timeout = timeout
		self.auth = auth
		""" API instance Constructor

		:param api_name: Name of the Sportradar API (e.g. 'Soccer INTL Trial v3')
		:param format: response format to request from the API
		"""

	def _make_request(self, full_uri, method='GET'):
		"""Make a GET request to the Sportradar API"""
		response = self.session.request(method,
										full_uri,
										timeout=self.timeout,
										auth=self.auth)

		assert response.status_code == 200, "Error in API request. Status: {}".format(response.status_code) 
		return response


class Soccer_INTL_Trial_v3(API):
	"""Soccer INTL Trial v3 API"""

	def __init__(self, language='en'):
		self._LANGUAGE = language
	    self._BASE_URL = 'https://api.sportradar.us/soccer-t3/intl/' + self._LANGUAGE

	def _format_request(self, partial_uri):        
        return self._BASE_URL + "/" + partial_uri + self.__FORMAT

    def get_tournaments(self):
        """Provides the list of International Soccer tournaments"""
        URI = "tournaments"
        return self._make_request(self._format_request(URI))
    
    def get_tournament_info(self, tournament_id):
        """Provides information for International Soccer tournaments"""
        # tournament_id is found via get_tournaments and follows the sr:tournament:num format
        URI = "tournaments/{_id}/info".format(_id=tournament_id)
        return self._make_request(URI)
    
    def get_team_profile(self, team_id):
        """Team information, including player roster information"""
        URI = "teams/{_id}/profile".format(_id=team_id)
        return self._make_request(URI)
        
    def get_player_profile(self, player_id):
        """"""
        URI = "players/{_id}/profile.{_format}".format(_id=player_id)
        return self._make_request(URI)  