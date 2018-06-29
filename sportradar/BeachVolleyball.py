# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class BeachVolleyball(API):

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_competitor_profile(self, competitor_id):
        """Provides information for a given competitor"""
        path = "volleyball-t1/beach/en/competitors/{competitor_id}/profile".format(
            competitor_id=competitor_id)
        print(path)
        return self._make_request(path)

    def get_competitor_results(self, competitor_id):
        """Provides past match results for a given competitor"""
        path = "volleyball-t1/beach/en/competitors/{competitor_id}/results".format(
            competitor_id=competitor_id)
        print(path)
        return self._make_request(path)

    def get_competitor_schedule(self, competitor_id):
        """Provides the schedule for a given competitor"""
        path = "volleyball-t1/beach/en/competitors/{competitor_id}/schedule".format(
            competitor_id=competitor_id)
        print(path)
        return self._make_request(path)

    def get_daily_results(self, year, month, day):
        """Provides the match scoring for all matches played on a given day"""
        path = "volleyball-t1/beach/en/schedules/{year:4d}-{month:02d}-{day:02d}/results".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_schedule(self, year, month, day):
        """Provides the schedule for all matches played on a given day"""
        path = "volleyball-t1/beach/en/schedules/{year:4d}-{month:02d}-{day:02d}/schedule".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_head_to_head(self, competitor_id1, competitor_id2):
        """Provides team versus team data"""
        path = "volleyball-t1/beach/en/competitors/{competitor_id1}/versus/{competitor_id2}/matches".format(
            competitor_id1=competitor_id1, competitor_id2=competitor_id2)
        print(path)
        return self._make_request(path)

    def get_live_schedule(self):
        """Provides a list of matches in progress"""
        path = "volleyball-t1/beach/en/schedules/live/schedule".format()
        print(path)
        return self._make_request(path)

    def get_sport_event_probabilities(self, match_id):
        """Provides probabilities for a given match; prematch only"""
        path = "volleyball-t1/beach/en/sport_events/{match_id}/probabilities".format(
            match_id=match_id)
        print(path)
        return self._make_request(path)

    def get_sport_event_timeline(self, match_id):
        """Provides detailed information for a given match"""
        path = "volleyball-t1/beach/en/sport_events/{match_id}/timeline".format(
            match_id=match_id)
        print(path)
        return self._make_request(path)

    def get_tournament_info(self, tournament_id):
        """Provides a list of Competitors from a given Tournament"""
        path = "volleyball-t1/beach/en/tournaments/{tournament_id}/in".format(
            tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_tournament_list(self):
        """Provides a list of all tournaments"""
        path = "volleyball-t1/beach/en/tournaments".format()
        print(path)
        return self._make_request(path)

    def get_live_standings(self, tournament_id):
        """Provides the live standings for a given Tournament"""
        path = "volleyball-t1/beach/en/tournaments/{tournament_id}/live_standings".format(
            tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_seasons(self, tournament_id):
        """Provides the seasons for a given Tournament"""
        path = "volleyball-t1/beach/en/tournaments/{tournament_id}/seasons".format(
            tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_tournament_results(self, tournament_id):
        """Provides the results for a given tournament"""
        path = "volleyball-t1/beach/en/tournaments/{tournament_id}/results".format(
            tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_tournament_schedule(self, tournament_id):
        """Provides the schedule for a given Tournament"""
        path = "volleyball-t1/beach/en/tournaments/{tournament_id}/schedule".format(
            tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_tournament_standings(self, tournament_id):
        """Provides the standings for a given Tournament"""
        path = "volleyball-t1/beach/en/tournaments/{tournament_id}/standings".format(
            tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

