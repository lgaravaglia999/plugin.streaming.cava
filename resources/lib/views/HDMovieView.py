import sys
from resources.lib import kodiutilsitem
from resources.lib.models.movie import Movie
from resources.lib.views.MovieView import MovieView

WEBSITE = "hdcloud"

class HDMovieView(MovieView):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(HDMovieView, self).__init__(WEBSITE)
        else:
            super().__init__(WEBSITE)

    def show_hdplayers(self, movie):
        is_folder = False
        movie_title = movie.title
        working_urls = ["vidoza", "fembed", "gounlimited", "mixdrop"]

        for player_name in movie.urls:
            item_url = {
                'mode':'play_hd',
                '0': movie_title,
                '1': movie.page_url,
                '2': player_name
                }
            if player_name in working_urls:
                item_title = "{0} [{1}]".format(movie_title, player_name)
            else:
                item_title = "{0} [{1}]  ---- rotto ----".format(movie_title, player_name)

            item_property = {"prop_key": 'IsPlayable', "prop_value": 'true'}

            kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder,
                properties=item_property)
                    
        kodiutilsitem.end_directory()