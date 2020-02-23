import sys
from resources.lib.views.TvshowView import TvShowView
from resources.lib.router_urls.websites_config import WebsitesConfig as cfg

#WEBSITE = "gs"
WEBSITE = cfg.get_path(cfg.GUARDASERIE)

class GuardaserieView(TvShowView):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(GuardaserieView, self).__init__(WEBSITE)
        else:
            super().__init__(WEBSITE)
