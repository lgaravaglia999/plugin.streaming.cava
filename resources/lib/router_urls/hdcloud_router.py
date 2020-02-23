from resources.lib.controllers import HDCloudController
from websites_config import WebsitesConfig as cfg

#base_path = "hdcloud"
base_path = cfg.get_path(cfg.ALTADEFINIZIONE)

URLS = [
    {"play_hd": HDCloudController.play_hd},
    {base_path: HDCloudController.show_movies},
    {"{0}/selected_movie".format(base_path): HDCloudController.movie_streaming_options}
]