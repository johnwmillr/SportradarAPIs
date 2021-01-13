# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class NBA(API):

    def __init__(self, api_key, format_='json', language='en',
                 access_level='trial', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.access_level = access_level
        self.language = language
        self.version = 7
        self.prefix = 'nba/{level}/v{ver}/{lang}/'.format(
                        level=self.access_level, ver=self.version, lang=self.language)

    def get_daily_change_log(self, year, month, day):
        """Provides information on any changes made to teams, players, game statistics,
            and standings
        """
        path = "league/{year:4d}/{month:02d}/{day:02d}/changes".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_daily_schedule(self, year, month, day):
        """Provides the schedule for a given day"""
        path = "games/{year:4d}/{month:02d}/{day:02d}/schedule".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_daily_transfers(self, year, month, day):
        """Provides information on player transfers for a given day"""
        path = "league/{year:4d}/{month:02d}/{day:02d}/transfers".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_free_agents(self):
        """Get boxscore data for NBA Games"""
        path = "league/free_agents".format()
        return self._make_request(self.prefix + path)

    def get_game_boxscore(self, game_id):
        """Provide top-level team scores by quarter"""
        path = "games/{game_id}/boxscore".format(game_id=game_id)
        return self._make_request(self.prefix + path)

    def get_game_summary(self, game_id):
        """Provides top-level boxscore information, along with detailed game stats at the
            team and player levels
        """
        path = "games/{game_id}/summary".format(game_id=game_id)
        return self._make_request(self.prefix + path)

    def get_injuries(self):
        """Provides active player injuries for all teams within the league"""
        path = "league/injuries".format()
        return self._make_request(self.prefix + path)

    def get_league_hierarchy(self):
        """League, conference, division, and team identification"""
        path = "league/hierarchy".format()
        return self._make_request(self.prefix + path)

    def get_league_leaders(self, season_year, season_type):
        """Provides the league leaders"""
        path = "seasons/{season_year}/{season_type}/leaders".format(
            season_year=season_year, season_type=season_type)
        return self._make_request(self.prefix + path)

    def get_play_by_play(self, game_id):
        """Provides information on every team possession and game event."""
        path = "games/{game_id}/pbp".format(game_id=game_id)
        return self._make_request(self.prefix + path)

    def get_player_profile(self, player_id):
        """Provides detailed player information"""
        path = "players/{player_id}/profile".format(
            player_id=player_id)
        return self._make_request(self.prefix + path)

    def get_rankings(self, season_year, season_type):
        """Provides conference and division rank for each team"""
        path = "seasons/{season_year}/{season_type}/rankings".format(
            season_year=season_year, season_type=season_type)
        return self._make_request(self.prefix + path)

    def get_schedule(self, season_year, season_type):
        """Get the schedule for a given NBA Season"""
        path = "games/{season_year}/{season_type}/schedule".format(
            season_year=season_year, season_type=season_type)
        return self._make_request(self.prefix + path)

    def get_seasonal_statistics_season_to_date(self, season_year, season_type, team_id):
        """Provides detailed team and player statistics for the defined season"""
        path = "seasons/{season_year}/{season_type}/teams/{team_id}/statistics".format(
            season_year=season_year, season_type=season_type, team_id=team_id)
        return self._make_request(self.prefix + path)

    def get_series_schedule(self, season_year, season_type):
        """Provides playoff participant and scheduling information"""
        path = "series/{season_year}/{season_type}/schedule".format(
            season_year=season_year, season_type=season_type)
        return self._make_request(self.prefix + path)

    def get_series_statistics(self, series_id, team_id):
        """Provides detailed team and player statistics for the defined series"""
        path = "series/{series_id}/teams/{team_id}/statistics".format(
            series_id=series_id, team_id=team_id)
        return self._make_request(self.prefix + path)

    def get_standings(self, season_year, season_type):
        """Get the standings for the NBA"""
        path = "seasons/{season_year}/{season_type}/standings".format(
            season_year=season_year, season_type=season_type)
        return self._make_request(self.prefix + path)

    def get_team_profile_rosters(self, team_id):
        """Provides detailed team information including league affiliation information and
            player roster information.
        """
        path = "teams/{team_id}/profile".format(team_id=team_id)
        return self._make_request(self.prefix + path)

