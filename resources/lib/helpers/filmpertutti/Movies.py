import sys
import re
from os import path
from resources.lib import scraper_lib
from resources.lib.helpers.filmpertutti.FPTScraper import FPTScraper
from resources.lib.models.movie import Movie

class Movies(FPTScraper):

    def __init__(self, release_date=None):
        if sys.version_info[0] < 3:
            super(Movies, self).__init__(release_date)
        else:
            super().__init__(release_date)
        self.replacing_chars = ["\n", ";", " "]
        
    def get_result_from_fpt(self, keyword):
        return self.get_fpt_posts(keyword, "movie")
    
    def get_movie(self, title, fpt_movie_url):
        self.soup = scraper_lib.get_page_soup(fpt_movie_url)
        urls = self.__get_movies_url()
        
        movie = Movie(title, urls)
        return movie
        
    def __get_movies_url(self):
        movies_url = scraper_lib.get_hrefs(self.soup, self.streaming_to_scrape)
        return movies_url