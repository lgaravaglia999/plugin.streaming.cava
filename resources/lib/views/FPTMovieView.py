import sys
from resources.lib import kodiutilsitem
from resources.lib.models.movie import Movie
from resources.lib.views.MovieView import MovieView
from resources.lib.router_urls.websites_config import WebsitesConfig as cfg

#WEBSITE = "fpt"
WEBSITE = cfg.get_path(cfg.FILMPERTUTTI_MOVIE)

class FPTMovieView(MovieView):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(FPTMovieView, self).__init__(WEBSITE)
        else:
            super().__init__(WEBSITE)