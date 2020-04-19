import os
import unittest
from sportradar import NCAAMB

api_key_name = "SPORTRADAR_API_KEY_NCAAMB"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, f"Must declare environment variable: ${api_key_name}"
api = NCAAMB.NCAAMB(api_key, format_="json", timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up NCAAMB tests...\n")
        cls.auth = api_key
        cls.api = api
        cls.year = 2020
        cls.month = 3
        cls.day = 7
        cls.game_id = "90180141-5236-473e-b9ee-c264ae4fbc4f"  # clemson vs virginia
        cls.season_year = "2019"
        cls.season_type = "REG"
        cls.team_id = "dcf5c2e7-c227-4c20-af26-715d5f859412"  # clemson
        cls.player_id = "c8438ea2-5422-48d0-8ca1-7d430d83b625"  # Tevin Mack
        cls.league_id = "cd4268ee-07aa-4c4d-a435-ec44ad2c76cb"  # NCAA MEN
        cls.conference_id = "88368ebb-01fb-44d5-a6c6-3e7d46bb3ab7"  # ACC
        cls.week_id = "w5"

    def test_daily_change_log(self):
        response = self.api.get_daily_change_log(
            self.year, self.maxDiff, self.day)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_daily_schedule(self):
        response = self.api.get_daily_schedule(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_game_boxscore(self):
        response = self.api.get_game_boxscore(self.game_id)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_game_summary(self):
        response = self.api.get_game_summary(self.game_id)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_league_hierarchy(self):
        response = self.api.get_league_hierarchy()
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_league_leaders(self):
        response = self.api.get_league_leaders(
            self.year, self.season_type, self.conference_id)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_play_by_play(self):
        response = self.api.get_play_by_play(self.game_id)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_player_profile(self):
        response = self.api.get_player_profile(self.player_id)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_rankings(self):
        response = self.api.get_rankings(self.season_type, self.season_year)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_rankings_by_week(self):
        response = self.api.get_rankings_by_week(
            self.season_type, self.season_year, self.week_id)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_rankings_by_rpi(self):
        response = self.api.get_rankings_by_rpi(self.season_year)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_schedule(self):
        response = self.api.get_schedule(self.season_year, self.season_type)
        self.assertEqual(response.status_code, 200,
                         "response status is not 200")

    def test_get_seasonal_statistics(self):
        response = self.api.get_seasonal_statistics(
            self.season_year, self.season_type, self.team_id)
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")

    def test_get_seasons(self):
        response = self.api.get_seasons()
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")

    def test_get_standings(self):
        response = self.api.get_standings(self.season_year, self.season_type)
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")

    def test_get_team_profile_rosters(self):
        response = self.api.get_team_profile(self.team_id)
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")

    def test_get_tournament_list(self):
        response = self.api.get_tournament_list(
            self.season_type, self.season_year)
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")

    def test_get_tournament_schedule(self):
        tournament_id = "04d4aec8-2d19-450f-8f7a-7050f06c9e43"  # from sportradar api sandbox
        response = self.api.get_tournament_schedule(tournament_id)
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")

    def test_get_tournament_statistics(self):
        tournament_id = "74db39e5-be49-4ec8-9169-0cc20ed9f792"  # from sportradar api sandbox
        team_id = "d203f38a-a166-4258-bca2-e161b591ecfb"  # from sportradar api sandbox
        response = self.api.get_tournament_statistics(tournament_id, team_id)
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")

    def test_get_tournament_summary(self):
        tournament_id = "74db39e5-be49-4ec8-9169-0cc20ed9f792"  # from sportradar api sandbox
        response = self.api.get_seeded_tournament_summary(tournament_id)
        self.assertEqual(response.status_code, 200,
                         "response status code is not 200")
