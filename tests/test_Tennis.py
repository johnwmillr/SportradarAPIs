import os
import unittest
from sportradar import Tennis

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_TENNIS"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Tennis.Tennis(api_key, format_="json", timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Tennis"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.match_id = "sr:match:10134403"
        cls.player_id = "sr:competitor:19578"
        cls.player_id_1 = "sr:competitor:19578"
        cls.player_id_2 = "sr:competitor:18254"
        cls.tournament_id = "sr:tournament:2591"
        cls.team_id = "sr:competitor:298214"
        cls.team_id_1 = "sr:competitor:257813"
        cls.team_id_2 = "sr:competitor:187839"

    def test_get_daily_results(self):
        """Test the daily results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_results(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_schedule(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_schedule(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_deleted_matches(self):
        """Test the deleted matches GET query"""
        msg = "Response status is not 200"
        response = self.api.get_deleted_matches()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_probabilities(self):
        """Test the match probabilities GET query"""
        msg = "Response status is not 200"
        response = self.api.get_match_probabilities(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_summary(self):
        """Test the match summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_match_summary(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_match_timeline(self):
        """Test the match timeline GET query"""
        msg = "Response status is not 200"
        response = self.api.get_match_timeline(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_versus_player(self):
        """Test the player versus player GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_versus_player(self.player_id_1, self.player_id_2)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_results(self):
        """Test the player results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_results(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_schedule(self):
        """Test the player schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_schedule(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_rankings(self):
        """Test the player rankings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_rankings()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_race_rankings(self):
        """Test the player race rankings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_race_rankings()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_double_team_profile(self):
        """Test the double-team profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_double_team_profile(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_double_team_results(self):
        """Test the double-team results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_double_team_results(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_double_team_schedule(self):
        """Test the double-team schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_double_team_schedule(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_double_team_versus_team(self):
        """Test the double team versus team GET query"""
        msg = "Response status is not 200"
        response = self.api.get_double_team_versus_team(self.team_id_1, self.team_id_2)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_doubles_rankings(self):
        """Test the doubles rankings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_doubles_rankings()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_doubles_race_rankings(self):
        """Test the doubles race rankings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_doubles_race_rankings()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_info(self):
        """Test the tournament info GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_info(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_list(self):
        """Test the tournament list GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_list()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_ongoing(self):
        """Test the tournament ongoing GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_ongoing()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_results(self):
        """Test the tournament results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_results(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_schedule(self):
        """Test the tournament schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_schedule(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)
