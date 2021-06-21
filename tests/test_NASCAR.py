import os
import unittest
from sportradar import NASCAR

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_NASCAR"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = NASCAR.NASCAR(api_key, format_="json", timeout=5, sleep_time=1.2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("NASCAR"))
        cls.auth = api_key
        cls.api = api
        cls.nascar_series = "mc"
        cls.year = 2017
        cls.race_id = "87f618bf-2ee5-4e6e-b558-7bbc0337e5c7"
        cls.standings_type = "manufacturers"
        cls.month = 6
        cls.day = 1

    def test_get_drivers(self):
        """Test the drivers GET query"""
        msg = "Response status is not 200"
        response = self.api.get_drivers(self.nascar_series, self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_tracks(self):
        """Test the tracks GET query"""
        msg = "Response status is not 200"
        response = self.api.get_tracks()
        self.assertEqual(response.status_code, 200, msg)

    def test_get_schedule(self):
        """Test the schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_schedule(self.nascar_series, self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_playoff_schedule(self):
        """Test the playoff schedule GET query"""
        msg = "Response status is not 200"
        response = self.api.get_playoff_schedule(self.nascar_series, self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_entry_list(self):
        """Test the entry list GET query"""
        msg = "Response status is not 200"
        response = self.api.get_entry_list(self.nascar_series, self.race_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_practice_leaderboard(self):
        """Test the practice leaderboard GET query"""
        msg = "Response status is not 200"
        response = self.api.get_practice_leaderboard(self.nascar_series, self.race_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_qualifying_leaderboard(self):
        """Test the qualifying leaderboard GET query"""
        msg = "Response status is not 200"
        response = self.api.get_qualifying_leaderboard(self.nascar_series, self.race_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_starting_grid(self):
        """Test the starting grid GET query"""
        msg = "Response status is not 200"
        response = self.api.get_starting_grid(self.nascar_series, self.race_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_race_leaderboard(self):
        """Test the race leaderboard GET query"""
        msg = "Response status is not 200"
        response = self.api.get_race_leaderboard(self.nascar_series, self.race_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_driver_rookie_owner_and_manufacturer_standings(self):
        """Test the driver, rookie, owner, and manufacturer standings GET query"""
        msg = "Response status is not 200"
        response = self.api.get_driver_rookie_owner_and_manufacturer_standings(self.nascar_series, self.year, self.standings_type)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_driver_statistics(self):
        """Test the driver statistics GET query"""
        msg = "Response status is not 200"
        response = self.api.get_driver_statistics(self.nascar_series, self.year)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_daily_change_log(self):
        """Test the daily change log GET query"""
        msg = "Response status is not 200"
        response = self.api.get_daily_change_log(self.year, self.month, self.day)
        self.assertEqual(response.status_code, 200, msg)
