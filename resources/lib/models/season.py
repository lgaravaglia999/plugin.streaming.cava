import sys
from base import Base

class Season(Base):
    def __init__(self, title, season_no,  tv_title="", episodes_number=None, html_block=""):

        if sys.version_info[0] < 3:
            super(Season, self).__init__(title=title)
        else:
            super().__init__(title=title)

        self._tv_title = tv_title
        self._season_no = season_no
        self._episodes_number = episodes_number
        self.html_block = html_block

    @property  
    def tv_title(self):
        return self._tv_title
    
    @property
    def season_no(self):
        return self._season_no

    @property
    def episodes_number(self):
        return self._episodes_number

    @tv_title.setter
    def tv_title(self, value):
        self._tv_title = value

    @season_no.setter
    def season_no(self, value):
        self._season_no = value

    @episodes_number.setter
    def episodes_number(self, value):
        self._episodes_number = value
