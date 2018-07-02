# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class eSportsLoL(API):

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_dailyresults(self, sport, language_code, year, month, day):
        """Provides the match scoring for all matches played on a given day"""
        path = "{sport}-t1/{language_code}/schedules/{year:4d}-{month:02d}-{day:02d}/results".format(
            sport=sport, language_code=language_code, year=year, month=month, day=day)
        return self._make_request(path)

    def get_dailyschedule(self, sport, language_code, year, month, day):
        """Provides the schedule for all matches played on a given day"""
        path = "{sport}-t1/{language_code}/schedules/{year:4d}-{month:02d}-{day:02d}/schedule".format(
            sport=sport, language_code=language_code, year=year, month=month, day=day)
        return self._make_request(path)

    def get_deletedmatches(self, sport, language_code):
        """Provides information for matches which have been removed from the sched
            ule
        """
        path = "{sport}-t1/{language_code}/schedules/deleted_matches".format(
            sport=sport, language_code=language_code)
        return self._make_request(path)

    def get_head_2_head(self, sport, language_code, team_id_1, team_id_2):
        """Provides team vs team match data"""
        path = "{sport}-t1/{language_code}/teams/{team_id_1}/versus/{team_id_2}/matches".format(
            sport=sport, language_code=language_code, team_id_1=team_id_1, team_id_2=team_id_2)
        return self._make_request(path)

    def get_matchlineups(self, sport, language_code, match_id):
        """Provides match lineup data for a given match"""
        path = "{sport}-t1/{language_code}/matches/{match_id}/lineups".format(
            sport=sport, language_code=language_code, match_id=match_id)
        return self._make_request(path)

    def get_matchprobabilities(self, sport, language_code, match_id):
        """Provides pre-match probabilities for a given match"""
        path = "{sport}-t1/{language_code}/matches/{match_id}/probabilities".format(
            sport=sport, language_code=language_code, match_id=match_id)
        return self._make_request(path)

    def get_matchsummary(self, sport, language_code, match_id):
        """Provides match summary data for a given match"""
        path = "{sport}-t1/{language_code}/matches/{match_id}/summary".format(
            sport=sport, language_code=language_code, match_id=match_id)
        return self._make_request(path)

    def get_playerprofile(self, sport, language_code, player_id):
        """Provides the Player profile information for a given player"""
        path = "{sport}-t1/{language_code}/players/{player_id}/profile".format(
            sport=sport, language_code=language_code, player_id=player_id)
        return self._make_request(path)

    def get_teamprofile(self, sport, language_code, team_id):
        """Provides the profile information for a given team"""
        path = "{sport}-t1/{language_code}/teams/{team_id}/profile".format(
            sport=sport, language_code=language_code, team_id=team_id)
        return self._make_request(path)

    def get_teamresults(self, sport, language_code, team_id):
        """Provides the results for a given team"""
        path = "{sport}-t1/{language_code}/teams/{team_id}/results".format(
            sport=sport, language_code=language_code, team_id=team_id)
        return self._make_request(path)

    def get_teamschedule(self, sport, language_code, team_id):
        """Provides the schedule for a given team"""
        path = "{sport}-t1/{language_code}/teams/{team_id}/schedule".format(
            sport=sport, language_code=language_code, team_id=team_id)
        return self._make_request(path)

    def get_tournamentinfo(self, sport, language_code, tournament_id):
        """Provides information for lol tournaments"""
        path = "{sport}-t1/{language_code}/tournaments/{tournament_id}/info".format(
            sport=sport, language_code=language_code, tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournamentlivesummary(self, sport, language_code):
        """Provides summary information for live LOL matches"""
        path = "{sport}-t1/{language_code}/schedules/live/summaries".format(
            sport=sport, language_code=language_code)
        return self._make_request(path)

    def get_tournamentresults(self, sport, language_code, tournament_id):
        """Provides information for lol tournaments"""
        path = "{sport}-t1/{language_code}/tournaments/{tournament_id}/results".format(
            sport=sport, language_code=language_code, tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournamentschedule(self, sport, language_code, tournament_id):
        """Provides information for lol tournaments"""
        path = "{sport}-t1/{language_code}/tournaments/{tournament_id}/schedule".format(
            sport=sport, language_code=language_code, tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournamentseasons(self, sport, language_code, tournament_id):
        """Provides information for LOL tournament seasons"""
        path = "{sport}-t1/{language_code}/tournaments/{tournament_id}/seasons".format(
            sport=sport, language_code=language_code, tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournamentstandings(self, sport, language_code, tournament_id):
        """Provides standing information for a given tournament"""
        path = "{sport}-t1/{language_code}/tournaments/{tournament_id}/standings".format(
            sport=sport, language_code=language_code, tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournamentsummary(self, sport, language_code, tournament_id):
        """Provides summary information for a given tournament"""
        path = "{sport}-t1/{language_code}/tournaments/{tournament_id}/summaries".format(
            sport=sport, language_code=language_code, tournament_id=tournament_id)
        return self._make_request(path)

    def get_tournaments(self, sport, language_code):
        """Provides information for lol tournaments"""
        path = "{sport}-t1/{language_code}/tournaments".format(
            sport=sport, language_code=language_code)
        return self._make_request(path)

