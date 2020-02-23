from resources.lib.controllers import MovieController, TvShowController
from websites_config import WebsitesConfig as cfg

#base_path = "fpt"
base_path_m = cfg.get_path(cfg.FILMPERTUTTI_MOVIE)
base_path_tv = cfg.get_path(cfg.FILMPERTUTTI_TVSHOW)

URLS = [
    {base_path_m: MovieController.fpt_movie},
    {'menu/fpt/keyword': MovieController.fpt_exact_name},
    {"{0}/selected_movie".format(base_path_m): MovieController.movie_streaming_options},
    {base_path_tv: TvShowController.fpt_tvshow},
    {"{0}/selected_tvshow".format(base_path_tv): TvShowController.fpt_seasons},
    {"{0}/selected_season".format(base_path_tv): TvShowController.fpt_episodes},
    {"{0}/selected_episode".format(base_path_tv): TvShowController.fpt_episodes_streaming_options}
]