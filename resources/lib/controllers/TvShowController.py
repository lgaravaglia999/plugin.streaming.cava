from resources.lib.views.FPTtvShowView import FPTtvShowView
from resources.lib.helpers.filmpertutti.TvSeries import TvSeries
from resources.lib.models.tvShow import TvShow
from resources.lib import kodiutilsitem

def fpt_tvshow(title):
	tv_show = TvSeries()
	tvshows = tv_show.get_result_from_fpt(title)
	FPTtvShowView().show_tvshows_results(tvshows, 'tvshow/fpt_tv')

def fpt_seasons(tvshow_title, page_url):
	tv_series = TvSeries()
	tv_series.scrape(page_url)
	seasons = tv_series.get_all_seasons()
	FPTtvShowView().show_tv_seasons(tvshow_title, seasons, page_url)

def fpt_episodes(tvshow_title, page_url, season_no):
	int_season_no = int(season_no)
	tv_series = TvSeries()
	tv_series.scrape(page_url)
	episodes = tv_series.get_episodes_by_season_number(int_season_no)
	FPTtvShowView().show_season_episodes(tvshow_title, episodes)

def fpt_episodes_streaming_options(ep_title, *args):
	urls = [url for url in args]

	FPTtvShowView().show_playable_url(ep_title, urls)
