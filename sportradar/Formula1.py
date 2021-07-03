# Sportradar APIs
# Copyright 2018 John W. Miller
# Copyright 2021 Teresa Fontanella De Santis
# See LICENSE for details.

from sportradar.api import API


class Formula1(API):
    """Formula 1 API Wrapper"""

    def __init__(self, api_key, access_level='trial', language='en', format_='json',
                 timeout=5, sleep_time=1.5):
        self.access_level = access_level
        self.version = 'v2'
        self.language = language
        self.sport = 'formula1'
        self.api_prefix = "{sport}/{access_level}/{version}/{language_code}".format(
            sport=self.sport, access_level=self.access_level,
            version=self.version, language_code=self.language)
        super().__init__(api_key, format_, timeout, sleep_time)

    def competitor_profile(self, competitor_id):
        """Obtain competitor profile for Formula 1.
        :param competitor_id: id of a given competitor
        """
        path = "{prefix}/competitors/{competitor_id}/profile".format(
            prefix=self.api_prefix, competitor_id=competitor_id)
        return self._make_request(path)

    def seasons(self):
        """Obtain full list of seasons for Formula 1."""
        path = "{prefix}/seasons".format(prefix=self.api_prefix)
        return self._make_request(path)

    def stage_probabilities(self, stage_id):
        """Obtain stage probabilities for Formula 1.
        :param stage_id: id of a given stage.
        """
        path = "{prefix}/sport_events/{stage_id}/probabilities".format(
            prefix=self.api_prefix, stage_id=stage_id)
        return self._make_request(path)

    def stage_summary(self, stage_id):
        """Obtain stage summary for Formula 1.
        :param stage_id: id of a given stage.
        """
        path = "{prefix}/sport_events/{stage_id}/summary".format(
            prefix=self.api_prefix, stage_id=stage_id)
        return self._make_request(path)
