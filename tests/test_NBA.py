import os
import unittest
from sportradar import NBA

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_NBA"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = NBA.NBA(api_key, format_="json", timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("NBA"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.game_id = "114844aa-3c31-4ac7-9afa-0a4f2ae65e0c"
        cls.season_year = "2017"
        cls.season_type = "PST"
        cls.player_id = "ab532a66-9314-4d57-ade7-bb54a70c65ad"
        cls.team_id = "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"
        cls.series_id = "a0ce3990-36a1-4ef3-939b-10d4feab0386"

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

    def test_get_free_agents(self):
        """Test the free agents GET query"""
        msg = "Response status is not 200"
        response = self.api.get_free_agents()
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
        response = self.api.get_league_leaders(self.season_year, self.season_type)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_play_by_play(self):
        """Test the play by play GET query"""
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
        response = self.api.get_rankings(self.season_year, self.season_type)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_schedule(self):
        """Test the schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_schedule(self.season_year, self.season_type)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_statistics_season_to_date(self):
        """Test the seasonal statistics (season to date) GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_statistics_season_to_date(self.season_year, self.season_type, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_schedule(self):
        """Test the series schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_schedule(self.season_year, self.season_type)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_statistics(self):
        """Test the series statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_statistics(self.series_id, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_standings(self):
        """Test the standings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_standings(self.season_year, self.season_type)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile_rosters(self):
        """Test the team profile (rosters) GET query"""
        msg = "Response status is not 200"
        response = self.api.get_team_profile_rosters(self.team_id)
        self.assertEqual(response.status_code, 200, msg)
