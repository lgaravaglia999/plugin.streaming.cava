from resources.lib.views.ItaliaserieOrgView import ItaliaserieOrgView
from resources.lib.helpers.italiaserie.italiaserieOrg import ItaliaSerie
from resources.lib import kodiutilsitem

def tvshow_list(title):
	scraper = ItaliaSerie()
	tvshows = scraper.get_search_result(title)
	ItaliaserieOrgView().show_tvshows_results(tvshows)

def seasons(title, page_url):
	scraper = ItaliaSerie()
	seasons = scraper.get_seasons(page_url)
	ItaliaserieOrgView().show_tv_seasons(title, seasons, page_url)

def episodes(tvshow_title, page_url, season_no):
	int_season_no = int(season_no)
	scraper = ItaliaSerie()
	episodes = scraper.get_episodes(page_url, season_no=int_season_no)
	ItaliaserieOrgView().show_season_episodes(tvshow_title, episodes)

def playable_url(ep_title, *args):
	urls = [url for url in args]

	ItaliaserieOrgView().show_playable_url(ep_title, urls)