from resources.lib import scraper_lib
from resources.lib.models.tvShow import TvShow
from resources.lib.models.season import Season
from resources.lib.models.episode import Episode
from resources.lib.streaming_hosts.hdload import HDLoad
from resources.lib.models.movie import Movie


#
# TODO:
# - ottenere il testo pulito(togliendo spazi e vari \n);
# - finire get_season()
# - fare il binding con i models del plugin(Tvshow, Seasons, Episode)


class SerieHD():
    def __init__(self):
        self.domain = 'https://seriehd.net/'
        self.search_url = '{0}?s={1}'
        self.cf_session = None

    def get_playable_url(self, title, hd_iframe, player_name="Vidoza"):
        hdload = HDLoad(hd_iframe)
        return hdload.get_final_url(player_name)

    def get_players(self, title, hdpass_iframe_url):
        hdload = HDLoad(hdpass_iframe_url)
        players = hdload.get_all_players()
        return  Movie(title=title, page_url=hdpass_iframe_url ,urls=players)

    def get_episodes(self, episodes_url):
        episodes = []

        page = scraper_lib.get_page_soup(url=episodes_url)

        episodes_container = scraper_lib.Container(page, tag="div", first=True,
            container_class="buttons-bar episodes").get_container()

        episode_soup = scraper_lib.get_soup_prettified(episodes_container)

        episodes_block = scraper_lib.Container(episode_soup, tag="li").get_container()

        for episode in episodes_block:
            episode_no = scraper_lib.get_text(episode).strip()

            episodes.append(Episode(title="Episodio {0}".format(episode_no), episode_no=episode_no,
                urls=scraper_lib.get_hrefs(episode)[0]))
        
        return episodes

    def get_seasons(self, tvshow_page_url):
        seasons = []
        page = scraper_lib.get_page_soup(url=tvshow_page_url)
        iframe = self.__get_iframe_page(page)

        seasons_container = scraper_lib.Container(iframe, tag="div", first=True,
            container_class="buttons-bar seasons").get_container()

        season_soup = scraper_lib.get_soup_prettified(seasons_container)

        seasons_block = scraper_lib.Container(season_soup, tag="li").get_container()

        for season in seasons_block:
            season_no = scraper_lib.get_text(season).strip()

            seasons.append(Season(title="Stagione {0}".format(scraper_lib.get_text(season).strip()), season_no=season_no,
             ref_url=scraper_lib.get_hrefs(season)[0]))

        return seasons

    def get_search_result(self, keyword):
        results = []
        
        search_result = scraper_lib.get_page_soup(url=self.search_url.format(self.domain, keyword))

        tvshows = scraper_lib.Container(block=search_result, tag='div',
            container_class='col-xl-3 col-lg-3 col-md-3 col-sm-6 col-6').get_container()

        for tvshow in tvshows:
            results.append(self.__get_post_info(tvshow))
        
        return results

    def __get_post_info(self, fpt_post):
        post_title = scraper_lib.Element(block=fpt_post, el_tag="div",
            el_class="infoSeries", get_text=True).get_element()

        post_ref_url = scraper_lib.Element(block=fpt_post, el_tag="a",
            el_property="href").get_element()

        try:
            image = scraper_lib.Element(block=fpt_post, el_tag="img", el_class="img-full",
                el_property="src").get_element()
        except:
            image = "n.d."

        tv_show = TvShow(title=post_title, page_url=post_ref_url)
        tv_show.image_url = image
        return tv_show
    
    def __get_iframe_page(self, seriehd_page):

        hdpass_iframe = scraper_lib.Element(seriehd_page,
            'iframe', el_id='iframeVid').get_element()

        return scraper_lib.get_page_soup(url=hdpass_iframe["src"])