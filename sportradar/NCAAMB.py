# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class NCAAMB(API):

    def __init__(self, api_key, format_='json', language='en',
                 access_level='trial', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.access_level = access_level
        self.language = language
        self.version = 7
        self.prefix = f'ncaamb/{self.access_level}/v{self.version}/{self.language}/'

    def get_daily_change_log(self, year, month, day):
        """provides information on any changes made to teams, players, game statistics
            and standings
        """
        return self._make_request(f'{self.prefix}league/{year:4d}/{month:02d}/{day:02d}/changes')

    def get_daily_schedule(self, year, month, day):
        """Provides the schedule for a given day"""
        return self._make_request(f'{self.prefix}games/{year:4d}/{month:02d}/{day:02d}/schedule')

    def get_game_boxscore(self, game_id):
        """Provide top-level team scores by quarter"""
        return self._make_request(f'{self.prefix}games/{game_id}/boxscore')

    def get_game_summary(self, game_id):
        """Provides top-level boxscore information, along with detailed game stats at the
            team and player levels
        """
        return self._make_request(f'{self.prefix}games/{game_id}/summary')

    def get_league_hierarchy(self):
        """get rankings for the entire league"""
        return self._make_request(f'{self.prefix}league/hierarchy')

    def get_league_leaders(self, year, season_type, conference_id):
        """get the leaders for a league"""
        return self._make_request(f'{self.prefix}seasons/{year}/{season_type}/{conference_id}/leaders')

    def get_play_by_play(self, game_id):
        """Provides information on every team possession and game event."""
        return self._make_request(f'{self.prefix}games/{game_id}/pbp')

    def get_player_profile(self, player_id):
        """Provides detailed player information"""
        return self._make_request(f'{self.prefix}players/{player_id}/profile')

    def get_rankings(self, season_type, season):
        """provides rankings for each team"""
        return self._make_request(f'{self.prefix}polls/{season_type}/{season}/rankings')

    def get_rankings_by_week(self, season_type, season, week):
        """provides ranking for each team in the given week"""
        return self._make_request(f'{self.prefix}polls/{season_type}/{season}/{week}/rankings')

    def get_rankings_by_rpi(self, season):
        """provides rankings for each team by RPI"""
        return self._make_request(f'{self.prefix}rpi/{season}/rankings')

    def get_schedule(self, season_year, season_type):
        """Get the schedule for a given NBA Season"""
        return self._make_request(f'{self.prefix}games/{season_year}/{season_type}/schedule')

    def get_seasonal_statistics(self, season_year, season_type, team_id):
        """Provides detailed team and player statistics for the defined season"""
        return self._make_request(f'seasons/{season_year}/{season_type}/teams/{team_id}/statistics')

    def get_seasons(self):
        """get seasons"""
        return self._make_request(f'{self.prefix}league/seasons')

    def get_standings(self, season_year, season_type):
        """Get the standings for the NCAAMB"""
        return self._make_request(f"{self.prefix}seasons/{season_year}/{season_type}/standings")

    def get_team_profile(self, team_id):
        """Provides detailed team information including league affiliation information and
            player roster information.
        """
        return self._make_request(f'{self.prefix}teams/{team_id}/profile')

    def get_tournament_list(self, season_id, ncaamb_season):
        """get a list of tournaments for the given season"""
        return self._make_request(f'{self.prefix}/tournaments/{season_id}/{ncaamb_season}')

    def get_tournament_schedule(self, tournament_id):
        """get the schedule for a tournament"""
        return self._make_request(f'{self.prefix}/tournaments/{tournament_id}/schedule')

    def get_tournament_statistics(self, tournament_id, team_id):
        """get the statistics with respect to a certain team for a tournament game"""
        return self._make_request(f'{self.prefix}/tournaments/{tournament_id}/teams/{team_id}/statistics')

    def get_seeded_tournament_summary(self, tournament_id):
        """get a summary about a tournament, must be seeded"""
        return self._make_request(f'{self.prefix}/tournaments/{tournament_id}/summary')
