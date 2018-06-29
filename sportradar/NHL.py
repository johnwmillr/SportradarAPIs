# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class NHL(API):

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_daily_change_log(self, year, month, day):
        """provides information on any changes made to teams, players, game statistics,
            and standings
        """
        path = "nhl/trial/v5/en/league/{year:4d}/{month:02d}/{day:02d}/changes".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_schedule(self, year, month, day):
        """provides the schedule for a given day"""
        path = "nhl/trial/v5/en/games/{year:4d}/{month:02d}/{day:02d}/schedule".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_transfers(self, year, month, day):
        """provides information on player transfers for a given day"""
        path = "nhl/trial/v5/en/league/{year:4d}/{month:02d}/{day:02d}/transfers".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_game_boxscore(self, game_id):
        """Get boxscore data for NHL Games"""
        path = "nhl/trial/v5/en/games/{game_id}/boxscore".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_game_faceoffs(self, game_id):
        """Get faceoff data for an NHL Game"""
        path = "nhl/trial/v5/en/games/{game_id}/faceoffs".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_game_play_by_play(self, game_id):
        """Get the Play-by-Play data for an NHL Game"""
        path = "nhl/trial/v5/en/games/{game_id}/pbp".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_game_summary(self, game_id):
        """Get the Summary data for an NHL Game"""
        path = "nhl/trial/v5/en/games/{game_id}/summary".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_game_time_on_ice(self, game_id):
        """Get the time on ice data for an NHL Game"""
        path = "nhl/trial/v5/en/games/{game_id}/time_on_ice".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_injuries(self):
        """Provides updated injuries for the NHL"""
        path = "nhl/trial/v5/en/league/injuries".format()
        print(path)
        return self._make_request(path)

    def get_league_hierarchy(self):
        """Provides list of all NHL teams"""
        path = "nhl/trial/v5/en/league/hierarchy".format()
        print(path)
        return self._make_request(path)

    def get_league_leaders___goaltending(self, season, nhl_season):
        """Provides the leaders for Goaltending"""
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/leaders/goaltending".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_league_leaders___skaters(self, season, nhl_season):
        """Provides the leaders for Defense and Offense skaters"""
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/leaders/offense".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_league_leaders___daily(self, year1, nhl_season, year2, month, day):
        """Provides the leaders for a given day. Please note that this feed will not
            return data until the regular season begins
        """
        path = "nhl/trial/v5/en/seasons/{year1}/{nhl_season}/{year2}/{month:02d}/{day:02d}/leaders".format(
            year1=year1, nhl_season=nhl_season, year2=year2, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_league_leaders___seasonal(self, season, nhl_season):
        """Provides the seasonal leaders. Please note that this feed will not return data
            until the regular season begins
        """
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/leaders".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_player_profile(self, player_id):
        """Player information for the NHL"""
        path = "nhl/trial/v5/en/players/{player_id}/profile".format(
            player_id=player_id)
        print(path)
        return self._make_request(path)

    def get_rankings(self, season, nhl_season):
        """Get ranking information for the NHL"""
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/rankings".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_schedule(self, season, nhl_season):
        """Get the schedule for a given NHL Season"""
        path = "nhl/trial/v5/en/games/{season}/{nhl_season}/schedule".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_seasonal_faceoffs(self, season, nhl_season, team_id):
        """Get faceoff information on a team level"""
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/teams/{team_id}/faceoffs".format(
            season=season, nhl_season=nhl_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_seasonal_statistics___season_to_date(self, season, nhl_season, team_id):
        """Get statistics on a team level"""
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/teams/{team_id}/statistics".format(
            season=season, nhl_season=nhl_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_series_faceoffs(self, series_id, team_id):
        """Get faceoff information for a playoff series"""
        path = "nhl/trial/v5/en/series/{series_id}/teams/{team_id}/faceoffs".format(
            series_id=series_id, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_series_schedule(self, season, nhl_season):
        """Get faceoff information for a playoff series"""
        path = "nhl/trial/v5/en/series/{season}/{nhl_season}/schedule".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_series_statistics(self, series_id, team_id):
        """Get the statistics for a playoff series"""
        path = "nhl/trial/v5/en/series/{series_id}/teams/{team_id}/statistics".format(
            series_id=series_id, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_standings(self, season, nhl_season):
        """Get the standings for the NHL"""
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/standings".format(
            season=season, nhl_season=nhl_season)
        print(path)
        return self._make_request(path)

    def get_team_leaders___daily(self, year1, nhl_season, year2, month, day, team_id):
        """Provides the leaders for a given day. Please note that this feed will not
            return data until the regular season begins
        """
        path = "nhl/trial/v5/en/seasons/{year1}/{nhl_season}/{year2}/{month:02d}/{day:02d}/teams/{team_id}/leaders".format(
            year1=year1, nhl_season=nhl_season, year2=year2, month=month, day=day, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_team_leaders___seasonal(self, season, nhl_season, team_id):
        """Get leaders on a team level. Please note that this feed will not return data
            until the regular season begins
        """
        path = "nhl/trial/v5/en/seasons/{season}/{nhl_season}/teams/{team_id}/leaders".format(
            season=season, nhl_season=nhl_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_team_profile___roster(self, team_id):
        """Get the roster information for a NHL team"""
        path = "nhl/trial/v5/en/teams/{team_id}/profile".format(team_id=team_id)
        print(path)
        return self._make_request(path)

