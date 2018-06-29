import os
import unittest
from sportradar import NFL

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_NFL"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = NFL.NFL(api_key, format_="json", timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("NFL"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.game_id = "b1dbf64f-822a-49b7-9bf3-070f5d6da827"
        cls.player_id = "9634e162-5ff5-4372-b72b-ee1b0cb73a0d"
        cls.nfl_season = "PST"
        cls.team_id = "33405046-04ee-4058-a950-d606f8c30852"
        cls.nfl_season_week = "10"

    def test_get_daily_change_log(self):
        """Test the daily change log GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_change_log(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_boxscore(self):
        """Test the game boxscore GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_boxscore(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_roster(self):
        """Test the game roster GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_roster(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_statistics(self):
        """Test the game statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_statistics(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_hierarchy(self):
        """Test the league hierarchy GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_hierarchy()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_play_by_play(self):
        """Test the play-by-play GET query"""
        msg = "Response status is not 200"
        response = self.api.get_play_by_play(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_participation(self):
        """Test the player participation GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_participation(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_schedule(self):
        """Test the schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_schedule(self.year, self.nfl_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_statistics(self):
        """Test the seasonal statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_statistics(self.year, self.nfl_season, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_standings(self):
        """Test the standings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_standings(self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile(self):
        """Test the team profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_team_profile(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_roster(self):
        """Test the team roster GET query"""
        msg = "Response status is not 200"
        response = self.api.get_team_roster(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_weekly_schedule(self):
        """Test the weekly schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_weekly_schedule(2017, 'REG', 13)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_weekly_injuries(self):
        """Test the weekly injuries GET query"""
        msg = "Response status is not 200"
        response = self.api.get_weekly_injuries(2017, 'REG', 13)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_weekly_depth_charts(self):
        """Test the weekly depth charts GET query"""
        msg = "Response status is not 200"
        response = self.api.get_weekly_depth_charts(2017, 'REG', 13)
        self.assertEqual(response.status_code, 200, msg)
