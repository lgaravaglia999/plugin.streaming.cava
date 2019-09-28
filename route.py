import os
import importlib
import sys
import urlparse
import xbmc
from resources.lib.controllers import TmdbController, MovieController, MainController, TvShowController
from resources.lib import kodiutilsitem 

def route(urls, mode, kwargs):
	"""
    Handle the routing process.

    :param urls: list of dictionaries with all mapped urls {mode: function_to_call}
    :param mode: str representing the url of clicked item
	:param kwargs: arguments to pass on the function_to_call
    """

	xbmc.log("#######################################################", xbmc.LOGNOTICE)
	if mode is None:
		create_menu()
	else:
		xbmc.log("Clicked : [" + ''.join(mode) + "] item", xbmc.LOGNOTICE)
		for url_dict in urls:
			if mode in url_dict:
				xbmc.log("Parameters: " + ' ,'.join(a for a in kwargs), xbmc.LOGNOTICE)
				xbmc.log("Going to: [" + ''.join(url_dict[mode].__name__) + "] Controller", xbmc.LOGNOTICE)
				url_dict[mode](*kwargs)

	xbmc.log("#######################################################", xbmc.LOGNOTICE)


def create_menu():
	kodiutilsitem.add_menu_item({'mode' : 'menu/genres/list'}, 'Generi')
	kodiutilsitem.add_menu_item({'mode' : 'menu/people/keyword'}, 'Attori/Cast')
	kodiutilsitem.add_menu_item({'mode' : 'menu/fpt/keyword'}, 'Titolo esatto')
	kodiutilsitem.add_menu_item({'mode': ''}, "-"*100),
	kodiutilsitem.add_menu_item({'mode' : 'menu/movies/keyword'}, 'Cerca Film')
	kodiutilsitem.add_menu_item({'mode' : 'menu/movies/most_popular'}, 'Guarda i film piu popolari')
	kodiutilsitem.add_menu_item({'mode' : 'menu/movies/most_voted'}, 'Guarda i film piu votati')
	kodiutilsitem.add_menu_item({'mode' : 'menu/movies/now_playing'}, 'Guarda i film in onda al cinema')
	kodiutilsitem.add_menu_item({'mode': ''}, "-"*100),
	kodiutilsitem.add_menu_item({'mode' : 'menu/tvshow/keyword'}, 'Cerca Serie Tv')
	kodiutilsitem.add_menu_item({'mode' : 'menu/tvshow/most_popular'}, 'Guarda le Serie Tv piu popolari')
	kodiutilsitem.add_menu_item({'mode' : 'menu/tvshow/most_voted'}, 'Guarda le Serie Tv piu votate')
	kodiutilsitem.add_menu_item({'mode' : 'menu/tvshow/on_air'}, 'Guarda le Serie Tv ancora in corso')

	kodiutilsitem.end_directory()

def get_all_module_routers():
	"""
	Get all mapped url list from all _router.py files into the router_urls folder.
	"""

	c_path = os.path.dirname(os.path.abspath(__file__)) + '/resources/lib/router_urls'
	router_urls = []
	for p_file in os.listdir(c_path):
		if p_file.endswith("_router.py"):
			router_name = 'resources.lib.router_urls.' + p_file.split('.')[0]
			router_urls.extend(importlib.import_module(router_name).URLS)

	xbmc.log(', '.join(str(url) for url in router_urls), xbmc.LOGNOTICE)
	return router_urls


if __name__ == '__main__':
	base_url = sys.argv[0]
	addon_handle = int(sys.argv[1])

	"""
	List of dictionary with all arguments of previous item
	this way i can pass all values i want from view to view.
	"""
	args = urlparse.parse_qs(sys.argv[2][1:])
	mode = args.get('mode', None)

	"""
 	In order to call dynamically the right controller with its parameters i have to get
	all arguments except the mode one to pass them on the controller.
	
	Arguments aren't sorted so i made a workaround by setting the argument's key as a number,
	this way i can order them into a list using the key as index.
	"""

	kwargs = [args[arg_key][0] for arg_key in args if arg_key != 'mode']
	for arg_key in args:
		if arg_key != 'mode':
			indx = int(arg_key)
			kwargs[indx] = args[arg_key][0]

	URL_LIST = get_all_module_routers()

	if mode is not None:
		route(URL_LIST, mode[0], kwargs)
	else:
		route(URL_LIST, None, kwargs)

