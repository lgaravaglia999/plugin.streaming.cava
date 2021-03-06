from resources.lib.views.HDMovieView import HDMovieView
from resources.lib.views.HDSerieView import HDSerieView
from resources.lib.helpers.hdcloud.altadefinizione import Altadefinizione
from resources.lib.helpers.hdcloud.seriehd import SerieHD
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
	HDMovieView().show_fpt_results(movies)

def movie_streaming_options(title, url):
	movie_scraper = Altadefinizione()
	iframe = movie_scraper.get_hdload_frame(title, url)
	movie = movie_scraper.get_players(title, iframe)
	HDMovieView().show_hdplayers(movie)

def tvshow(title):
	tv_show = SerieHD()
	tvshows = tv_show.get_search_result(title)
	HDSerieView().show_tvshows_results(tvshows)

def tvshow_seasons(tvshow_title, page_url):
	tv_series = SerieHD()
	seasons = tv_series.get_seasons(page_url)
	HDSerieView().show_tv_seasons(tvshow_title, seasons)

def tvshow_episodes(title, episodes_url):
	tv_series = SerieHD()
	episodes = tv_series.get_episodes(episodes_url)
	HDSerieView().show_season_episodes(title, episodes)

def tvshow_streaming_options(ep_title, url):
	serie_hd = SerieHD()
	movie = serie_hd.get_players(ep_title, url)
	HDSerieView().show_hdplayers(movie)