from resources.lib.views import MovieView
from resources.lib.models.filmpertutti.Movies import Movies
from resources.lib import kodiutilsitem

def fpt_movie(title):
	movie = Movies()
	posts = movie.get_result_from_fpt(title)
	if posts is None:
		fpt_exact_name(title)
	else:
		MovieView.show_fpt_results(posts, 'movies/fpt_movie')

def fpt_exact_name(keyword=None):
	movie = Movies()
	if keyword is None:
		keyword = kodiutilsitem.user_input()

	direct_url = movie.get_by_exact_name(keyword)
	movie_urls = movie.scrape_url(direct_url)
	movie_title = keyword

	MovieView.show_scraped_url(movie_title, movie_urls)

def movie_streaming_options(title, url):
	movie = Movies()
	movie_urls = movie.scrape_url(url)
	MovieView.show_scraped_url(title, movie_urls)

