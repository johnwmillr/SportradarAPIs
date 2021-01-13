import os
import unittest
from sportradar import Soccer

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_SOCCER"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Soccer.Soccer(api_key, format_='json', language='en', timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Soccer"))
        cls.auth = api_key
        cls.api = api
        cls.player_id = "sr:player:149304"
        cls.team_id = "sr:competitor:4715"
        cls.team_id_2 = "sr:competitor:4698"
        cls.match_id = "sr:match:7696036"
        cls.tournament_id = "sr:tournament:1"

    # How do I write proper tests for these?
    # I assume just checking status code isn't good enough.

    def test_get_daily_results(self):
        """Test the daily results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_daily_results(2018, 6, 20)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_schedule(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200."
        response = self.api.get_daily_schedule(2018, 6, 20)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_live_results(self):
    #     """Test the live results GET query"""
    #     # Requires a game in progress
    #     msg = "Response status is not 200."
    #     response = self.api.get_live_results()
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_match_summary(self):
        """Test the match summary GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_summary(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_timeline(self):
        """Test the match timeline GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_timeline(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_lineups(self):
        """Test the match lineups GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_lineups(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_probabilities(self):
        """Test the match probabilities GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_probabilities(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_match_fun_facts(self):
    # # *** API RETURNS 404 IN THEIR EXAMPLE ***
    #     """Test the match fun facts GET query"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_fun_facts("sr:match:10987366")
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_missing_players(self):
        msg = "Response status is not 200."
        response = self.api.get_missing_players(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_mapping(self):
        msg = "Response status is not 200."
        response = self.api.get_player_mapping("teams")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        msg = "Response status is not 200."
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_player_rankings(self):
    # # *** API RETURNS 404 IN THEIR EXAMPLE ***
    #     msg = "Response status is not 200."
    #     response = self.api.get_player_rankings(self.tournament_id)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile(self):
        msg = "Response status is not 200."
        response = self.api.get_team_profile(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_team_statistics(self):
    # # *** API RETURNS 404 IN THEIR EXAMPLE ***
    #     msg = "Response status is not 200."
    #     response = self.api.get_team_statistics(
    #         self.tournament_id, self.team_id_2)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_head2head(self):
        msg = "Response status is not 200."
        response = self.api.get_head2head(
            self.team_id, self.team_id_2)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournaments(self):
        """Test the tournaments GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournaments()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_info(self):
        """Test the tournament info GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_info(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_standings(self):
        """Test the tournament standings GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_standings(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_live_standings(self):
        """Test the live standings GET query"""
        msg = "Response status is not 200."
        response = self.api.get_live_standings(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_results(self):
        """Test the tournament results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_results(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_schedule(self):
        """Test the tournament schedule GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_schedule(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_seasons(self):
        """Test the tournament seasons GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_seasons(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)
