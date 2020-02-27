import inspect

#SOLUZIONE TEMPORANEA PER SUPPORTARE PYTHON 2
#IN SEGUITO USARE ENUM

class WebsitesConfig(object):
    ALTADEFINIZIONE = {"name": "Altadefinizione", "base_path": "hdcloud",
                            "is_movie": True}

    FILMPERTUTTI_MOVIE = {"name": "FilmPerTutti [Film]", "base_path": "fpt",
                            "is_movie": True}

    FILMPERTUTTI_TVSHOW = {"name": "FilmPerTutti [Serie TV]", "base_path": "fpt_tv",
                            "is_movie": False}

    GUARDASERIE = {"name": "Guardaserie", "base_path": "gs", "is_movie": False}

    ITALIASERIE_ORG = {"name": "ITALIASERIE ORG", "base_path": "italiaserie_org",
                            "is_movie": False}


    @staticmethod
    def get_name(website):
        return website["name"]

    @staticmethod
    def get_path(website):
        return website["base_path"]

    @staticmethod
    def get_all_movies():
        attributes = inspect.getmembers(WebsitesConfig, lambda a:not(inspect.isroutine(a)))
        return [a[1] for a in attributes if not(a[0].startswith('__')
                    and a[0].endswith('__')) and a[1]["is_movie"]]

    @staticmethod
    def get_all_tvshow():
        attributes = inspect.getmembers(WebsitesConfig, lambda a:not(inspect.isroutine(a)))
        return [a[1] for a in attributes if not(a[0].startswith('__')
                    and a[0].endswith('__')) and not a[1]["is_movie"]]