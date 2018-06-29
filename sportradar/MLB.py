# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class MLB(API):

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

    def get_daily_boxscore(self, year, month, day):
        """Obtain Daily Boxscores for MLB for a given season. NOTE: The 2012 sample data
            is an abbreviated season.
        """
        path = "mlb/trial/v6.5/en/games/{year:4d}/{month:02d}/{day:02d}/boxscore".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_change_log(self, year, month, day):
        """Obtain changes made to previously closed events, team rosters, or player
            profiles for a given day.
        """
        path = "mlb/trial/v6.5/en/league/{year:4d}/{month:02d}/{day:02d}/changes".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_schedule(self, year, month, day):
        """Obtain Schedule for the MLB for a given day. NOTE: The 2012 sample data is an
            abbreviated season.
        """
        path = "mlb/trial/v6.5/en/games/{year:4d}/{month:02d}/{day:02d}/schedule".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_summary(self, year, month, day):
        """Obtain Daily Summary for the MLB for a given day. NOTE: The 2012 sample data is
            an abbreviated season.
        """
        path = "mlb/trial/v6.5/en/games/{year:4d}/{month:02d}/{day:02d}/summary".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_daily_transactions(self, year, month, day):
        """Obtain information concerning all transactions taking place on a given MLB
            defined day.
        """
        path = "mlb/trial/v6.5/en/league/{year:4d}/{month:02d}/{day:02d}/transactions".format(
            year=year, month=month, day=day)
        print(path)
        return self._make_request(path)

    def get_game_boxscore(self, event_id):
        """Obtain a boxscore for a specific MLB game."""
        path = "mlb/trial/v6.5/en/games/{event_id}/boxscore".format(event_id=event_id)
        print(path)
        return self._make_request(path)

    def get_game_pitch_metrics(self, event_id):
        """Obtain pitch metrics for a specific MLB game."""
        path = "mlb/trial/v6.5/en/games/{event_id}/pitch_metrics".format(
            event_id=event_id)
        print(path)
        return self._make_request(path)

    def get_game_summary(self, event_id):
        """Obtain a game summary for a specific MLB game."""
        path = "mlb/trial/v6.5/en/games/{event_id}/summary".format(event_id=event_id)
        print(path)
        return self._make_request(path)

    def get_glossary(self):
        """Obtain the pitch types, player statuses, pitch outcomes, runner outcomes, game
            status and postseason game IDs.
        """
        path = "mlb/trial/v6.5/en/league/glossary".format()
        print(path)
        return self._make_request(path)

    def get_injuries(self):
        """Obtain information concerning all current injuries across the league."""
        path = "mlb/trial/v6.5/en/league/injuries".format()
        print(path)
        return self._make_request(path)

    def get_league_depth_chart(self):
        """Obtain league depth charts for MLB."""
        path = "mlb/trial/v6.5/en/league/depth_charts".format()
        print(path)
        return self._make_request(path)

    def get_league_hierarchy(self):
        """Obtain list of MLB teams."""
        path = "mlb/trial/v6.5/en/league/hierarchy".format()
        print(path)
        return self._make_request(path)

    def get_league_leaders(self, year, mlb_season):
        """Obtain leaders for a given year."""
        path = "mlb/trial/v6.5/en/seasons/{year:4d}/{mlb_season}/leaders/statistics".format(
            year=year, mlb_season=mlb_season)
        print(path)
        return self._make_request(path)

    def get_league_schedule(self, year, mlb_season):
        """Obtain Schedule for the MLB for a given season. NOTE: The 2012 sample data is
            an abbreviated season.
        """
        path = "mlb/trial/v6.5/en/games/{year:4d}/{mlb_season}/schedule".format(
            year=year, mlb_season=mlb_season)
        print(path)
        return self._make_request(path)

    def get_play_by_play(self, event_id):
        """Obtain the play-by-play data for a specific MLB game."""
        path = "mlb/trial/v6.5/en/games/{event_id}/pbp".format(event_id=event_id)
        print(path)
        return self._make_request(path)

    def get_player_profile(self, player_id):
        """Obtain a profile for a given player."""
        path = "mlb/trial/v6.5/en/players/{player_id}/profile".format(
            player_id=player_id)
        print(path)
        return self._make_request(path)

    def get_rankings(self, year, mlb_season):
        """Obtain league and division rank for each team, including post season clinching
            status (available beginning with 2014 season)
        """
        path = "mlb/trial/v6.5/en/seasons/{year:4d}/{mlb_season}/rankings".format(
            year=year, mlb_season=mlb_season)
        print(path)
        return self._make_request(path)

    def get_seasonal_pitch_metrics(self, player_id):
        """Obtain pitch metrics for a specific season"""
        path = "mlb/trial/v6.5/en/players/{player_id}/pitch_metrics".format(
            player_id=player_id)
        print(path)
        return self._make_request(path)

    def get_seasonal_splits(self, year, mlb_season, team_id):
        """Obtain season splits for MLB -- Not available pre-2015"""
        path = "mlb/trial/v6.5/en/seasons/{year:4d}/{mlb_season}/teams/{team_id}/splits".format(
            year=year, mlb_season=mlb_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_seasonal_statistics(self, year, mlb_season, team_id):
        """Obtain season statistics for MLB"""
        path = "mlb/trial/v6.5/en/seasons/{year:4d}/{mlb_season}/teams/{team_id}/statistics".format(
            year=year, mlb_season=mlb_season, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_seasonal_transactions(self, year):
        """Obtain information concerning all transactions taking place during a given
            season.
        """
        path = "mlb/trial/v6.5/en/league/{year:4d}/transactions".format(year=year)
        print(path)
        return self._make_request(path)

    def get_series_schedule(self, year, mlb_season):
        """Obtain Series Schedule for the MLB for the postseason."""
        path = "mlb/trial/v6.5/en/series/{year:4d}/{mlb_season}/schedule".format(
            year=year, mlb_season=mlb_season)
        print(path)
        return self._make_request(path)

    def get_series_statistics(self, series_id, team_id):
        """Obtain series statistics for a given series. Please note that this feed will
            not return data until the 2017 playoffs begin
        """
        path = "mlb/trial/v6.5/en/series/{series_id}/teams/{team_id}/statistics".format(
            series_id=series_id, team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_series_summary(self, series_id):
        """Obtain series summary info for a given series. Please note that this feed will
            not return data until the 2017 playoffs begin
        """
        path = "mlb/trial/v6.5/en/series/{series_id}/summary".format(
            series_id=series_id)
        print(path)
        return self._make_request(path)

    def get_standings(self, year, mlb_season):
        """Obtain Standings for the MLB for a given season. Standing data is not valid for
            2012 as we do not have a full season available.
        """
        path = "mlb/trial/v6.5/en/seasons/{year:4d}/{mlb_season}/standings".format(
            year=year, mlb_season=mlb_season)
        print(path)
        return self._make_request(path)

    def get_team_depth_chart(self, team_id):
        """Obtain team depth chart information."""
        path = "mlb/trial/v6.5/en/teams/{team_id}/depth_chart".format(team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_team_profile(self, team_id):
        """Obtain team profile information."""
        path = "mlb/trial/v6.5/en/teams/{team_id}/profile".format(team_id=team_id)
        print(path)
        return self._make_request(path)

    def get_venues(self):
        """Obtain venue data for the current season."""
        path = "mlb/trial/v6.5/en/league/venues".format()
        print(path)
        return self._make_request(path)

