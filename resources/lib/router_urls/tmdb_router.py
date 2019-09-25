from resources.lib.controllers import TmdbController

URLS = [
    {'menu/movies/keyword': TmdbController.movie_by_keyword},
    {'menu/movies/most_popular': TmdbController.most_popular_movies},
    {'menu/movies/most_voted': TmdbController.most_voted_movies},
    {'menu/movies/now_playing': TmdbController.now_playing_movies},
    {'menu/tvshow/keyword': TmdbController.tvshow_by_keyword},
    {'menu/tvshow/most_popular': TmdbController.most_popular_tvshow},
    {'menu/tvshow/most_voted': TmdbController.most_voted_tvshow},
    {'menu/tvshow/on_air': TmdbController.on_air_tvshow},
    {'menu/people/keyword': TmdbController.people_by_keyword},
    {'menu/people/movies': TmdbController.movie_by_people}
]