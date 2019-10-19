import sys
from base import Base

class TvShow(Base):
    def __init__(self, title, page_url=None):

        if sys.version_info[0] < 3:
            super(TvShow, self).__init__(title)
        else:
            super().__init__(title)

        self._page_url = page_url
    
    @property
    def page_url(self):
        return self._page_url
    
    @page_url.setter
    def page_url(self, value):
        self._page_url = value