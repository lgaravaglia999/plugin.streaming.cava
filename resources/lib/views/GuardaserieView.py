import sys
from resources.lib.views.TvshowView import TvShowView

WEBSITE = "gs"

class GuardaserieView(TvShowView):
    def __init__(self):
        if sys.version_info[0] < 3:
            super(GuardaserieView, self).__init__(WEBSITE)
        else:
            super().__init__(WEBSITE)
