import os
import unittest
from sportradar import Handball

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_HANDBALL"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Handball.Handball(api_key, format_='json', language='en', timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Handball"))
        cls.auth = api_key
        cls.api = api
        cls.competition_id = "sr:competition:149" # German bundesliga
        cls.season_id = "sr:season:95685" # German Bundesliga 22/23
        cls.sport_event_id = "sr:sport_event:34738527" # TBV vs. VFL on the 01.09.2022
        cls.team_id = "sr:competitor:3996" # TBV Lemgo Lippe
        cls.team_id_2 = "sr:competitor:3994" # VFL Gummersbach
        cls.player_id = "sr:player:918114" # Zerbe Lukas
        cls.team_id = "sr:competitor:3996" # TBV Lemgo Lippe
        cls.team_id_2 = "sr:competitor:3994" # VFL Gummersbach

    # How do I write proper tests for these?
    # I assume just checking status code isn't good enough.

    def test_get_competitions(self):
        """Test the daily results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_competitions()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasons_for_competition(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200."
        response = self.api.get_seasons_for_competition(self.competition_id)
        self.assertEqual(response.status_code, 200, msg)
        
    def test_get_players_for_season(self):
        """Test the match summary GET query"""
        msg = "Response status is not 200."
        response = self.api.get_players_for_season(self.season_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_sport_event_timeline(self):
        """Test the sport event timeline GET query"""
        msg = "Response status is not 200."
        response = self.api.get_sport_event_timeline(self.sport_event_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200."
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_summaries(self):
        """Test the season summaries GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_summaries(self.season_id)
        self.assertEqual(response.status_code, 200, msg)
