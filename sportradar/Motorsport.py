# Sportradar APIs
# See LICENSE for details.

import logging

from sportradar.api import API


class Motorsport(API):

    def __init__(self, api_key, access_level='t', language='en', format_='json', timeout=5, sleep_time=1.5):
        self.access_level = access_level
        self.version = 3
        self.language = language
        self.sport = 'motorsport'
        self.api_prefix = "{sport}-{access_level}{version}/{language_code}".format(sport=self.sport, access_level = self.access_level, version = self.version))
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_competitor_profile(self, competitor_id):
        """Obtain competitor profile for Motorcycle.
        """
        path = "{prefix}/competitors/{competitor_id}/results".format(
            prefix=self.api_prefix, competitor_id = competitor_id)
        logging.info(path)
        return self._make_request(path)

    def get_competitor_profile(self, competitor_id):
        """Obtain competitor profile for Motorcycle.
        """
        path = "{prefix}/competitors/{competitor_id}/results".format(
            prefix=self.api_prefix, competitor_id = competitor_id)
        logging.info(path)
        return self._make_request(path)

    #def get_entry_list(self, nascar_series, race_id):
    #    """Obtain entry list information for NASCAR. NOTE: The 2012 sample data is an
    #        abbreviated season
    #    """
    #    path = "nascar-ot3/{nascar_series}/races/{race_id}/entry_list".format(
    #        nascar_series=nascar_series, race_id=race_id)
    #    print(path)
    #    return self._make_request(path)

    #def get_daily_change_log(self, year, month, day):
    #    """information on any changes made to race information, race results, driver
    #        information, track information, or standings
    #    """
    #    path = "nascar-ot3/{year:4d}/{month:02d}/{day:02d}/changes".format(
    #        year=year, month=month, day=day)
    #    print(path)
    #    return self._make_request(path)
