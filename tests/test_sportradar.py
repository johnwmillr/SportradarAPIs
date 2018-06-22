import os
import unittest
import sportradar as sr

# Import API keys from environment variables
api_key_name = "SPORTRADAR_API_KEY_SOCCER"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(key_name="SPORTRADAR_API_SOCCER_KEY")
api = sr.API(api_key)

class TestAPI(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("\n---------------------\nSetting up Sportradar API tests...\n")
		cls.auth = api_key
		cls.api = api						
		cls.response = cls.api.get_tournaments()

	def test_valid_status(self):
		msg = "Response status is not 200."
		self.assertEqual(self.response.status_code, 200, msg)