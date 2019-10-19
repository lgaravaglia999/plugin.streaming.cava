from resources.lib.views import MovieView
from resources.lib.helpers.filmpertutti.Movies import Movies
from resources.lib.models.movie import Movie
from resources.lib import kodiutilsitem

def fpt_movie(title):
	movie_scraper = Movies()
	movies = movie_scraper.get_result_from_fpt(title)
	if movies is None:
		fpt_exact_name(title)
	else:
		MovieView.show_fpt_results(movies, 'movies/fpt_movie')

def fpt_exact_name(keyword=None):
	movie_scraper = Movies()
	if keyword is None:
		keyword = kodiutilsitem.user_input()

	direct_url = movie_scraper.get_by_exact_name(keyword)
	movie = movie_scraper.get_movie(keyword, direct_url)

	MovieView.show_scraped_url(movie)

def movie_streaming_options(title, url):
	movie_scraper = Movies()
	movie = movie_scraper.get_movie(title, url)
	MovieView.show_scraped_url(movie)

