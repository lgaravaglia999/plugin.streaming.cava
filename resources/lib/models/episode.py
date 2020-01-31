import sys
from base import Base

class Episode(Base):
    def __init__(self, title, urls, episode_no, season_no=None, html_block=None):

        if sys.version_info[0] < 3:
            super(Episode, self).__init__(title=title, html_block=html_block)
        else:
            super().__init__(title=title, html_block=html_block)

        self._urls = urls
        self._episode_no = episode_no
        self._season_no = season_no

    @property
    def urls(self):
        return self._urls

    @property  
    def episode_no(self):
        return self._episode_no
    
    @property
    def season_no(self):
        return self._season_no

    @urls.setter
    def urls(self, value):
        self._urls = value
        
    @episode_no.setter
    def episode_no(self, value):
        self._episode_no = value

    @season_no.setter
    def season_no(self, value):
        self._season_no = value