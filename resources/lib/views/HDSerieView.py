import sys
from resources.lib import kodiutilsitem
from resources.lib.models.movie import Movie
from resources.lib.views.TvshowView import TvShowView
from resources.lib.router_urls.websites_config import WebsitesConfig as cfg

#WEBSITE = "seriehd"
WEBSITE = cfg.get_path(cfg.SERIE_HD)

class HDSerieView(TvShowView):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(HDSerieView, self).__init__(WEBSITE)
        else:
            super().__init__(WEBSITE)


    def show_tv_seasons(self, tv_title, seasons):
        """
        Show all seasons of the selected tv show.
        
        :param tv_title: str
        :param fpt_tv_url: str
        :param seasons: list of Seasons objects
        """

        is_folder = True
        for season in seasons:
            item_url = {
                'mode': self.on_season_click,
                '0': season.title.encode("utf-8"),
                '1': season.ref_url
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
            ep_title = episode.title

            item_url = {
                'mode': self.on_episode_click,
                '0': ep_title.encode("utf-8"),
                '1': episode.urls
                }
        
        
            item_title = u"".join(ep_title).encode("utf-8").strip()

            item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

            kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
                properties=item_property)

        kodiutilsitem.end_directory()

    def show_hdplayers(self, movie):
        is_folder = False
        movie_title = movie.title
        #working_urls = ["vidoza", "fembed", "gounlimited", "mixdrop"]

        for player_name in movie.urls:
            item_url = {
                'mode':'play_hd',
                '0': movie_title,
                '1': movie.page_url,
                '2': player_name
                }
            item_title = "{0} [{1}]".format(movie_title, player_name)

            item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

            kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
                properties=item_property)
                    
        kodiutilsitem.end_directory()