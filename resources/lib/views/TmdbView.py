from resources.lib import kodiutilsitem
from resources.lib.models.tmdb.MovieDb import MovieDb

NEXT_PAGE = "Next Page --->"
tmdb = MovieDb()

def show_moviedb_results(results, media_type, tmdb_type, page=1, keyword=None):
    """
    Show movies or tv shows got from the themoviedb api request.
    
    :param results: list of dictionaries representing themoviedb api request's results
    :param media_type: str represent movie or tv show type (used for routing)
    :param tmdb_type: str represent mode for paginations
    :param page: int
    :param keyword: str, optional represent user keyboard input
    """
    is_folder = True
    page = int(page)
    for media in results:
        item_url = {
            'mode': media_type,
            '0': media["titolo"].encode("utf-8"),
            #'year': media["anno"],
            }
        
        item_title = media["titolo"].encode("utf-8")

        item_arts = {
            'thumb': tmdb.MOVIEDB_IMAGE_URL.format('500', media["poster"]),
            'fanart': tmdb.MOVIEDB_IMAGE_URL.format('500', media["poster"])
            }
        
        item_info = {'title': media["titolo"].encode('utf-8'),
                    'plot': media["trama"].encode('utf-8'),
                    'year': media["anno"],
                    'mediatype': 'movie'
                    }
        
        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
                info=item_info, arts=item_arts)
        
    if keyword is not None:
        kodiutilsitem.add_menu_item({
            'mode' : tmdb_type,
            '0': page+1,
            '1': keyword
            }, NEXT_PAGE)
    else:
        kodiutilsitem.add_menu_item({
            'mode' : tmdb_type,
            '0': page+1,
            }, NEXT_PAGE)

    kodiutilsitem.end_directory()


def show_moviedb_cast_results(results, media_type, tmdb_type, page=1, keyword=None):
    """
    Show cast got from the themoviedb api request.
    
    :param results: list of dictionaries representing themoviedb api request's results
    :param media_type: str
    :param tmdb_type: str represent routing url for paginations
    :param page: int
    :param keyword: str, optional represent user keyboard input
    """
    is_folder = True
    page = int(page)
    for media in results:
        item_url = {
            'mode': media_type,
            '0': 0,
            '1': media["people_id"]
            #'year': media["anno"],
            }
        
        item_title = media["nome"].encode("utf-8")

        item_arts = {
            'thumb': tmdb.MOVIEDB_IMAGE_URL.format('500', media["poster"]),
            'fanart': tmdb.MOVIEDB_IMAGE_URL.format('500', media["poster"])
            }
        
        item_info = {'title': media["nome"].encode('utf-8'),
                    'mediatype': 'movie'
                    }
        
        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
                info=item_info, arts=item_arts)
        
    if keyword is not None:
        kodiutilsitem.add_menu_item({
            'mode' : tmdb_type,
            '0': page+1,
            '1': keyword
            }, NEXT_PAGE)
    else:
        kodiutilsitem.add_menu_item({
            'mode' : tmdb_type,
            '0': page+1,
            }, NEXT_PAGE)

    kodiutilsitem.end_directory()
