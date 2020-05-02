from resources.lib.controllers import HDCloudController
from websites_config import WebsitesConfig as cfg

#base_path = "hdcloud"
base_path_movie = cfg.get_path(cfg.ALTADEFINIZIONE)
base_path_tvshow = cfg.get_path(cfg.SERIE_HD)

URLS = [
    {"play_hd": HDCloudController.play_hd},
    {base_path_movie: HDCloudController.show_movies},
    {"{0}/selected_movie".format(base_path_movie): HDCloudController.movie_streaming_options},

    {base_path_tvshow: HDCloudController.tvshow},
    {"{0}/selected_tvshow".format(base_path_tvshow): HDCloudController.tvshow_seasons},
    {"{0}/selected_season".format(base_path_tvshow): HDCloudController.tvshow_episodes},
    {"{0}/selected_episode".format(base_path_tvshow): HDCloudController.tvshow_streaming_options}
]