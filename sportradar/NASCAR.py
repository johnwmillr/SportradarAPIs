# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class NASCAR(API):

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_drivers(self, nascar_series, year):
        """Obtain driver information for NASCAR. NOTE: The 2012 sample data is an
            abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/{year:4d}/drivers/list".format(
            nascar_series=nascar_series, year=year)
        print(path)
        return self._make_request(path)

    def get_tracks(self):
        """Obtain track information for NASCAR. NOTE: The 2012 sample data is an
            abbreviated season
        """
        path = "nascar-ot3/tracks/list".format()
        print(path)
        return self._make_request(path)

    def get_schedule(self, nascar_series, year):
        """Obtain schedule for NASCAR. NOTE: The 2012 sample data is an abbreviated
            season
        """
        path = "nascar-ot3/{nascar_series}/{year:4d}/races/schedule".format(
            nascar_series=nascar_series, year=year)
        print(path)
        return self._make_request(path)

    def get_entry_list(self, nascar_series, race_id):
        """Obtain entry list information for NASCAR. NOTE: The 2012 sample data is an
            abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/races/{race_id}/entry_list".format(
            nascar_series=nascar_series, race_id=race_id)
        print(path)
        return self._make_request(path)

    def get_practice_leaderboard(self, nascar_series, race_id):
        """Obtain practice leaderboard information for NASCAR. NOTE: The 2012 sample data
            is an abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/races/{race_id}/practices".format(
            nascar_series=nascar_series, race_id=race_id)
        print(path)
        return self._make_request(path)

    def get_qualifying_leaderboard(self, nascar_series, race_id):
        """Obtain qualifying leaderboard information for NASCAR. NOTE: The 2012 sample
            data is an abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/races/{race_id}/qualifying".format(
            nascar_series=nascar_series, race_id=race_id)
        print(path)
        return self._make_request(path)

    def get_starting_grid(self, nascar_series, race_id):
        """Obtain starting grid information for NASCAR. NOTE: The 2012 sample data is an
            abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/races/{race_id}/starting_grid".format(
            nascar_series=nascar_series, race_id=race_id)
        print(path)
        return self._make_request(path)

    def get_race_leaderboard(self, nascar_series, race_id):
        """Obtain race leaderboard information for NASCAR. NOTE: The 2012 sample data is
            an abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/races/{race_id}/results".format(
            nascar_series=nascar_series, race_id=race_id)
        print(path)
        return self._make_request(path)

    def get_driver_rookie_owner_and_manufacturer_standings(self, nascar_series, year, standings_type):
        """Obtain standings for drivers, rookies, owners, and manufacturers. NOTE: The
            2012 sample data is an abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/{year:4d}/standings/{standings_type}".format(
            nascar_series=nascar_series, year=year, standings_type=standings_type)
        print(path)
        return self._make_request(path)

    def get_driver_statistics(self, nascar_series, year):
        """Obtain driver statistics for NASCAR. NOTE: The 2012 sample data is an
            abbreviated season
        """
        path = "nascar-ot3/{nascar_series}/drivers/{year:4d}/drivers".format(
            nascar_series=nascar_series, year=year)
        print(path)
        return self._make_request(path)

    def get_daily_change_log(self, year, month, day):
        """information on any changes made to race information, race results, driver
            information, track information, or standings
        """
        path = "nascar-ot3/{year:4d}/{month:02d}/{day:02d}/changes".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

