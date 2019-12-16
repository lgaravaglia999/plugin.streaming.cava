from resources.lib import scraper_lib
from resources.lib.models.movie import Movie
from resources.lib.streaming_hosts.hdload import HDLoad

class Altadefinizione():
    def __init__(self):
        self.domain = 'https://altadefinizione.cloud/'
        self.search_url = '{0}?s={1}'

    def get_playable_url(self, title, hd_iframe, player_name="vidoza"):
        hdload = HDLoad(hd_iframe)
        return hdload.get_final_url(player_name)

    def get_players(self, title, hdpass_iframe_url):
        hdload = HDLoad(hdpass_iframe_url)
        players = hdload.get_all_players()
        return Movie(title=title, page_url=hdpass_iframe_url ,urls=players)

    def get_hdload_frame(self, title, movie_url):
        altadefinizione_page = scraper_lib.get_page_soup(movie_url)

        hdpass_iframe = scraper_lib.Element(altadefinizione_page,
            'iframe', el_id='iframeVid').get_element()

        hdpass_iframe_url = hdpass_iframe["src"]
        return hdpass_iframe_url

    def get_search_result(self, keyword):
        search_result = scraper_lib.get_page_soup(self.search_url.format(self.domain, keyword))
        movies_list = []

        movies = scraper_lib.Container(block=search_result, tag='div', container_class='col-lg-3 col-md-3 col-xs-3').get_container()
        for movie in movies:
            movies_list.append(self.__get_post_info(movie))

        return movies_list

    def __get_post_info(self, fpt_post):
        post_title = scraper_lib.Element(block=fpt_post, el_tag="h5",
            el_class="titleFilm", get_text=True).get_element()

        post_ref_url = scraper_lib.Element(block=fpt_post, el_tag="a",
            el_property="href").get_element()

        try:
            image = scraper_lib.Element(block=fpt_post, el_tag="img",
                el_class="attachment-loc-film size-loc-film wp-post-image", el_property="src").get_element()
        except:
            image = "n.d."

        movie = Movie(title=post_title, page_url=post_ref_url)
        movie.image_url = image
        return movie