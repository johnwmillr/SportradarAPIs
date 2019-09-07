# Sportradar APIs
# Copyright 2018 John W. Miller
# Copyright 2019 Alexander Sutcliffe
# See LICENSE for details.

from sportradar.api import API


class Cricket(API):

    def __init__(self, api_key, format_='json', access_level='t', version=2,
                 language='en', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.access_level = access_level
        self.language = language
        self.version = version
        self.prefix = 'cricket-{level}{version}/{lang}/'.format(level=self.access_level,
                version=self.version, lang=self.language)

    def get_daily_results(self, year, month, day):
        """Provides match information and scoring, for all matches played on a given day"""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/results".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_daily_schedule(self, year, month, day):
        """Provides the schedule for a given day"""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/schedule".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_match_lineups(self, match):
        """Provides match lineups and substitutions"""
        path = "matches/{match}/lineups".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_probabilities(self, match):
        """Provides pre-match probabilities"""
        path = "matches/{match}/probabilities".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_summary(self, match):
        """Provides basic match information and scoring"""
        path = "matches/{match}/summary".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_timeline(self, match):
        """Provides an events timeline for a match"""
        path = "matches/{match}/timeline".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_timeline_delta(self, match):
        """Will display the last 5 minutes of a live timeline element"""
        path = "matches/{match}/timeline/delta".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_player_profile(self, player):
        """Provides player information"""
        path = "players/{player}/profile".format(
            player=player)
        return self._make_request(self.prefix + path)

    def get_team_profile(self, team):
        """Provides information and stats for a team"""
        path = "teams/{team}/profile".format(
            team=team)
        return self._make_request(self.prefix + path)

    def get_team_results(self, team):
        """The results of the last played matches for a team"""
        path = "teams/{team}/results".format(
            team=team)
        return self._make_request(self.prefix + path)

    def get_team_schedule(self, team):
        """Provides a list of scheduled matches for a given team"""
        path = "teams/{team}/schedule".format(
            team=team)
        return self._make_request(self.prefix + path)
    
    def get_team_vs_team(self, team, team2):
        """Compares past results and upcoming games given two team IDs"""
        path = "teams/{team}/versus/{team2}/matches".format(
            team=team, team2=team2)
        return self._make_request(self.prefix + path)

    def get_tour_list(self):
        """Provides the tour list"""
        path = "tours"
        return self._make_request(self.prefix + path)

    def get_tour_schedule(self, tour):
        """Provides the tour schedule"""
        path = "tours/{tour}/schedule".format(
            tour=tour)
        return self._make_request(self.prefix + path)

    def get_tournament_info(self, tournament):
        """Provides information pertaining to a given tournament/league/season"""
        path = "tournaments/{tournament}/info".format(
            tournament=tournament)
        return self._make_request(self.prefix + path)

    def get_tournament_leaders(self, tournament):
        """Provides information pertaining to a given tournament/league/season"""
        path = "tournaments/{tournament}/leaders".format(
            tournament=tournament)
        return self._make_request(self.prefix + path)

    def get_tournament_list(self):
        """Provides the tournament list"""
        path = "tournaments"
        return self._make_request(self.prefix + path)

    def get_tournament_results(self, tournament):
        """Provides a list of results for a given tournament/league/season"""
        path = "tournaments/{tournament}/results".format(
            tournament=tournament)
        return self._make_request(self.prefix + path)

    def get_tournament_schedule(self, tournament):
        """Provides a list of scheduled matches for a given tournament/league/season"""
        path = "tournaments/{tournament}/schedule".format(
            tournament=tournament)
        return self._make_request(self.prefix + path)

    def get_tournament_seasons(self, tournament):
        """Provides a list of seasons with respective IDs"""
        path = "tournaments/{tournament}/seasons".format(
            tournament=tournament)
        return self._make_request(self.prefix + path)

    def get_tournament_squads(self, tournament, team):
        """Provides a list of seasons with respective IDs"""
        path = "tournaments/{tournament}/teams/{team}/squads".format(
            tournament=tournament, team=team)
        return self._make_request(self.prefix + path)

    def get_tournament_standings(self, tournament):
        """Provides the standings for a team and tournament/season"""
        path = "tournaments/{tournament}/standings".format(
            tournament=tournament)
        return self._make_request(self.prefix + path)