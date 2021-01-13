# Sportradar APIs
# Copyright 2018 John W. Miller
# Copyright 2020 Serge Koudoro
# See LICENSE for details.

from sportradar.api import API


class Rugby(API):

    def __init__(self, api_key, format_='json', access_level='trial',
                 rugby_type='union', version=2, language='en',
                 timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)

        self.prefix = 'rugby/{level}/v{version}/{rugby_type}/{lang}/'.format(
            level=access_level, version=version, rugby_type=rugby_type,
            lang=language)

    def get_daily_live_summaries(self):
        """Provide all matches information/scoring played on a given day."""
        path = "schedules/live/summaries"
        return self._make_request(self.prefix + path)

    def get_daily_live_results(self):
        """Provide all matches information/scoring played on a given day."""
        path = "schedules/live/results"
        return self._make_request(self.prefix + path)

    def get_daily_results(self, year, month, day):
        """Provide all matches information/scoring played on a given day."""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/results".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_daily_schedule(self, year, month, day):
        """Provide the schedule for a given day."""
        path = "schedules/{year:4d}-{month:02d}-{day:02d}/schedule".format(
            year=year, month=month, day=day)
        return self._make_request(self.prefix + path)

    def get_match_lineups(self, match):
        """Provide match lineups and substitutions."""
        path = "matches/{match}/lineups".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_probabilities(self, match):
        """Provide pre-match probabilities."""
        path = "matches/{match}/probabilities".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_summary(self, match):
        """Provide basic match information and scoring."""
        path = "matches/{match}/summary".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_timeline(self, match):
        """Provide an events timeline for a match."""
        path = "matches/{match}/timeline".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_match_timeline_delta(self, match):
        """Will display the last 5 minutes of a live timeline element."""
        path = "matches/{match}/timeline/delta".format(
            match=match)
        return self._make_request(self.prefix + path)

    def get_player_profile(self, player):
        """Provide player information."""
        path = "players/{player}/profile".format(
            player=player)
        return self._make_request(self.prefix + path)

    def get_team_profile(self, team):
        """Provide information and stats for a team."""
        path = "teams/{team}/profile".format(
            team=team)
        return self._make_request(self.prefix + path)

    def get_team_results(self, team):
        """Provide the results of the last played matches for a team."""
        path = "teams/{team}/results".format(
            team=team)
        return self._make_request(self.prefix + path)

    def get_team_schedule(self, team):
        """Provide a list of scheduled matches for a given team."""
        path = "teams/{team}/schedule".format(
            team=team)
        return self._make_request(self.prefix + path)

    def get_team_vs_team(self, team, team2):
        """Compare past results and upcoming games given two team IDs."""
        path = "teams/{team}/versus/{team2}/matches".format(
            team=team, team2=team2)
        return self._make_request(self.prefix + path)

    def get_season_info(self, season):
        """Provide information pertaining to a given season."""
        path = "seasons/{season}/info".format(
            season=season)
        return self._make_request(self.prefix + path)

    def get_season_list(self):
        """Provide the season list."""
        path = "seasons"
        return self._make_request(self.prefix + path)

    def get_season_list_previous(self, season):
        """Provide previous season list or tournaments."""
        path = "seasons/{season}/previous_seasons".format(
            season=season)
        return self._make_request(self.prefix + path)

    def get_season_results(self, season):
        """Provide a list of results for a given season."""
        path = "seasons/{season}/results".format(
            season=season)
        return self._make_request(self.prefix + path)

    def get_season_schedule(self, season):
        """Provide a list of scheduled matches for a given season."""
        path = "seasons/{season}/schedule".format(
            season=season)
        return self._make_request(self.prefix + path)

    def get_season_standings(self, season):
        """Provide the standings for a season."""
        path = "seasons/{season}/standings".format(
            season=season)
        return self._make_request(self.prefix + path)

    def get_season_live_standings(self, season):
        """Provide the live standings for a season."""
        path = "seasons/{season}/live_standings".format(
            season=season)
        return self._make_request(self.prefix + path)

    def get_season_summaries(self, season):
        """Provide the summary for a season."""
        path = "seasons/{season}/summaries".format(
            season=season)
        return self._make_request(self.prefix + path)
