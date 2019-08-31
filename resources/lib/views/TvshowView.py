from resources.lib import kodiutilsitem

def show_fpt_results(posts_data, media_type):
    """
    Show all movies/tv shows scraped
    :param posts_data: list of dictionaries representing scraped info
    :param media_type: str
    """
    is_folder = True
    for post in posts_data:
        item_url = {
            'mode': media_type,
            '0': post["title"].encode("utf-8"),
            '1': post["url"]
            }

        item_title = u''.join(post["title"]).encode("utf-8").strip()
      
        item_arts = {
            'thumb': post["image"],
            'fanart': post["image"]
            }
        kodiutilsitem.add_item(url_dict=item_url, title=item_title,
            is_folder=is_folder, arts=item_arts)
        
    kodiutilsitem.end_directory()

def show_tv_seasons(tv_title, fpt_tv_url, tv_seasons_list):
    """
    Show all seasons of the selected tv show.
    
    :param tv_title: str
    :param fpt_tv_url: str
    :param tv_seasons_list: list of seasons name
    """

    is_folder = True
    for i in range(len(tv_seasons_list)):
        item_url = {
            'mode':'tvshow/selected_season',
            #'series_title': tv_title,
            '0': tv_seasons_list[i].encode("utf-8"),
            '1': fpt_tv_url,
            '2': i
            }
        
        item_title = u''.join(tv_seasons_list[i]).encode("utf-8").strip()

        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder)
        
    kodiutilsitem.end_directory()

def show_season_episodes(tv_title, episodes):
    """
    Show all episodes of the selected season.
    
    :param tv_title: str
    :param episodes: list of dictionaries representing episodes name and a list of urls
    """
    is_folder = True
    for episode in episodes:
        idx = 1
        ep_title = list(episode.keys())[0]
        ep_urls = episode[ep_title]

        item_url = {
            'mode':'tvshow/selected_episode',
            '0': ep_title.encode("utf-8")
            }
        
        for url in ep_urls:
            item_url[idx] = url
            idx += 1
    
        item_title = u"".join(ep_title).encode("utf-8").strip()

        item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
            properties=item_property)

    kodiutilsitem.end_directory()

def show_scraped_url(movie_title, movie_urls):
    """
    Show playable items with all streaming options for the selected movie.

    :param movie_title: str
    :param movie_urls: list of strings representing movie url
    """
    is_folder = False
    for movie_url in movie_urls:
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

