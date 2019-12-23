from resources.lib.views import MovieView
from resources.lib.helpers.hdcloud.altadefinizione import Altadefinizione
from resources.lib.streaming_hosts.mixdrop import Mixdrop
from resources.lib.models.movie import Movie
from resources.lib import kodiutilsitem
from resources.lib import kodiplayer

def play_hd(title, iframe, player_name):
	altadefinizione = Altadefinizione()
	url = altadefinizione.get_playable_url(title, iframe, player_name)
	if "mixdrop" in url:
		mixdrop = Mixdrop(url)
		kodiplayer.play_video(mixdrop.get_final_url())
	else:
		kodiplayer.play_video_with_resolver(url)

def show_movies(title):
	movie_scraper = Altadefinizione()
	movies = movie_scraper.get_search_result(title)
	MovieView.show_fpt_results(movies, 'hdcloud/movies')

def movie_streaming_options(title, url):
	movie_scraper = Altadefinizione()
	iframe = movie_scraper.get_hdload_frame(title, url)
	movie = movie_scraper.get_players(title, iframe)
	MovieView.show_hdplayers(movie)
