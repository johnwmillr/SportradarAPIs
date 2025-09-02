# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class Motorsport(API):
    """Motorsport API"""

    def __init__(self, api_key, access_level='t', language='en', format_='json',
                 timeout=5, sleep_time=1.5):
        self.access_level = access_level
        self.version = 1
        self.language = language
        self.sport = 'motorsport'
        self.api_prefix = "{sport}-{access_level}{version}/{language_code}".format(
            sport=self.sport, access_level=self.access_level,
            version=self.version, language_code=self.language)
        super().__init__(api_key, format_, timeout, sleep_time)

    def competitor_profile(self, competitor_id):
        """Obtain competitor profile for Motorcycle.

        :param competitor_id: id of a given competitor
        """
        path = "{prefix}/competitors/{competitor_id}/profile".format(
            prefix=self.api_prefix, competitor_id=competitor_id)
        return self._make_request(path)

    def competitor_results(self, competitor_id):
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

    def head_to_head(self, competitor_id, competitor_id2):
        """Obtain comparisson between two Motorcycle competitors.

        :param competitor_id: id of a given competitor.
        :param competitor_id2: id of another given competitor.
        """
        path = "{prefix}/competitors/{competitor_id}/versus/{competitor_id2}/matches".format(
            prefix=self.api_prefix, competitor_id=competitor_id, competitor_id2=competitor_id2)
        return self._make_request(path)

    def seasons(self, tournament_or_season_id):
        """Obtain seasons of a given Motorcycle tournament."""
        path = "{prefix}/tournaments/{tournament_or_season_id}/seasons".format(
            prefix=self.api_prefix, tournament_or_season_id=tournament_or_season_id)
        return self._make_request(path)

    def sport_event_probabilities(self, match_id):
        """Obtain sport event probabilities for a given Motrcycle match.

        :param match_id: id of a given match.
        """
        path = "{prefix}/matches/{match_id}/probabilities".format(
            prefix=self.api_prefix, match_id=match_id)
        return self._make_request(path)

    def sport_event_timeline(self, match_id):
        """Obtain sport event timeline for a given Motrcycle match.

        :param match_id: id of a given match.
        """
        path = "{prefix}/sport_events/{match_id}/timeline".format(
            prefix=self.api_prefix, match_id=match_id)
        return self._make_request(path)

    def tournament_info(self, tournament_or_season_id):
        """Obtain information of a given Motorcycle Tournament.

        :param tournament_or_season_id: id of a given tournament or season.
        """
        path = "{prefix}/tournaments/{tournament_or_season_id}/info".format(
            prefix=self.api_prefix, tournament_or_season_id=tournament_or_season_id)
        return self._make_request(path)

    def tournament_list(self):
        """Obtain Motorcycle Tournament list.
        """
        path = "{prefix}/tournaments".format(prefix=self.api_prefix)
        return self._make_request(path)

    def tournament_live_standings(self, tournament_or_season_id):
        """Obtain live standings of a given Motorcycle Tournament.

        :param tournament_or_season_id: id of a given tournament or season.
        """
        path = "{prefix}/tournaments/{tournament_or_season_id}/live_standings".format(
            prefix=self.api_prefix, tournament_or_season_id=tournament_or_season_id)
        return self._make_request(path)

    def tournament_results(self, tournament_or_season_id):
        """Obtain results of a given Motorcycle Tournament.

        :param tournament_or_season_id: id of a given tournament or season.
        """
        path = "{prefix}/tournaments/{tournament_or_season_id}/results".format(
            prefix=self.api_prefix, tournament_or_season_id=tournament_or_season_id)
        return self._make_request(path)

    def tournament_schedule(self, tournament_or_season_id):
        """Obtain schedule of a given Motorcycle Tournament.

        :param tournament_or_season_id: id of a given tournament or season.
        """
        path = "{prefix}/tournaments/{tournament_or_season_id}/schedule".format(
            prefix=self.api_prefix, tournament_or_season_id=tournament_or_season_id)
        return self._make_request(path)

    def tournament_standings(self, tournament_or_season_id):
        """Obtain standings of a given Motorcycle Tournament.

        :param tournament_or_season_id: id of a given tournament or season.
        """
        path = "{prefix}/tournaments/{tournament_or_season_id}/standings".format(
            prefix=self.api_prefix, tournament_or_season_id=tournament_or_season_id)
        return self._make_request(path)
