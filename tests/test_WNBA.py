import os
import unittest
from sportradar import WNBA

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_WNBA"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = WNBA.WNBA(api_key, format_="json", timeout=3, sleep_time=1.5)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("WNBA"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.game_id = "0144c46e-e830-4082-8558-933a21923e60"
        cls.season_id = "2018"
        cls.wnba_season = "REG"
        cls.player_id = "3f53a238-b4df-4861-b260-73fc309d6e94"
        cls.team_id = "6f017f37-be96-4bdc-b6d3-0a0429c72e89"

    def test_get_daily_change_log(self):
        """Test the daily change log GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_change_log(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_schedule(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_schedule(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_transfers(self):
        """Test the daily transfers GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_transfers(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_boxscore(self):
        """Test the game boxscore GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_boxscore(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_summary(self):
        """Test the game summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_summary(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_injuries(self):
        """Test the injuries GET query"""
        msg = "Response status is not 200"
        response = self.api.get_injuries()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_hierarchy(self):
        """Test the league hierarchy GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_hierarchy()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_leaders(self):
        """Test the league leaders GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_leaders(self.season_id, self.wnba_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_play_by_play(self):
        """Test the play-by-play GET query"""
        msg = "Response status is not 200"
        response = self.api.get_play_by_play(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_rankings(self):
        """Test the rankings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_rankings(self.season_id, self.wnba_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_schedule(self):
        """Test the schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_schedule(self.season_id, self.wnba_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_statistics(self):
        """Test the seasonal statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_statistics(self.season_id, self.wnba_season, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_schedules(self):
        """Test the series schedules GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_schedules(self.season_id, self.wnba_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_standings(self):
        """Test the standings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_standings(self.season_id, self.wnba_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile_rosters(self):
        """Test the team profile (rosters) GET query"""
        msg = "Response status is not 200"
        response = self.api.get_team_profile_rosters(self.team_id)
        self.assertEqual(response.status_code, 200, msg)
