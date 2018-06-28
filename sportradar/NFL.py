# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class NFL(API):

    def __init__(self, api_key, format_='json', language='en', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, language, timeout, sleep_time)

    def get_daily_change_log(self, year, month, day):
        """Obtain changes made to previously closed events, team rosters, or player
            profiles for a given day.
        """
        path = "nfl-ot2/league/{year:4d}/{month:02d}/{day:02d}/changes".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_game_boxscore(self, game_id):
        """Obtain the scoring information for each team, including drive and play
            information for all scoring events.
        """
        path = "nfl-ot2/games/{game_id}/boxscore".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_game_roster(self, game_id):
        """Obtain the roster information for each teams, as well as player profile da
            ta.
        """
        path = "nfl-ot2/games/{game_id}/roste".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_game_statistics(self, game_id):
        """Obtain team and player level game statistics for each team."""
        path = "nfl-ot2/games/{game_id}/statistics".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_league_hierarchy(self):
        """Obtain the complete league hierarchy."""
        path = "nfl-ot2/league/hierarchy".format()
        print(path)
        return self._make_request(path)

    def get_play-by-play(self, game_id):
        """Obtain complete play-by-play narrative."""
        path = "nfl-ot2/games/{game_id}/pbp".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_player_participation(self, game_id):
        """Obtain player participation for a given game."""
        path = "nfl-ot2/plays/{game_id}/participation".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_player_profile(self, player_id):
        """Obtain complete player biographical information."""
        path = "nfl-ot2/players/{player_id}/profile".format(player_id=player_id)
        print(path)
        return self._make_request(path)

    def get_schedule(self, year, nfl_season):
        """Obtain complete schedule information."""
        path = "nfl-ot2/games/{year:4d}/{nfl_season}/schedule".format(
            year=year, nfl_season=nfl_season)
        print(path)
        return self._make_request(path)

    def get_seasonal_statistics(self, year, nfl_season, team_id):
        """Obtain complete team and player seasonal statistics."""
        path = "nfl-ot2/seasontd/{year:4d}/{nfl_season}/teams/{team_id}/statistics".format(
            year=year, nfl_season=nfl_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_standings(self, year):
        """Obtain standings information for each team."""
        path = "nfl-ot2/seasontd/{year:4d}/standings".format(year=year)
        print(path)
        return self._make_request(path)

    def get_team_profile(self, team_id):
        """Obtain franchise team information."""
        path = "nfl-ot2/teams/{team_id}/profile".format(team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_team_roster(self, team_id):
        """Obtain the complete roster of players for a given team"""
        path = "nfl-ot2/teams/{team_id}/full_roste".format(team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_weekly_schedule(self, year, nfl_season, nfl_season_week):
        """Obtain schedules for the NFL for a given week. Pre-Season (PRE) valid weeks
            1-4, Regular Season (REG) weeks 1-17, Post-Season (PST) weeks 1-4.
        """
        path = "nfl-ot2/games/{year:4d}/{nfl_season}/{nfl_season_week}/schedule".format(
            year=year, nfl_season=nfl_season, nfl_season_week=nfl_season_week)
        print(path)
        return self._make_request(path)

    def get_weekly_injuries(self, year, nfl_season, nfl_season_week):
        """Obtain injuries for the NFL for a given week. Pre-Season (PRE) valid weeks 1-4,
            Regular Season (REG) weeks 1-17, Post-Season (PST) weeks 1-4.
        """
        path = "nfl-ot2/seasontd/{year:4d}/{nfl_season}/{nfl_season_week}/injuries".format(
            year=year, nfl_season=nfl_season, nfl_season_week=nfl_season_week)
        print(path)
        return self._make_request(path)

    def get_weekly_depth_charts(self, year, nfl_season, nfl_season_week):
        """Obtain depth charts for the NFL for a given week. Pre-Season (PRE) valid weeks
            1-4, Regular Season (REG) weeks 1-17, Post-Season (PST) weeks 1-4.
        """
        path = "nfl-ot2/seasontd/{year:4d}/{nfl_season}/{nfl_season_week}/depth_charts".format(
            year=year, nfl_season=nfl_season, nfl_season_week=nfl_season_week)
        print(path)
        return self._make_request(path)

