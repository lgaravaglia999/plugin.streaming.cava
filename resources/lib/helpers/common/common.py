from resources.lib.models.movie import Movie
import os
import json

def load_movies_from_json():
    json_path = os.path.dirname(os.path.realpath(__file__))
    json_fullname = json_path + "/example.json"
    movies = []
    with open(json_fullname) as json_file:
        data = json.load(json_file)
        for json_movie in data["movies"]:
            movie = Movie(title=json_movie["title"], urls=json_movie["url"])
            movies.append(movie)
    return movies


def load_tvshow_from_json():
    pass
