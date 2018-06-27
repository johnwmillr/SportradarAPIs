# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class Darts(API):

    def __init__(self, api_key, format_='json', language='en', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, language, timeout, sleep_time)
        self.api_root = 'https://api.sportradar.us//darts-t1/' + self._LANGUAGE + '/'

    def get_competitor_profile(self, competitor_id):
        """Provides information for a given competitor"""
        path = "{competitor_id}/profile".format(competitor_id=competitor_id)
        return self._make_request(path)

    def get_competitor_results(self, competitor_id):
        """Provides past match results for a given competitor"""
        path = "{competitor_id}/results".format(competitor_id=competitor_id)
        return self._make_request(path)

    def get_competitor_schedule(self, competitor_id):
        """Provides the schedule for a given competitor"""
        path = "{competitor_id}/schedule".format(competitor_id=competitor_id)
        return self._make_request(path)

    def get_daily_results(self, year, month, day):
        """Provides the match scoring for all matches played on a given day"""
        path = "{year:4d}-{month:02d}-{day:02d}/results".format(
            year=year, month=month, day=day)
        return self._make_request(path)

    def get_daily_schedule(self, year, month, day):
        """Provides the schedule for all matches played on a given day"""
        path = "{year:4d}-{month:02d}-{day:02d}/schedule".format(
            year=year, month=month, day=day)
        return self._make_request(path)

    def get_head_to_head(self, competitor_id1, competitor_id2):
        """Provides team versus team data"""
        path = "competitors/{competitor_id1}/versus/{competitor_id2}/matches".format(
            competitor_id1=competitor_id1, competitor_id2=competitor_id2)
        return self._make_request(path)

    def get_live_schedule(self):
        """Provides a list of matches in progress"""
        path = "live/schedule".format()
        return self._make_request(path)

    def get_seasons(self, tournament_id):
        """Provides the seasons for a given Tournament"""
        path = "{tournament_id}/seasons".format(tournament_id=tournament_id)
        return self._make_request(path)

    def get_sport_event_probabilities(self, match_id):
        """Provides probabilities for a given match; prematch only"""
        path = "{match_id}/probabilities".format(match_id=match_id)
        return self._make_request(path)

    def get_sport_event_timeline(self, match_id):
        """Provides detailed information for a given match"""
        path = "{match_id}/timeline".format(match_id=match_id)
        return self._make_request(path)

    def get_tournament_info(self, tournament_id):
        """Provides a list of Competitors from a given Tournament"""
        path = "{tournament_id}/in".format(tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournament_list(self):
        """Provides a list of all tournaments"""
        path = "tournaments".format()
        return self._make_request(path)

    def get_tournament_live_standings(self, tournament_id):
        """Provides the live standings for a given Tournament"""
        path = "{tournament_id}/live_standings".format(tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournament_results(self, tournament_id):
        """Provides the results for a given tournament"""
        path = "{tournament_id}/results".format(tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournament_schedule(self, tournament_id):
        """Provides the schedule for a given Tournament"""
        path = "{tournament_id}/schedule".format(tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournament_standings(self, tournament_id):
        """Provides the standings for a given Tournament"""
        path = "{tournament_id}/standings".format(tournament_id=tournament_id)
        return self._make_request(path)
