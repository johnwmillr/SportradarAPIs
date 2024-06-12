import os
import unittest
from sportradar import Formula1

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_FORMULA1"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = Formula1.Formula1(api_key, format_="json", timeout=5, sleep_time=1.2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} tests...\n".format("Formula 1"))
        cls.auth = api_key
        cls.api = api
        cls.competitor_id = "sr:competitor:7135"
        cls.stage_id = "sr:stage:324771"


    def test_competitor_profile(self):
        """Test the competitor profile GET query"""
        msg = "Response status is not 200"
        response = self.api.competitor_profile(self.competitor_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_seasons(self):
        """Test the seasons GET query"""
        msg = "Response status is not 200"
        response = self.api.seasons()
        self.assertEqual(response.status_code, 200, msg)

    def test_stage_probabilities(self):
        """Test the stage probabilities GET query"""
        msg = "Response status is not 200"
        response = self.api.stage_probabilities(self.stage_id)
        self.assertEqual(response.status_code, 200, msg)

    def test_stage_summary(self):
        """Test the stage summary GET query"""
        msg = "Response status is not 200"
        response = self.api.stage_summary(self.stage_id)
        self.assertEqual(response.status_code, 200, msg)
