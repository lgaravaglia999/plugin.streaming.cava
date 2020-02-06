from resources.lib.controllers import MovieController, TvShowController
base_path = "fpt"

URLS = [
    {base_path: MovieController.fpt_movie},
    {'menu/fpt/keyword': MovieController.fpt_exact_name},
    {'{0}/selected_movie': MovieController.movie_streaming_options},
	{'tmdb_tvshow': TvShowController.fpt_tvshow},
    {'tvshow/fpt_tv': TvShowController.fpt_seasons},
    {'tvshow_fpt': TvShowController.fpt_tvshow},
    # {'tvshow/selected_season': TvShowController.fpt_episodes},
    # {'tvshow/selected_episode': TvShowController.fpt_episodes_streaming_options},
    # {"{0}/selected_tvshow".format(base_path): ""},
    {"{0}/selected_season".format(base_path): TvShowController.fpt_episodes},
    {"{0}/selected_episode".format(base_path): TvShowController.fpt_episodes_streaming_options}
]