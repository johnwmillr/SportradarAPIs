# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class Golf(API):

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_tournament_schedule(self, golf_tour, year):
        """Obtain the schedules for a given tour."""
        path = "golf-t2/schedule/{golf_tour}/{year:4d}/tournaments/schedule".format(
            golf_tour=golf_tour, year=year)
        print(path)
        return self._make_request(path)

    def get_player_profiles(self, golf_tour, year):
        """Obtain the profiles for a given year."""
        path = "golf-t2/profiles/{golf_tour}/{year:4d}/players/profiles".format(
            golf_tour=golf_tour, year=year)
        print(path)
        return self._make_request(path)

    def get_tournament_summary(self, golf_tour, year, tournament_id):
        """Obtain summary information for a given tournament."""
        path = "golf-t2/summary/{golf_tour}/{year:4d}/tournaments/{tournament_id}/summary".format(
            golf_tour=golf_tour, year=year, tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_tournament_leaderboard(self, golf_tour, year, tournament_id):
        """Obtain the leaderboard for a given tournament."""
        path = "golf-t2/leaderboard/{golf_tour}/{year:4d}/tournaments/{tournament_id}/leaderboard".format(
            golf_tour=golf_tour, year=year, tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_tournament_hole_statistics(self, golf_tour, year, tournament_id):
        """Obtain the hole statistics for a given tournament."""
        path = "golf-t2/hole_stats/{golf_tour}/{year:4d}/tournaments/{tournament_id}/hole-statistics".format(
            golf_tour=golf_tour, year=year, tournament_id=tournament_id)
        print(path)
        return self._make_request(path)

    def get_tee_times_per_round(self, golf_tour, year, tournament_id, round_number):
        """Obtain the tee times for a given round."""
        path = "golf-t2/teetimes/{golf_tour}/{year:4d}/tournaments/{tournament_id}/rounds/{round_number}/teetimes".format(
            golf_tour=golf_tour, year=year, tournament_id=tournament_id, round_number=round_number)
        print(path)
        return self._make_request(path)

    def get_scorecards_per_round(self, golf_tour, year, tournament_id, round_number):
        """Obtain the scores for a given round."""
        path = "golf-t2/scorecards/{golf_tour}/{year:4d}/tournaments/{tournament_id}/rounds/{round_number}/scores".format(
            golf_tour=golf_tour, year=year, tournament_id=tournament_id, round_number=round_number)
        print(path)
        return self._make_request(path)

    def get_player_statistics(self, golf_tour, year):
        """Obtain statistics for each golfer."""
        path = "golf-t2/seasontd/{golf_tour}/{year:4d}/players/statistics".format(
            golf_tour=golf_tour, year=year)
        print(path)
        return self._make_request(path)

    def get_daily_change_log(self, golf_tour, year, month, day):
        """Provides all changes related to player, tournaments, schedules, and s
            tatistics
        """
        path = "golf-t2/changelog/{golf_tour}/{year:4d}/{month:02d}/{day:02d}/changes".format(
            golf_tour=golf_tour, year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_official_world_golf_rankings(self, year):
        """Obtain the World Golf Rankings."""
        path = "golf-t2/players/wgr/{year:4d}/rankings".format(year=year)
        print(path)
        return self._make_request(path)

