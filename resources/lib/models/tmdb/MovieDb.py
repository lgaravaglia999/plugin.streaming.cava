import requests

class MovieDb:

    def __init__(self):
        self.MOVIEDB_API_KEY = "e88c6bf9342d064606be7cd7680a03d7"
        self.REGION = "IT"
        self.LANGUAGE = "it-IT"
        self.API_URL = "https://api.themoviedb.org/3"

        self.COMMON_SETTINGS = "api_key={0}&language={1}&region={2}".format(
                self.MOVIEDB_API_KEY,
                self.LANGUAGE,
                self.REGION
        )

        """
        Movie urls
        """
        self.MOST_VOTED_MOVIES_URL = "{0}/movie/top_rated?{1}&page={2}"
        self.UPCOMING_MOVIES_URL = "{0}/movie/upcoming?{1}&page={2}"
        self.NOW_PLAYING_MOVIES_URL = "{0}/movie/now_playing?{1}&page={2}"
        self.MOST_POPULAR_MOVIES_URL = "{0}/movie/popular?{1}&page={2}"
        self.SEARCH_MOVIE_URL = "{0}/search/movie?{1}&page={2}&query={3}"

        """
        TV Serie urls
        """
        self.MOST_VOTED_TV_URL = "{0}/tv/top_rated?{1}&page={2}"
        self.ON_AIR_TV_URL = "{0}/tv/on_the_air?{1}&page={2}"
        self.MOST_POPULAR_TV_URL = "{0}/tv/popular?{1}&page={2}"
        self.SEARCH_TV_URL = "{0}/search/tv?{1}&page={2}&query={3}"

        """
        People urls
        """
        self.SEARCH_PEOPLE_URL = "{0}/search/person?{1}&page={2}&query={3}"
        self.PEOPLE_MOVIES_URL = "{0}/person/{1}/movie_credits?{2}"

        self.MOVIEDB_IMAGE_URL = "https://image.tmdb.org/t/p/w{0}/{1}"

    def search_moviesdb(self, keyword, page=1):
        tmdb_url = self.SEARCH_MOVIE_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page,
                keyword)

        return self._get_movie_result(tmdb_url)

    def get_most_voted_movies(self, page=1):
        tmdb_url = self.MOST_VOTED_MOVIES_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page)

        return self._get_movie_result(tmdb_url)

    def get_most_popular_movies(self, page=1):
        tmdb_url = self.MOST_POPULAR_MOVIES_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page)

        return self._get_movie_result(tmdb_url)

    def get_now_playing_movies(self, page=1):
        tmdb_url = self.NOW_PLAYING_MOVIES_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page)

        return self._get_movie_result(tmdb_url)

    def search_tvseries(self, keyword, page=1):
        tmdb_url = self.SEARCH_TV_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page,
                keyword)

        return self._get_tv_result(tmdb_url)

    def get_most_voted_tvseries(self, page=1):
        tmdb_url = self.MOST_VOTED_TV_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page)

        return self._get_tv_result(tmdb_url)

    def get_most_popular_tvseries(self, page=1):
        tmdb_url = self.MOST_POPULAR_TV_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page)

        return self._get_tv_result(tmdb_url)
		
    def get_on_air_tvseries(self, page=1):
        tmdb_url = self.ON_AIR_TV_URL.format(
                self.API_URL,
                self.COMMON_SETTINGS,
                page)
        return self._get_tv_result(tmdb_url)

    def search_people(self, keyword, page=1):
        tmdb_url = self.SEARCH_PEOPLE_URL.format(
            self.API_URL,
            self.COMMON_SETTINGS,
            page,
            keyword)
        return self.__get_people_result(tmdb_url)

    def get_people_movies(self, people_id):
        tmdb_url = self.PEOPLE_MOVIES_URL.format(
            self.API_URL,
            people_id,
            self.COMMON_SETTINGS)
        
        return self._get_people_movie_result(tmdb_url)

    def __get_people_result(self, tmdb_url):
        result = requests.get(tmdb_url).json()

        return list(map(
                lambda x: {
                        "nome":x["name"],
                        "people_id":x["id"],
                        "poster":x["profile_path"]
                        },
                        result['results']))
    
    def _get_people_movie_result(self, tmdb_url):
        result = requests.get(tmdb_url).json()

        return list(map(
                lambda x: {
                        "titolo":x["title"],
                        "trama":x["overview"],
                        "anno":x.get("release_date", '-').split('-')[0],
                        "genere":x["genre_ids"],
                        "poster":x["poster_path"]
                        },
                        result['cast']))

    def _get_movie_result(self, tmdb_url):
        result = requests.get(tmdb_url).json()

        return list(map(
                lambda x: {
                        "titolo":x["title"],
                        "trama":x["overview"],
                        "anno":x["release_date"].split('-')[0],
                        "genere":x["genre_ids"],
                        "poster":x["poster_path"]
                        },
                        result['results']))

    def _get_tv_result(self, tmdb_url):
        
        result = requests.get(tmdb_url).json()

        return list(map(
                lambda x: {
                        "titolo":x["name"],
                        "trama":x["overview"],
                        "anno":x.get("first_air_date", '-').split('-')[0],
                        "genere":x["genre_ids"],
                        "poster":x["poster_path"]
                        },
                        result['results']))