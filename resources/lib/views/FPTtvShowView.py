import sys
from resources.lib.views.TvshowView import TvShowView
from resources.lib.router_urls.websites_config import WebsitesConfig as cfg


#WEBSITE = "fpt"
WEBSITE = cfg.get_path(cfg.FILMPERTUTTI_TVSHOW)

class FPTtvShowView(TvShowView):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(FPTtvShowView, self).__init__(WEBSITE)
        else:
            super().__init__(WEBSITE)