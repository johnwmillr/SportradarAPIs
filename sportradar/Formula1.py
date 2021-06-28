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
        self.version = 1
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

    def seasons(self, competitor_id):
        """Obtain competitor results for Motorcycle.
        :param competitor_id: id of a given competitor.
        """
        path = "{prefix}/competitors/{competitor_id}/results".format(
            prefix=self.api_prefix, competitor_id=competitor_id)
        return self._make_request(path)

    def competitor_schedule(self, competitor_id):
        """Obtain competitor schedule for Motorcycle.
        :param competitor_id: id of a given competitor.
        """
        path = "{prefix}/competitors/{competitor_id}/schedule".format(
            prefix=self.api_prefix, competitor_id=competitor_id)
        return self._make_request(path)

    def daily_results(self, year, month, day):
        """Obtain daily results.
        :param year: year int. Must be greater or equal than 2014.
        :param month: month int. Must be between 1 and 12.
        :param day: day int.
        """
        path = "{prefix}/schedules/{year:4d}-{month:02d}-{day:02d}/results".format(
            prefix=self.api_prefix, year=year, month=month, day=day)
        return self._make_request(path)

    def daily_schedule(self, year, month, day):
        """Obtain daily schedule.
        :param year: year int. Must be greater or equal than 2014.
        :param month: month int. Must be between 1 and 12.
        :param day: day int.
        """
        path = "{prefix}/schedules/{year:4d}-{month:02d}-{day:02d}/schedule".format(
            prefix=self.api_prefix, year=year, month=month, day=day)
        return self._make_request(path)
