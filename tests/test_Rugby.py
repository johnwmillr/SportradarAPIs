import os
import unittest

from sportradar import Rugby

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_RUGBY"
api_key = os.environ.get(api_key_name, None)
msg = "Must declare environment variable: "
msg += "{key_name}".format(key_name=api_key_name)
assert api_key is not None, msg
api = Rugby.Rugby(api_key, format_='json', language='en', timeout=5,
                  rugby_type="union", sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Rugby"))
        cls.auth = api_key
        cls.api = api
        cls.player_id = "sr:player:402946"
        cls.team_id = "sr:competitor:4217"
        cls.team_id_2 = "sr:competitor:4218"
        cls.match_id = ""
        cls.season_id = "sr:season:77345"

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

    def test_get_daily_live_results(self):
        """Test the live results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_daily_live_results()
        self.assertEqual(response.status_code, 200, msg)

    def get_daily_live_summaries(self):
        """Test the live results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_daily_live_summaries()
        self.assertEqual(response.status_code, 200, msg)

    # Todo: Add match id and uncomment this part
    #
    # def test_get_match_summary(self):
    #     """Test the match summary GET query"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_summary(self.match_id)
    #     self.assertEqual(response.status_code, 200, msg)

    # def test_get_match_timeline(self):
    #     """Test the match timeline GET query"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_timeline(self.match_id)
    #     self.assertEqual(response.status_code, 200, msg)

    # def test_get_match_timeline_delta(self):
    #     """Test the match timeline delta"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_timeline_delta(self.match_id)
    #     self.assertEqual(response.status_code, 200, msg)

    # def test_get_match_lineups(self):
    #     """Test the match lineups GET query"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_lineups(self.match_id)
    #     self.assertEqual(response.status_code, 200, msg)

    # def test_get_match_probabilities(self):
    #     """Test the match probabilities GET query"""
    #     msg = "Response status is not 200."
    #     response = self.api.get_match_probabilities(self.match_id)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        msg = "Response status is not 200."
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile(self):
        msg = "Response status is not 200."
        response = self.api.get_team_profile(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_results(self):
        msg = "Response status is not 200."
        response = self.api.get_team_results(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_schedule(self):
        msg = "Response status is not 200."
        response = self.api.get_team_schedule(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_vs_team(self):
        msg = "Response status is not 200."
        response = self.api.get_team_vs_team(self.team_id, self.team_id_2)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_info(self):
        msg = "Response status is not 200."
        response = self.api.get_season_info(self.season_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_list(self):
        """Test the season GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_list()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_list_previous(self):
        """Test the season previous GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_list_previous(self.season_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_results(self):
        """Test the season results GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_results(self.season_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_schedule(self):
        """Test the season schedule GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_schedule(self.season_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_standings(self):
        """Test the season standings GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_standings(self.season_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_live_standings(self):
        """Test the season live standing GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_live_standings(self.season_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_season_summaries(self):
        """Test the tournament seasons GET query"""
        msg = "Response status is not 200."
        response = self.api.get_season_summaries(self.season_id)
        self.assertEqual(response.status_code, 200, msg)
