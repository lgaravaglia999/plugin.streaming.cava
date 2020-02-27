from resources.lib import scraper_lib
from resources.lib.models.tvShow import TvShow
from resources.lib.models.season import Season
from resources.lib.models.episode import Episode

class ItaliaSerie():
    def __init__(self):
        self.domain = 'https://italiaserie.org/'
        self.search_url = '{0}?s={1}'
        self.cf_session = None

    def get_episodes(self, page_url, season_no=1):
        episodes_lst = []
        block = scraper_lib.get_page_soup(page_url)

        episodes_container = scraper_lib.Container(block, tag="div",
            container_class="su-spoiler-content").get_container()[season_no-1]
        
        episodes_block = scraper_lib.Container(episodes_container,
            tag="div", container_class="su-link-ep").get_container()
        
        for i, episode in  enumerate(episodes_block, start=1):
            urls = []
            ep_title = scraper_lib.get_text(episode).replace('\n', '').strip()
            urls.append(scraper_lib.Element(episode, el_tag="a",
                el_property="href").get_element())
            
            episodes_lst.append(Episode(title=ep_title, urls=urls, episode_no=i))
                
        return episodes_lst

    def get_seasons(self, page_url):
        seasons_page = []
        page = scraper_lib.get_page_soup(page_url)

        seasons = scraper_lib.Container(page, tag="div",
                container_class="su-spoiler-title").get_container()
                
        for i, season in enumerate(seasons, start=1):
            seasons_page.append(Season(title="stagione: {0}".format(i), season_no=i))
        return seasons_page

    def get_search_result(self, keyword):
        tvshow_lst = []
        keyword = keyword.replace(" ", "+")
        search_result = scraper_lib.get_page_soup(url=self.search_url.format(self.domain, keyword))

        div_posts = scraper_lib.Container(block=search_result, tag='ul',
            container_class='recent-posts', first=True).get_container()
        
        tvshows = scraper_lib.Container(block=div_posts, tag='li').get_container()

        for tvshow in tvshows:
            try:
                tvshow_lst.append(self.__get_post_info(tvshow))
            except:
                pass

        return tvshow_lst

    def __get_post_info(self, block):

        info_block = scraper_lib.Container(block=block, tag="h2",
            first=True).get_container()

        post_title = scraper_lib.Element(block=info_block, el_tag="a",
            get_text=True).get_element()
        
        post_ref_url = scraper_lib.Element(block=block, el_tag="a",
            el_property="href").get_element()
        
        try:
            image = scraper_lib.Element(block=block, el_tag="img", el_class="Thumbnail",
                el_property="src").get_element()
        except:
            image = "n.d."

        tvshow = TvShow(title=post_title, page_url=post_ref_url)
        tvshow.image_url=image
        return tvshow