from resources.lib.views import TmdbView
from resources.lib.models.tmdb.MovieDb import MovieDb
from resources.lib import kodiutilsitem

tmdb = MovieDb()
TV_MEDIA_TYPE = 'tmdb_tvshow'
MOVIE_MEDIA_TYPE = 'tmdb_movie'
PEOPLE_MEDIA_TYPE = "menu/people/movies"

def people_by_keyword(page=1, keyword=None):
	if keyword is None:
		keyword = kodiutilsitem.user_input()
		if keyword is not None:
			results = tmdb.search_people(keyword, page)
	else:
		results = tmdb.search_people(keyword, page)

	TmdbView.show_moviedb_cast_results(results, PEOPLE_MEDIA_TYPE, 'menu/people/keyword', page, keyword)

def movie_by_keyword(page=1, keyword=None):
	if keyword is None:
		keyword = kodiutilsitem.user_input()
		if keyword is not None:
			results = tmdb.search_moviesdb(keyword, page)
	else:
		results = tmdb.search_moviesdb(keyword, page)

	TmdbView.show_moviedb_results(results, MOVIE_MEDIA_TYPE, 'menu/movies/keyword', page, keyword)

def movie_by_people(page=0, people_id=1):
	i_page = int(page)
	tmdb_type = 'menu/people/movies'
	results = tmdb.get_people_movies(int(people_id))
	
	"""
	pagination just to not render all movies images in a row
	"""
	max_results_per_page = 10
	n_pages = len(results) // max_results_per_page

	if i_page > n_pages:
		return

	start_index = max_results_per_page * i_page
	end_index = start_index + max_results_per_page
	if end_index > len(results):
		end_index = len(results)

	paginated_result = results[start_index: end_index]

	TmdbView.show_moviedb_results(paginated_result, MOVIE_MEDIA_TYPE, tmdb_type, page, people_id)

def most_popular_movies(page=1):
	tmdb_type = 'menu/movies/most_popular'
	results = tmdb.get_most_popular_movies(page)
	TmdbView.show_moviedb_results(results, MOVIE_MEDIA_TYPE, tmdb_type, page)

def most_voted_movies(page=1):
	tmdb_type = 'menu/movies/most_voted'
	results = tmdb.get_most_voted_movies(page)
	TmdbView.show_moviedb_results(results, MOVIE_MEDIA_TYPE, tmdb_type, page)

def now_playing_movies(page=1):
	tmdb_type = 'menu/movies/now_playing'
	results = tmdb.get_now_playing_movies(page)
	TmdbView.show_moviedb_results(results, MOVIE_MEDIA_TYPE, tmdb_type, page)

def tvshow_by_keyword(page=1, keyword=None):
	if keyword is None:
		keyword = kodiutilsitem.user_input()
		if keyword is not None:
			results = tmdb.search_tvseries(keyword, page)
	else:
		results = tmdb.search_tvseries(keyword, page)

	TmdbView.show_moviedb_results(results, TV_MEDIA_TYPE, 'menu/tvshow/keyword', page, keyword)

def most_popular_tvshow(page=1):
	tmdb_type = 'menu/tvshow/most_popular'
	results = tmdb.get_most_popular_tvseries(page)
	TmdbView.show_moviedb_results(results, TV_MEDIA_TYPE, tmdb_type, page)

def most_voted_tvshow(page=1):
	tmdb_type = 'menu/tvshow/most_voted'
	results = tmdb.get_most_voted_tvseries(page)
	TmdbView.show_moviedb_results(results, TV_MEDIA_TYPE, tmdb_type, page)

def on_air_tvshow(page=1):
	tmdb_type = 'menu/tvshow/on_air'
	results = tmdb.get_on_air_tvseries(page)
	TmdbView.show_moviedb_results(results, TV_MEDIA_TYPE, tmdb_type, page)
