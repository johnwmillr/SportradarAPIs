import os
import unittest
import sportradar as sr

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_SOCCER"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
        key_name="SPORTRADAR_API_SOCCER_KEY")
api = sr.API(api_key, format_='json', language='en', timeout=5, sleep_time=1.5)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up Sportradar API tests...\n")
        cls.auth = api_key
        cls.api = api

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
        response = self.api.get_match_summary("sr:match:7696036")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_timeline(self):
        """Test the match timeline GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_timeline("sr:match:7696036")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_lineups(self):
        """Test the match lineups GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_lineups("sr:match:7696036")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_probabilities(self):
        """Test the match probabilities GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_probabilities("sr:match:7696036")
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_match_fun_facts(self):
    # # *** API RETURNS 404 IN THEIR EXAMPLE ***
    #     """Test the match fun facts GET query"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_fun_facts("sr:match:10987366")
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_missing_players(self):
        msg = "Response status is not 200."
        response = self.api.get_missing_players("sr:tournament:1")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_mapping(self):
        msg = "Response status is not 200."
        response = self.api.get_player_mapping("teams")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        msg = "Response status is not 200."
        response = self.api.get_player_profile("sr:player:149304")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_rankings(self):
        msg = "Response status is not 200."
        response = self.api.get_player_rankings("sr:tournament:1")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile(self):
        msg = "Response status is not 200."
        response = self.api.get_team_profile("sr:competitor:4715")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_statistics(self):
        msg = "Response status is not 200."
        response = self.api.get_team_statistics("sr:tournament:1", "sr:competitor:4698")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_head2head(self):
        msg = "Response status is not 200."
        response = self.api.get_head2head("sr:competitor:4715", "sr:competitor:4698")
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournaments(self):
        """Test the tournaments GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournaments()
        self.assertEqual(response.status_code, 200, msg)
