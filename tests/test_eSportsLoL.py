import os
import unittest
from sportradar import eSportsLoL

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_ESPORTSLOL"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = eSportsLoL.eSportsLoL(api_key, format_="json", timeout=5, sleep_time=1.5)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("eSportsLoL"))
        cls.auth = api_key
        cls.api = api
        cls.year = 2018
        cls.month = 6
        cls.day = 1
        cls.team_id_1 = "sr:competitor:240582"
        cls.team_id_2 = "sr:competitor:240564"
        cls.match_id = "sr:match:11753058"
        cls.player_id = "sr:player:949022"
        cls.team_id = "sr:competitor:240582"
        cls.tournament_id = "sr:tournament:2450"

    def test_get_dailyresults(self):
        """Test the daily results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_dailyresults(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_dailyschedule(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_dailyschedule(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_deletedmatches(self):
        """Test the deleted matches GET query"""
        msg = "Response status is not 200"
        response = self.api.get_deletedmatches(self)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_head_2_head(self):
        """Test the head-2-head GET query"""
        msg = "Response status is not 200"
        response = self.api.get_head_2_head(self.team_id_1, self.team_id_2)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_matchlineups(self):
        """Test the match lineups GET query"""
        msg = "Response status is not 200"
        response = self.api.get_matchlineups(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_matchprobabilities(self):
        """Test the match probabilities GET query"""
        msg = "Response status is not 200"
        response = self.api.get_matchprobabilities(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_matchsummary(self):
        """Test the match summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_matchsummary(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_playerprofile(self):
        """Test the player profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_playerprofile(self.player_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_teamprofile(self):
        """Test the team profile GET query"""
        msg = "Response status is not 200"
        response = self.api.get_teamprofile(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_teamresults(self):
        """Test the team results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_teamresults(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_teamschedule(self):
        """Test the team schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_teamschedule(self.team_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentinfo(self):
        """Test the tournament info GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentinfo(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentlivesummary(self):
        """Test the tournament live summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentlivesummary(self)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentresults(self):
        """Test the tournament results GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentresults(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentschedule(self):
        """Test the tournament schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentschedule(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentseasons(self):
        """Test the tournament seasons GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentseasons(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentstandings(self):
        """Test the tournament standings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentstandings(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournamentsummary(self):
        """Test the tournament summary GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournamentsummary(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tournaments(self):
        """Test the tournaments GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tournaments(self)
        self.assertEqual(response.status_code, 200, msg)
