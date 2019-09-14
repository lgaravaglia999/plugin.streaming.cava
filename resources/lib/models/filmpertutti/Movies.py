import sys
import re
from os import path
from resources.lib import scraper_lib
from resources.lib.models.filmpertutti.FPTScraper import FPTScraper

class Movies(FPTScraper):

    def __init__(self, release_date=None):
        if sys.version_info[0] < 3:
            super(Movies, self).__init__(release_date)
        else:
            super().__init__(release_date)
        self.replacing_chars = ["\n", ";", " "]
        
    def get_result_from_fpt(self, keyword):
        return self.get_fpt_posts(keyword)
    
    def scrape_url(self, fpt_movie_url):
        self.soup = scraper_lib.get_page_soup(fpt_movie_url)
        return self.__get_movies_url()
        
    def __get_movies_url(self):
        movies_url = scraper_lib.get_hrefs(self.soup, self.streaming_to_scrape)
        return movies_url

if __name__ == "__main__":
    movie = Movies()
    direct_url = movie.get_by_exact_name('it 2017')
    movie_urls = movie.scrape_url(direct_url)
    print(movie_urls)
    # res = movie.get_result_from_fpt('alita')
    # url = res[1]["url"]

    # movie_urls = movie.scrape_url(url)
    # print(movie_urls)