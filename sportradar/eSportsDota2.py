# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class eSportsDota2(API):

    def __init__(self, api_key, access_level='t', language='en',
                 format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.access_level = access_level
        self.language = language
        self.version = 1
        self.prefix = 'dota2-{level}{ver}/{lang}/'.format(
                        level=self.access_level, ver=self.version, lang=self.language)

    def get_dailyresults(self, year, month, day):
        """Provides the match scoring for all matches played on a given day"""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/results".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_dailyschedule(self, year, month, day):
        """Provides the schedule for all matches played on a given day"""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/schedule".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_deletedmatches(self):
        """Provides information for matches which have been removed from the
            schedule
        """
        path = "schedules/deleted_matches".format()
        return self._make_request(self.prefix + path)

    def get_head_2_head(self, team_id_1, team_id_2):
        """Provides team vs team match data"""
        path = "teams/{team_id_1}/versus/{team_id_2}/matches".format(
            team_id_1=team_id_1, team_id_2=team_id_2)
        return self._make_request(self.prefix + path)

    def get_matchlineups(self, match_id):
        """Provides match lineup data for a given match"""
        path = "matches/{match_id}/lineups".format(
            match_id=match_id)
        return self._make_request(self.prefix + path)

    def get_matchprobabilities(self, match_id):
        """Provides pre-match probabilities for a given match"""
        path = "matches/{match_id}/probabilities".format(
            match_id=match_id)
        return self._make_request(self.prefix + path)

    def get_matchsummary(self, match_id):
        """Provides match summary data for a given match"""
        path = "matches/{match_id}/summary".format(
            match_id=match_id)
        return self._make_request(self.prefix + path)

    def get_playerprofile(self, player_id):
        """Provides the Player profile information for a given player"""
        path = "players/{player_id}/profile".format(
            player_id=player_id)
        return self._make_request(self.prefix + path)

    def get_teamprofile(self, team_id):
        """Provides the profile information for a given team"""
        path = "teams/{team_id}/profile".format(
            team_id=team_id)
        return self._make_request(self.prefix + path)

    def get_teamresults(self, team_id):
        """Provides the results for a given team"""
        path = "teams/{team_id}/results".format(
            team_id=team_id)
        return self._make_request(self.prefix + path)

    def get_teamschedule(self, team_id):
        """Provides the schedule for a given team"""
        path = "teams/{team_id}/schedule".format(
            team_id=team_id)
        return self._make_request(self.prefix + path)

    def get_tournamentinfo(self, tournament_id):
        """Provides information for dota2 tournaments"""
        path = "tournaments/{tournament_id}/info".format(
            tournament_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_tournamentlivesummary(self):
        """Provides summary information for live Dota2 matches"""
        path = "schedules/live/summaries".format()
        return self._make_request(self.prefix + path)

    def get_tournamentresults(self, tournament_id):
        """Provides information for dota2 tournaments"""
        path = "tournaments/{tournament_id}/results".format(
            tournament_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_tournamentschedule(self, tournament_id):
        """Provides information for dota2 tournaments"""
        path = "tournaments/{tournament_id}/schedule".format(
            tournament_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_tournamentseasons(self, tournament_id):
        """Provides information for Dota2 tournament seasons"""
        path = "tournaments/{tournament_id}/seasons".format(
            tournament_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_tournamentstandings(self, tournament_id):
        """Provides standing information for a given tournament"""
        path = "tournaments/{tournament_id}/standings".format(
            tournament_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_tournamentsummary(self, tournament_id):
        """Provides summary information for a given tournament"""
        path = "tournaments/{tournament_id}/summaries".format(
            tournament_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_tournaments(self):
        """Provides information for dota2 tournaments"""
        path = "tournaments".format()
        return self._make_request(self.prefix + path)

