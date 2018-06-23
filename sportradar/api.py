# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

"""
API details and documentation: https://developer.sportradar.com/io-docs
"""

import requests
import time


class API(object):
    """Sportradar API

    *Currently only supports the "Soccer INTL Trial v3" API*
    *Will be generalized to support multiple APIs from Sportradar
    (e.g. NFL, NBA, etc.)*
    """

    # Create a persistent requests connection
    session = requests.Session()
    session.headers = {'application': 'PythonAPI'}

    def __init__(self, api_key, format_='json', language='en', timeout=5, sleep_time=1.5):
        """ Sportradar API Constructor

        :param api_key: key provided by Sportradar, specific to the sport's API
        :param format_: response format to request from the API (json, xml)
        :param language: language of the response data
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests, (free min is 1 second)
        """

        self.api_key = {'api_key': api_key}
        self._LANGUAGE = language
        self.api_root = 'https://api.sportradar.us/soccer-t3/intl/' + self._LANGUAGE + '/'
        self.FORMAT = "." + format_.strip(".")
        self.timeout = timeout
        self._sleep_time = sleep_time

    def _make_request(self, path, method='GET'):
        """Make a GET or POST request to the API"""
        time.sleep(self._sleep_time)  # Rate limiting
        full_uri = self.api_root + path + self.FORMAT
        response = self.session.request(method,
                                        full_uri,
                                        timeout=self.timeout,
                                        params=self.api_key)
        # response.raise_for_status()  # Raise error for bad status
        return response

    def get_daily_results(self, year, month, day):
        """Provides match information and scoring, for all matches
            played on a given day. The year, month, and day arguments
            must all be of type int.
        """
        path = "schedules/{y:4d}-{m:02d}-{d:02d}/results".format(
            y=year, m=month, d=day)
        return self._make_request(path)

    def get_daily_schedule(self, year, month, day):
        """Provides match played on a certain day
            The year, month, and day arguments must all be of type int.
        """
        path = "schedules/{y:4d}-{m:02d}-{d:02d}/schedule".format(
            y=year, m=month, d=day)
        return self._make_request(path)

    def get_live_results(self):
        """Provides results for live matches"""
        path = "schedules/live/results"
        return self._make_request(path)

    def get_match_summary(self, match_id):
        """Provides match summary, including team statistics and lineups"""
        path = "matches/{_id}/summary".format(_id=match_id)
        return self._make_request(path)

    def get_match_timeline(self, match_id):
        """Provides match information and scoring, including team
        statistics and a play-by-play
        """
        path = "matches/{_id}/timeline".format(_id=match_id)
        return self._make_request(path)

    def get_match_lineups(self, match_id):
        """Provides lineups for a given match"""
        path = "matches/{_id}/lineups".format(_id=match_id)
        return self._make_request(path)

    def get_match_probabilities(self, match_id):
        """Provides match probabilities"""
        path = "matches/{_id}/probabilities".format(_id=match_id)
        return self._make_request(path)

    def get_match_fun_facts(self, match_id):
        """Provides match fun facts"""
        path = "matches/{_id}/funfacts".format(_id=match_id)
        return self._make_request(path)

    def get_match_fun_facts(self, match_id):
        """Provides match fun facts"""
        path = "matches/{_id}/funfacts".format(_id=match_id)
        return self._make_request(path)

    def get_missing_players(self, tournament_id):
        """Provides a listing of players by team who are missing from play"""
        path = "tournaments/{_id}/missing_players".format(_id=tournament_id)
        return self._make_request(path)

    def get_player_mapping(self, mapping):
        """Displays Player and Team IDs from the Soccer v2 API and
            the converted IDs that are used in the Soccer v3 API.
        """
        path = "{mapping}/v2_v3_id_mappings".format(mapping=mapping)
        return self._make_request(path)

    def get_player_profile(self, player_id):
        """Provides player information"""
        path = "players/{_id}/profile".format(_id=player_id)
        return self._make_request(path)

    def get_player_rankings(self, tournament_id):
        """Provides player rankings for goals, assists, points, cards,
        and own goals in a tournament
        """
        path = "tournaments/{_id}/leaders".format(_id=tournament_id)
        return self._make_request(path)

    def get_team_profile(self, team_id):
        """Team information, including player roster information"""
        path = "teams/{_id}/profile".format(_id=team_id)
        return self._make_request(path)

    def get_team_statistics(self, tournament_id, team_id):
        """Team information, including player roster information"""
        path = "tournaments/{tournament_id}/teams/{team_id}/statistics".format(
            tournament_id=tournament_id, team_id=team_id)
        return self._make_request(path)

    def get_head2head(self, team_id_1, team_id_2):
        """Provides information on team versus team results"""
        path = "teams/{_id_1}/versus/{_id_2}/matches".format(
            _id_1=team_id_1, _id_2=team_id_2)
        return self._make_request(path)

    def get_tournaments(self):
        """Provides the list of International Soccer tournaments"""
        path = "tournaments"
        return self._make_request(path)

    def get_tournament_info(self, tournament_id):
        """Provides information for International Soccer tournaments"""
        path = "tournaments/{_id}/info".format(_id=tournament_id)
        return self._make_request(path)

    def get_tournament_standings(self, tournament_id):
        """Provides the standings for International Soccer tournaments"""
        path = "tournaments/{_id}/standings".format(_id=tournament_id)
        return self._make_request(path)

    def get_live_standings(self, tournament_id):
        """Provides the live standings for Soccer tournaments"""
        path = "tournaments/{_id}/live_standings".format(_id=tournament_id)
        return self._make_request(path)

    def get_tournament_results(self, tournament_id):
        """Provides the results for International Soccer tournaments"""
        path = "tournaments/{_id}/results".format(_id=tournament_id)
        return self._make_request(path)

    def get_tournament_schedule(self, tournament_id):
        """Provides the schedule for International Soccer tournaments"""
        path = "tournaments/{_id}/schedule".format(_id=tournament_id)
        return self._make_request(path)

    def get_tournament_seasons(self, tournament_id):
        """Provides the seasons for International Soccer tournaments"""
        path = "tournaments/{_id}/seasons".format(_id=tournament_id)
        return self._make_request(path)
