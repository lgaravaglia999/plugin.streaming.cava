from resources.lib import kodiutilsitem
from resources.lib.models.tvShow import TvShow
from resources.lib.models.season import Season
from resources.lib.models.episode import Episode

class TvShowView(object):
    def __init__(self, website):
        self.on_selected_tvshow = "{0}/selected_tvshow".format(website)
        self.on_season_click = "{0}/selected_season".format(website)
        self.on_episode_click = "{0}/selected_episode".format(website)
        self.on_playable_urls_click = "play"

    def show_tvshows_results(self, tvshows, media_type):
        """
        Show all movies/tv shows scraped
        :param tvshows: list of TvShow objects
        :param media_type: str
        """
        is_folder = True
        for tvshow in tvshows:
            item_url = {
                'mode': media_type,
                '0': tvshow.title.encode("utf-8"),
                '1': tvshow.page_url
                }

            item_title = u''.join(tvshow.title).encode("utf-8").strip()
        
            item_arts = {
                'thumb': tvshow.image_url,
                'fanart': tvshow.image_url
                }

            kodiutilsitem.add_item(url_dict=item_url, title=item_title,
                is_folder=is_folder, arts=item_arts)
            
        kodiutilsitem.end_directory()

    def show_tv_seasons(self, tv_title, seasons, fpt_tv_url=None):
        """
        Show all seasons of the selected tv show.
        
        :param tv_title: str
        :param fpt_tv_url: str
        :param seasons: list of Seasons objects
        """

        is_folder = True
        for season in seasons:
            item_url = {
                #'mode':'tvshow/selected_season',
                'mode': self.on_season_click,
                '0': season.title.encode("utf-8"),
                '1': season.html_block.encode("utf-8") if fpt_tv_url is None else fpt_tv_url,
                '2': season.season_no
                }
            
            item_title = u''.join(season.title).encode("utf-8").strip()

            kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder)
            
        kodiutilsitem.end_directory()

    def show_season_episodes(self, tv_title, episodes):
        """
        Show all episodes of the selected season.
        
        :param tv_title: str
        :param episodes: list of Episode objects
        """
        is_folder = True
        for episode in episodes:
            idx = 1
            ep_title = episode.title
            ep_urls = episode.urls

            item_url = {
                'mode': self.on_episode_click,
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

    def show_playable_url(self, movie_title, movie_urls):
        """
        Show playable items with all streaming options for the selected movie.

        :param movie_title: str
        :param movie_urls: list of strings representing movie url
        """
        is_folder = False
        for movie_url in movie_urls:
            streaming_source = kodiutilsitem.get_streaming_source_name(movie_url)

            item_url = {
                'mode': self.on_playable_urls_click,
                '0': movie_title,
                '1': movie_url
                }
            
            item_title = "{0} [{1}]".format(movie_title, streaming_source)

            item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

            kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
                properties=item_property)
                    
        kodiutilsitem.end_directory()

