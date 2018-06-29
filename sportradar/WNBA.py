# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class WNBA(API):

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_daily_change_log(self, year, month, day):
        """information on any changes made to teams, players, game statistics, and
            standings
        """
        path = "wnba/trial/v4/en/league/{year:4d}/{month:02d}/{day:02d}/changes".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_schedule(self, year, month, day):
        """Get single day schedules for the WNBA."""
        path = "wnba/trial/v4/en/games/{year:4d}/{month:02d}/{day:02d}/schedule".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_transfers(self, year, month, day):
        """information for all transfers added or edited during the league defined day

        """
        path = "wnba/trial/v4/en/league/{year:4d}/{month:02d}/{day:02d}/transfers".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_game_boxscore(self, game_id):
        """Get boxscore data for WNBA games."""
        path = "wnba/trial/v4/en/games/{game_id}/boxscore".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_game_summary(self, game_id):
        """Obtain game summaries for the WNBA."""
        path = "wnba/trial/v4/en/games/{game_id}/summary".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_injuries(self):
        """Get injury feeds for the WNBA."""
        path = "wnba/trial/v4/en/league/injuries".format()
        print(path)
        return self._make_request(path)

    def get_league_hierarchy(self):
        """Get the league hierarchy information for the WNBA."""
        path = "wnba/trial/v4/en/league/hierarchy".format()
        print(path)
        return self._make_request(path)

    def get_league_leaders(self, season_id, wnba_season):
        """Get the league leaders for the WNBA."""
        path = "wnba/trial/v4/en/seasons/{season_id}/{wnba_season}/leaders".format(
            season_id=season_id, wnba_season=wnba_season)
        print(path)
        return self._make_request(path)

    def get_play_by_play(self, game_id):
        """Get play-by-play detail for WNBA games."""
        path = "wnba/trial/v4/en/games/{game_id}/pbp".format(game_id=game_id)
        print(path)
        return self._make_request(path)

    def get_player_profile(self, player_id):
        """Get player profiles for the WNBA."""
        path = "wnba/trial/v4/en/players/{player_id}/profile".format(
            player_id=player_id)
        print(path)
        return self._make_request(path)

    def get_rankings(self, season_id, wnba_season):
        """Get rankings information for the WNBA."""
        path = "wnba/trial/v4/en/seasons/{season_id}/{wnba_season}/rankings".format(
            season_id=season_id, wnba_season=wnba_season)
        print(path)
        return self._make_request(path)

    def get_schedule(self, season_id, wnba_season):
        """Get full season schedules for the WNBA."""
        path = "wnba/trial/v4/en/games/{season_id}/{wnba_season}/schedule".format(
            season_id=season_id, wnba_season=wnba_season)
        print(path)
        return self._make_request(path)

    def get_seasonal_statistics(self, season_id, wnba_season, team_id):
        """Get seasonal statistics information for the WNBA."""
        path = "wnba/trial/v4/en/seasons/{season_id}/{wnba_season}/teams/{team_id}/statistics".format(
            season_id=season_id, wnba_season=wnba_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_series_schedules(self, season_id, wnba_season):
        """Get post season series information for the WNBA."""
        path = "wnba/trial/v4/en/series/{season_id}/{wnba_season}/schedule".format(
            season_id=season_id, wnba_season=wnba_season)
        print(path)
        return self._make_request(path)

    def get_standings(self, season_id, wnba_season):
        """Get standings information for the WNBA."""
        path = "wnba/trial/v4/en/seasons/{season_id}/{wnba_season}/standings".format(
            season_id=season_id, wnba_season=wnba_season)
        print(path)
        return self._make_request(path)

    def get_team_profile_rosters(self, team_id):
        """Get team rosters for the WNBA."""
        path = "wnba/trial/v4/en/teams/{team_id}/profile".format(team_id=team_id)
        print(path)
        return self._make_request(path)

