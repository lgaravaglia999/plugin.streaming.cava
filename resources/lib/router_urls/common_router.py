from resources.lib.controllers import MainController

URLS = [
    {'play': MainController.play},
    {'play_direct': MainController.play_direct},
    {'play_hardcoded': MainController.get_json_movies},
    {'tmdb_movie': MainController.select_website},
    {'tmdb_tvshow': MainController.select_tv_from_website},
    {'menu/keyword_websites': MainController.search_from_websites},
    {'menu/keyword_tv_websites': MainController.search_tv_from_websites}
]
