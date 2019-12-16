from resources.lib import kodiutilsitem
from resources.lib.models.movie import Movie

def show_fpt_results(movies, media_type):
    """
    Show all movies/tv shows scraped
    :param posts_data: list of Movie objects
    :param media_type: str
    """
    is_folder = True
    for movie in movies:
        item_url = {
            'mode': media_type,
            '0': movie.title.encode("utf-8"),
            '1': movie.page_url
            }

        item_title = u''.join(movie.title).encode("utf-8").strip()
      
        item_arts = {
            'thumb': movie.image_url,
            'fanart': movie.image_url
            }
        kodiutilsitem.add_item(url_dict=item_url, title=item_title,
            is_folder=is_folder, arts=item_arts)
        
    kodiutilsitem.end_directory()

def show_scraped_url(movie):
    """
    Show playable items with all streaming options for the selected movie.

    :param movie_title: str
    :param movie_urls: list of strings representing movie url
    """
    is_folder = False
    movie_title = movie.title

    for movie_url in movie.urls:
        streaming_source = kodiutilsitem.get_streaming_source_name(movie_url)

        item_url = {
            'mode':'play',
            '0': movie_title,
            '1': movie_url
            }
        
        item_title = "{0} [{1}]".format(movie_title, streaming_source)

        item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
            properties=item_property)
                
    kodiutilsitem.end_directory()

def show_hdplayers(movie):
    """
    Show playable items with all streaming options for the selected movie.

    :param movie_title: str
    :param movie_urls: list of strings representing movie url
    """
    is_folder = False
    movie_title = movie.title

    for player_name in movie.urls:
        item_url = {
            'mode':'play_hd',
            '0': movie_title,
            '1': movie.page_url,
            '2': player_name
            }
        if player_name == "vidoza" or player_name == "fembed":
            item_title = "{0} [{1}] ** migliori **".format(movie_title, player_name)
        else:
            item_title = "{0} [{1}]".format(movie_title, player_name)

        item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
            properties=item_property)
                
    kodiutilsitem.end_directory()

def show_jsons(movies):
    """
    Show movies from json file

    :param movie_title: str
    :param movie_urls: list of strings representing movie url
    """
    is_folder = False

    for movie in movies:
        item_url = {
            'mode':'play_direct',
            '0': movie.title,
            '1': movie.urls
            }
        
        item_title = "{0}".format(movie.title)

        item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
            properties=item_property)
                
    kodiutilsitem.end_directory()