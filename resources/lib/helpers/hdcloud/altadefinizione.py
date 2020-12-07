from resources.lib import scraper_lib
from resources.lib import google_scraper #soluzione temporanea a cloudfare
from resources.lib.models.movie import Movie
from resources.lib.streaming_hosts.hdload import HDLoad

class Altadefinizione():
    def __init__(self):
        self.domain = 'https://altadefinizione.dance/'
        self.search_url = '{0}?s={1}'


    def get_movie_url_from_google(self, keyword):
        return google_scraper.get_first_result(keyword, self.domain)

    def get_playable_url(self, title, hd_iframe, player_name="Vidoza"):
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
        movies_list = []
        raw_keyword = keyword
        keyword = raw_keyword.replace(" ", "+")
        search_result = scraper_lib.get_page_soup(url=self.search_url.format(self.domain, keyword), check_result=True)

        if (search_result == -1):
            result_url = self.get_movie_url_from_google(keyword)
            search_result = scraper_lib.get_page_soup(url=result_url)
            
        movies = scraper_lib.Container(block=search_result, tag='div', container_class='col-lg-3 col-md-4 col-xs-4 mb-30').get_container()
        
        for movie in movies:
            movies_list.append(self.__get_post_info(movie))

        if (not movies_list):
            try:
                title = scraper_lib.Element(block=search_result, el_tag='title', get_text=True).get_element()
            except:
                title = raw_keyword

            movie = Movie(title=title, page_url=result_url)
            movie.image_url = "n.d."
            movies_list.append(movie)

        return movies_list

    def __get_post_info(self, fpt_post):
        try:
            post_title = scraper_lib.Element(block=fpt_post, el_tag="h5",
                el_class="titleFilm", get_text=True).get_element()
        except:
            post_title = scraper_lib.Element(block=fpt_post, el_tag="h2",
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