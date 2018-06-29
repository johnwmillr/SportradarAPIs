import os
import unittest
from sportradar import Golf

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_GOLF"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Golf.Golf(api_key, format_="json", timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Golf"))
        cls.auth = api_key
        cls.api = api
        cls.golf_tour = "lpga"
        cls.year = 2018
        cls.tournament_id = "b95ab96b-9a0b-4309-880a-ad063cb163ea"
        cls.round_number = "4"
        cls.month = 6
        cls.day = 1

    def test_get_tournament_schedule(self):
        """Test the tournament schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_schedule(self.golf_tour, self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profiles(self):
        """Test the player profiles GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_profiles(self.golf_tour, self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_summary(self):
        """Test the tournament summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_summary(self.golf_tour, self.year, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_leaderboard(self):
        """Test the tournament leaderboard GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_leaderboard(self.golf_tour, self.year, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_hole_statistics(self):
        """Test the tournament hole statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournament_hole_statistics(self.golf_tour, self.year, self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tee_times_per_round(self):
        """Test the tee times per round GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tee_times_per_round(self.golf_tour, self.year, self.tournament_id, self.round_number)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_scorecards_per_round(self):
        """Test the scorecards per round GET query"""
        msg = "Response status is not 200"
        response = self.api.get_scorecards_per_round(self.golf_tour, self.year, self.tournament_id, self.round_number)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_statistics(self):
        """Test the player statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_statistics(self.golf_tour, self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_change_log(self):
        """Test the daily change log GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_change_log(self.golf_tour, self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_official_world_golf_rankings(self):
        """Test the official world golf rankings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_official_world_golf_rankings(self.year)
        self.assertEqual(response.status_code, 200, msg)
