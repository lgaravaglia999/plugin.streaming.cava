from resources.lib.views import MovieView
from resources.lib.helpers.hdcloud.altadefinizione import Altadefinizione
from resources.lib.models.movie import Movie
from resources.lib import kodiutilsitem

def show_movies(title):
	movie_scraper = Altadefinizione()
	movies = movie_scraper.get_search_result(title)
	MovieView.show_fpt_results(movies, 'hdcloud/movies')

def movie_streaming_options(title, url):
	movie_scraper = Altadefinizione()
	movie = movie_scraper.get_movie(title, url)
	MovieView.show_scraped_url(movie)
