from resources.lib.views.GuardaserieView import GuardaserieView
from resources.lib.helpers.guardaserie.guardaserie import GuardaSerie
from resources.lib.models.tvShow import TvShow
from resources.lib import kodiutilsitem

def gs_tvshow_list(title):
	gs_seasons(title)
	
def gs_seasons(title):
	gs = GuardaSerie()
	seasons = gs.get_search_result(title)
	GuardaserieView().show_tv_seasons(title, seasons)

def gs_episodes(tvshow_title, season_block, season_no):
	gs = GuardaSerie()
	episodes = gs.get_episodes(season_block)
	GuardaserieView().show_season_episodes(tvshow_title, episodes)

def gs_playable_url(ep_title, *args):
	urls = [url for url in args]

	GuardaserieView().show_playable_url(ep_title, urls)