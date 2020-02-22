from resources.lib.controllers import MovieController, TvShowController
base_path = "fpt"

URLS = [
    {base_path: MovieController.fpt_movie},
    {'menu/fpt/keyword': MovieController.fpt_exact_name},
    {"{0}/selected_movie".format(base_path): MovieController.movie_streaming_options},
    {'tvshow_fpt': TvShowController.fpt_tvshow},
    {"{0}/selected_tvshow".format(base_path): TvShowController.fpt_seasons},
    {"{0}/selected_season".format(base_path): TvShowController.fpt_episodes},
    {"{0}/selected_episode".format(base_path): TvShowController.fpt_episodes_streaming_options}
]