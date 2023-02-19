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
