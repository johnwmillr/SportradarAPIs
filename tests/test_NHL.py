import os
import unittest
from sportradar import NHL

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_NHL"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = NHL.NHL(api_key, format_="json", timeout=5, sleep_time=1.2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("NHL"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.game_id = "af285aa3-3d80-4051-9449-5b58e5985a4e"
        cls.season = "2016"
        cls.nhl_season = "PST"
        cls.year1 = "2017"
        cls.year2 = "2018"
        cls.player_id = "42b7b605-0f24-11e2-8525-18a905767e44"
        cls.team_id = "4416091c-0f24-11e2-8525-18a905767e44"
        cls.series_id = "6fdf1873-a327-4926-a411-ff55ef95a78a"
        cls.format = ".json"

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

    def test_get_game_faceoffs(self):
        """Test the game faceoffs GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_faceoffs(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_play_by_play(self):
        """Test the game play by play GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_play_by_play(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_summary(self):
        """Test the game summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_summary(self.game_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_game_time_on_ice(self):
        """Test the game time on ice GET query"""
        msg = "Response status is not 200"
        response = self.api.get_game_time_on_ice(self.game_id)
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

    def test_get_league_leaders___goaltending(self):
        """Test the league leaders - goaltending GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_leaders___goaltending(self.season, self.nhl_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_leaders___skaters(self):
        """Test the league leaders - skaters GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_leaders___skaters(self.season, self.nhl_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_league_leaders___daily(self):
        """Test the league leaders - daily GET query"""
        msg = "Response status is not 200"
        response = self.api.get_league_leaders___daily(self.year1, self.nhl_season, self.year2, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_league_leaders___seasonal(self):
    #     """Test the league leaders - seasonal GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_league_leaders___seasonal(self.season, self.nhl_season)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_player_profile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_rankings(self):
    #     """Test the rankings GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_rankings(self.season, self.nhl_season)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_schedule(self):
        """Test the schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_schedule(self.season, self.nhl_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_faceoffs(self):
        """Test the seasonal faceoffs GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_faceoffs(self.season, self.nhl_season, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_seasonal_statistics___season_to_date(self):
        """Test the seasonal statistics - season to date GET query"""
        msg = "Response status is not 200"
        response = self.api.get_seasonal_statistics___season_to_date(self.season, self.nhl_season, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_faceoffs(self):
        """Test the series faceoffs GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_faceoffs(self.series_id, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_schedule(self):
        """Test the series schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_schedule(self.season, self.nhl_season)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_series_statistics(self):
        """Test the series statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_series_statistics(self.series_id, self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_standings(self):
        """Test the standings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_standings(self.season, self.nhl_season)
        self.assertEqual(response.status_code, 200, msg)

    # def test_get_team_leaders___daily(self):
    #     """Test the team leaders - daily GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_team_leaders___daily(self.year1, self.nhl_season, self.year2, self.month, self.day, self.team_id)
    #     self.assertEqual(response.status_code, 200, msg)

    # def test_get_team_leaders___seasonal(self):
    #     """Test the team leaders - seasonal GET query"""
    #     msg = "Response status is not 200"
    #     response = self.api.get_team_leaders___seasonal(self.season, self.nhl_season, self.team_id)
    #     self.assertEqual(response.status_code, 200, msg)

    def test_get_team_profile___roster(self):
        """Test the team profile - roster GET query"""
        msg = "Response status is not 200"
        response = self.api.get_team_profile___roster(self.team_id)
        self.assertEqual(response.status_code, 200, msg)
