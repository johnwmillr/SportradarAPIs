# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

from sportradar.api import API


class Handball(API):

    def __init__(self, api_key, format_='json', access_level='trial', version="v2",
                 league='INTL', language='en', timeout=5, sleep_time=1.5):
        super().__init__(api_key, format_, timeout, sleep_time)
        self.access_level = access_level
        self.language = language
        self.version = version
        self.league = league.lower()
        self.prefix = 'handball/{level}/{version}/{lang}/'.format(level=self.access_level,
                version=self.version,  lang=self.language)

    def get_competitions(self):
        """Provides list of all competitions scouted by Sportradar."""

        path = "competitions"

        return self._make_request(self.prefix + path)
    
    def get_seasons_for_competition(self, competition_id):
        """Provides list of all seasons in a given competition scouted by Sportradar."""
        
        path = "competitions/{_id}/seasons".format(_id=competition_id)

        return self._make_request(self.prefix + path)
    
    def get_players_for_season(self, season_id):
        """Provides list of all competitors in a given season."""
        path = "seasons/{_id}/players".format(_id=season_id)

        return self._make_request(self.prefix + path)
    
    def get_competitors_for_season(self, season_id):
        """Provides list of all competitors in a given season."""
        path = "seasons/{_id}/competitors".format(_id=season_id)

        return self._make_request(self.prefix + path)
    
    def get_season_summaries(self, season_id):
        """Provides list of all competitors in a given season."""
        path = "seasons/{_id}/summaries".format(_id=season_id)

        return self._make_request(self.prefix + path)
    
    def get_player_profile(self, player_id):
        """Provides player information"""
        path = "players/{_id}/profile".format(_id=player_id)
        return self._make_request(self.prefix + path)    


    def get_sport_event_timeline(self, match_id):
        """Provides list of all competitors in a given season."""
        path = "sport_events/{_id}/timeline".format(_id=match_id)

        return self._make_request(self.prefix + path)

    def get_daily_results(self, year, month, day):
        """Provides match information and scoring, for all matches
            played on a given day. The year, month, and day arguments
            must all be of type int.
        """
        path = "schedules/{y:4d}-{m:02d}-{d:02d}/summaries".format(
            y=year, m=month, d=day)
        return self._make_request(self.prefix + path)

    def get_live_results(self):
        """Provides results for live matches"""
        path = "schedules/live/summaries"
        return self._make_request(self.prefix + path)

    def get_match_summary(self, match_id):
        """Provides match summary, including team statistics and lineups"""
        path = "sport_events/{_id}/summary".format(_id=match_id)
        return self._make_request(self.prefix + path)

    def get_match_timeline(self, match_id):
        """Provides match information and scoring, including team
        statistics and a play-by-play
        """
        path = "sport_events/{_id}/timeline".format(_id=match_id)
        return self._make_request(self.prefix + path)


    def get_match_probabilities(self, match_id):
        """Provides match probabilities"""
        path = "sport_events/{_id}/sport_event_probabilities".format(_id=match_id)
        return self._make_request(self.prefix + path)





    
    def get_team_profile(self, team_id):
        """Team information, including player roster information"""
        path = "competitors/{_id}/profile".format(_id=team_id)
        return self._make_request(self.prefix + path)

    def get_team_statistics(self, tournament_id, team_id):
        """Team information, including player roster information"""
        path = "seasons/{tournament_id}/competitors/{team_id}/statistics".format(
            tournament_id=tournament_id, team_id=team_id)
        return self._make_request(self.prefix + path)

    def get_head2head(self, team_id_1, team_id_2):
        """Provides information on team versus team results"""
        path = "competitors/{_id_1}/versus/{_id_2}/summaries".format(
            _id_1=team_id_1, _id_2=team_id_2)
        return self._make_request(self.prefix + path)

    def get_tournaments(self):
        """Provides the list of International Handball tournaments"""
        path = "competitions"
        return self._make_request(self.prefix + path)

    def get_tournament_info(self, tournament_id):
        """Provides information for International Soccer tournaments"""
        path = "competitions/{_id}/info".format(_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_tournament_standings(self, tournament_id):
        """Provides the standings for International Soccer tournaments"""
        path = "seasons/{_id}/standings".format(_id=tournament_id)
        return self._make_request(self.prefix + path)

    def get_live_standings(self, tournament_id):
        """Provides the live standings for Soccer tournaments"""
        path = "schedules/{_id}/live/timelines".format(_id=tournament_id)
        return self._make_request(self.prefix + path)

