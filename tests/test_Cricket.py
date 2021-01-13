import os
import unittest
from sportradar import Cricket

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_CRICKET"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Cricket.Cricket(api_key, format_='json', language='en', timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Cricket"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2019
        cls.month = 9
        cls.day = 4
        cls.player_id = "sr:player:647920"  
        cls.team_id = "sr:competitor:142690"
        cls.team_id_2 = "sr:competitor:107205"
        cls.match_id = "sr:match:18596810"
        cls.tournament_id = "sr:tournament:25227"
        cls.tour_id = "sr:tour:15538"

    # How do I write proper tests for these?
    # I assume just checking status code isn't good enough.

    def test_get_daily_results(self):
        """Test the daily results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_daily_results(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_schedule(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200."
        response = self.api.get_daily_schedule(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_match_lineups(self):
    #     """Test the match lineups GET query"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_lineups(self.match_id)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_match_probabilities(self):
        """Test the match probabilities GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_probabilities(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

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

    def test_get_match_timeline_delta(self):
        """Test the match timeline delta GET query"""
        msg = "Response status is not 200."
        response = self.api.get_match_timeline_delta(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200."
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile(self):
        """Test the team profile GET query"""
        msg = "Response status is not 200."
        response = self.api.get_team_profile(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_results(self):
        """Test the team results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_team_results(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_schedule(self):
        """Test the team schedule GET query"""
        msg = "Response status is not 200."
        response = self.api.get_team_schedule(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_vs_team(self):
        """Test the team vs team GET query"""
        msg = "Response status is not 200."
        response = self.api.get_team_vs_team(
            self.team_id, self.team_id_2)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tour_list(self):
        """Test the tour list GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tour_list()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tour_schedule(self):
        """Test the tour schedule GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tour_schedule(self.tour_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_info(self):
        """Test the tournament info GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_info(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_leaders(self):
        """Test the tournament leaders GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_leaders(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_list(self):
        """Test the tournament list GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_list()
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

    def test_get_tournament_squads(self):
        """Test the tournament squads GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_squads(self.tournament_id, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournament_standings(self):
        """Test the tournament standings GET query"""
        msg = "Response status is not 200."
        response = self.api.get_tournament_standings(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)


if __name__ == "__main__":
    unittest.main()
