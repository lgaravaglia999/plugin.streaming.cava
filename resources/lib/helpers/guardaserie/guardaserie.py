from resources.lib import scraper_lib
from resources.lib.models.season import Season
from resources.lib.models.episode import Episode
import time

class GuardaSerie():
    def __init__(self):
        self.domain = 'http://guardaserie.style/'
        self.search_url = '{0}?s={1}'
        self.cf_session = None
    
    def get_playable_urls(self, block):
        urls = []

        urls.append(scraper_lib.Element(block, el_tag="span", el_class="player-overlay",
            el_property="meta-embed").get_element())

        return urls

    def get_episodes(self, page):
        page = scraper_lib.get_soup(page)
        episodes = []

        episodes_block = scraper_lib.Container(page, tag="a",
            container_class="box-link-serie").get_container()
        
        for i, episode_block in enumerate(episodes_block, start=1):
            urls = self.get_playable_urls(episode_block)
            episode_name = scraper_lib.Element(episode_block, el_tag="div", get_text=True).get_element()

            episodes.append(Episode(title=episode_name, urls=urls, episode_no=i))
                
        return episodes

    def get_seasons(self, page):
        season_lst = []
        seasons = scraper_lib.Container(page, tag="a", container_class="button-sel-serie").get_container()

        for i, season in enumerate(seasons, start=1):

            season_block = scraper_lib.Element(page, el_tag="div",
                el_class="row-stagione-{0}".format(i)).get_element()

            season_lst.append(Season(title="stagione: {0}".format(i), season_no=i, html_block=season_block))

        return season_lst

    def get_search_result(self, keyword):
        keyword = keyword.replace(" ", "+")
        self.cf_session = scraper_lib.get_cf_session()
        
        search_result = scraper_lib.get_page_soup(url=self.search_url.format(self.domain, keyword),
            scraper=self.cf_session)

        tvshow = scraper_lib.Container(block=search_result, tag='div', first=True,
            container_class='col-xs-6 col-sm-2-5').get_container()
        
        info = self.__get_post_info(tvshow)
        time.sleep(1)
        return self.get_seasons(scraper_lib.get_page_soup(info["url"], scraper=self.cf_session))

    def __get_post_info(self, fpt_post):
        post_title = scraper_lib.Element(block=fpt_post, el_tag="div",
            el_class="box-link-serie-bottom", get_text=True).get_element()

        post_ref_url = scraper_lib.Element(block=fpt_post, el_tag="a", el_class="box-link-serie",
            el_property="href").get_element()

        image = "n.d."

        return {"title": post_title, "url": post_ref_url, "image": image}