from resources.lib.controllers import MovieController, TvShowController

URLS = [
    {'tmdb_movie': MovieController.fpt_movie},
    {'menu/fpt/keyword': MovieController.fpt_exact_name},
    {'movies/fpt_movie': MovieController.movie_streaming_options},
	{'tmdb_tvshow': TvShowController.fpt_tvshow},
    {'tvshow/fpt_tv': TvShowController.fpt_seasons},
    {'tvshow/selected_season': TvShowController.fpt_episodes},
    {'tvshow/selected_episode': TvShowController.fpt_episodes_streaming_options},
]