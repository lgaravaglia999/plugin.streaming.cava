from resources.lib.controllers import MainController

URLS = [
    {'play': MainController.play},
    {'play_direct': MainController.play_direct},
    {'play_hardcoded': MainController.get_json_movies},
    {'tmdb_movie': MainController.select_website}

]
