import os
import unittest
from sportradar import Motorsport

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_MOTORSPORT"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Motorsport.Motorsport(api_key, format_="json", timeout=5, sleep_time=1.2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Motorsport"))
        cls.auth = api_key
        cls.api = api
        cls.competitor_id = "sr:competitor:66632"
        cls.year = 2018
        cls.month = 4
        cls.day = 15
        cls.tournament_id = "sr:tournament:293"
        cls.match_id = "sr:match:9251633"


    def test_competitor_profile(self):
        """Test the competitor profile GET query"""
        msg = "Response status is not 200"
        response = self.api.competitor_profile(self.competitor_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_competitor_results(self):
        """Test the competitor results GET query"""
        msg = "Response status is not 200"
        response = self.api.competitor_results(self.competitor_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_competitor_schedule(self):
        """Test the competitor schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.competitor_schedule(self.competitor_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_daily_results(self):
        """Test the daily results GET query"""
        msg = "Response status is not 200"
        response = self.api.daily_results(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_daily_schedule(self):
        """Test the daily schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.daily_schedule(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)

    def test_head_to_head(self):
        """Test the head to head GET query"""
        msg = "Response status is not 200"
        response = self.api.head_to_head(self.competitor_id, self.competitor_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_seasons(self):
        """Test the seasons GET query"""
        msg = "Response status is not 200"
        response = self.api.seasons(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_sport_event_probabilities(self):
        """Test the sport event probabilities GET query"""
        msg = "Response status is not 200"
        response = self.api.sport_event_probabilities(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_sport_event_timeline(self):
        """Test the sport event timeline GET query"""
        msg = "Response status is not 200"
        response = self.api.sport_event_timeline(self.match_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_tournament_info(self):
        """Test the tournament info GET query"""
        msg = "Response status is not 200"
        response = self.api.tournament_info(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_tournament_list(self):
        """Test the tournament list GET query"""
        msg = "Response status is not 200"
        response = self.api.tournament_list()
        self.assertEqual(response.status_code, 200, msg)

    def test_tournament_live_standings(self):
        """Test the tournament live standings GET query"""
        msg = "Response status is not 200"
        response = self.api.tournament_live_standings(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_tournament_results(self):
        """Test the tournament results GET query"""
        msg = "Response status is not 200"
        response = self.api.tournament_results(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_tournament_schedule(self):
        """Test the tournament schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.tournament_schedule(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_tournament_standings(self):
        """Test the tournament standings GET query"""
        msg = "Response status is not 200"
        response = self.api.tournament_standings(self.tournament_id)
        self.assertEqual(response.status_code, 200, msg)
