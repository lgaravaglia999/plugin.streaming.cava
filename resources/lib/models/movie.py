import sys
from base import Base

class Movie(Base):
    def __init__(self, title, urls="", page_url=""):

        if sys.version_info[0] < 3:
            super(Movie, self).__init__(title)
        else:
            super().__init__(title)
        
        self._urls = urls
        self._page_urls = page_url
    
    @property
    def urls(self):
        return self._urls
    
    @urls.setter
    def urls(self, value):
        self._urls = value
    
    @property
    def page_url(self):
        return self._page_urls
    
    @page_url.setter
    def page_url(self, value):
        self._page_urls = value