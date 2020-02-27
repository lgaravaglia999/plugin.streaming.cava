import sys
from resources.lib.views.TvshowView import TvShowView
from resources.lib.router_urls.websites_config import WebsitesConfig as cfg

WEBSITE = cfg.get_path(cfg.ITALIASERIE_ORG)

class ItaliaserieOrgView(TvShowView):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(ItaliaserieOrgView, self).__init__(WEBSITE)
        else:
            super().__init__(WEBSITE)
