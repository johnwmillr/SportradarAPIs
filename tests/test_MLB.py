import os
import unittest
from sportradar import MLB

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_MLB"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = MLB.MLB(api_key, format_="json", timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("MLB"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.event_id = "b6f922df-46c6-483c-8d3b-4235a6fc4520"
        cls.mlb_season = "REG"
        cls.player_id = "6e1cac5c-b059-4b80-a267-5143b19efb27"
        cls.team_id = "aa34e0ed-f342-4ec6-b774-c79b47b60e2d"
        cls.series_id = "0e85bf84-517b-46af-b75e-37514468e06e"

    def test_get_daily_boxscore(self):
        """Test the daily boxscore GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_boxscore(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

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

    # def test_get_daily_summary(self):
    #     """Test the daily summary GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_daily_summary(self.year, self.month, self.day)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_transactions(self):
        """Test the daily transactions GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_transactions(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_boxscore(self):
        """Test the game boxscore GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_boxscore(self.event_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_pitch_metrics(self):
        """Test the game pitch metrics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_pitch_metrics(self.event_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_summary(self):
        """Test the game summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_summary(self.event_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_glossary(self):
        """Test the glossary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_glossary()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_injuries(self):
        """Test the injuries GET query"""
        msg = "Response status is not 200"
        response = self.api.get_injuries()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_depth_chart(self):
        """Test the league depth chart GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_depth_chart()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_hierarchy(self):
        """Test the league hierarchy GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_hierarchy()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_leaders(self):
        """Test the league leaders GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_leaders(self.year, self.mlb_season)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_league_schedule(self):
    #     """Test the league schedule GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_league_schedule(self.year, self.mlb_season)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_play_by_play(self):
        """Test the play-by-play GET query"""
        msg = "Response status is not 200"
        response = self.api.get_play_by_play(self.event_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_rankings(self):
        """Test the rankings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_rankings(self.year, self.mlb_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_pitch_metrics(self):
        """Test the seasonal pitch metrics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_pitch_metrics(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_splits(self):
        """Test the seasonal splits GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_splits(self.year, self.mlb_season, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_statistics(self):
        """Test the seasonal statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_statistics(self.year, self.mlb_season, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_transactions(self):
        """Test the seasonal transactions GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_transactions(self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_schedule(self):
        """Test the series schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_schedule(self.year, self.mlb_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_statistics(self):
        """Test the series statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_statistics(self.series_id, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_standings(self):
        """Test the standings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_standings(self.year, self.mlb_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_depth_chart(self):
        """Test the team depth chart GET query"""
        msg = "Response status is not 200"
        response = self.api.get_team_depth_chart(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_team_profile(self):
    #     """Test the team profile GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_team_profile(self.team_id)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_venues(self):
        """Test the venues GET query"""
        msg = "Response status is not 200"
        response = self.api.get_venues()
        self.assertEqual(response.status_code, 200, msg)
