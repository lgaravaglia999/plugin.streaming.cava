import re
import requests
import sys

from resources.lib import scraper_lib
from resources.lib.models.season import Season
from resources.lib.models.episode import Episode
from resources.lib.helpers.filmpertutti.FPTScraper import FPTScraper


class TvSeries(FPTScraper):

    def __init__(self, release_date=None):
        if sys.version_info[0] < 3:
            super(TvSeries, self).__init__(release_date)
        else:
            super().__init__(release_date)

        self.seasons_lst = []
        self.is_modern_state = True
        self.replacing_chars = ["\n", ";", " "]
    
    def get_result_from_fpt(self, keyword):
        return self.get_fpt_posts(keyword, "tvshow")
    
    def scrape(self, fpt_tvshow_url):
        self.soup = scraper_lib.get_page_soup(fpt_tvshow_url)
        self.seasons_wrapper = self.get_seasons_wrapper()
    
    def replace_chars(self, word):
        for char_to_replace in self.replacing_chars:
            word = word.replace(char_to_replace, '')
        return word.strip()

    def get_episode_info(self, tag, episode_number):
        episode_urls = []
        if self.is_modern_state:

            episode_wrapper = scraper_lib.get_tag(tag, "ul")

            name = scraper_lib.Element(block=episode_wrapper, el_tag='li',
                el_class="episode_link", get_text=True)
            
            url = scraper_lib.Element(block=episode_wrapper, el_tag='a',
                el_class="myBtn", el_property="data-link")
            try:
                episode_name = name.get_element()
                episode_url = url.get_element()
                episode_urls.append(episode_url)

                #other links
                others_url = scraper_lib.get_hrefs(block=tag, filters=self.streaming_to_scrape)
                episode_urls = episode_urls + others_url
            except:
                episode_name = "nd"
        else:
            #old version
            try:
                soup = scraper_lib.get_soup(tag)
                episode_name = scraper_lib.get_previous_sibling(block=soup, tag='a')
                episode_name = self.replace_chars(episode_name)

                episode_urls = scraper_lib.get_hrefs(block=soup, filters=self.streaming_to_scrape)
            except:
                episode_name = "nd"

        episode = Episode(title=episode_name, urls=episode_urls, episode_no=episode_number)
        return episode

    def get_all_seasons(self):
        if sys.version_info[0] < 3:
            del self.seasons_lst[:]
        else:
            self.seasons_lst.clear()

        if self.is_modern_state:
            season_container = scraper_lib.Container(block=self.seasons_wrapper,
                tag='div', container_class='accordion-item')

            title = scraper_lib.Element(block='', el_tag='ul', get_text=True)
        else:
            #old version
            season_container = scraper_lib.Container(block=self.seasons_wrapper,
                tag='p', text=True, recursive=False)

            title = scraper_lib.Element(block='', el_tag='span', get_text=True)

        seasons_block = season_container.get_container()

        for i, season_block in enumerate(seasons_block):
            title.block = season_block
            season_title = title.get_element()
            season = Season(title=season_title, season_no=i)
            self.seasons_lst.append(season)
        
        return self.seasons_lst

    def get_seasons_wrapper(self):
        #return the html tag which cointains all the seasons
        seasons_wrapper = scraper_lib.Container(block=self.soup, tag='div', first=True,
                container_class='seasons-wraper').get_container()

        if seasons_wrapper is not None:
            return seasons_wrapper
        else:
            self.is_modern_state = False

            container = scraper_lib.Container(block=self.soup, tag='div',
                    container_id='info', container_class='pad').get_container()

            return container[-1]
    
    def get_all_episodes(self, episode_wrapper):
        episodes = []
        if self.is_modern_state:

            episodes_wrapper = scraper_lib.Container(block=episode_wrapper, tag='div',
                    container_class='episode-wrap').get_container()
                            
            for i, episode in enumerate(episodes_wrapper):
                episodes.append(self.get_episode_info(episode, i))
        else:
            #old version
            episodes_html = "{0}".format(episode_wrapper).split("<br/>")

            for i, episode in enumerate(episodes_html):
                episodes.append(self.get_episode_info(episode.strip(), i))

        return episodes

    def get_episodes_by_season_number(self, season_no):
        #return all episodes of that season
        self.get_all_seasons()
        if len(self.seasons_lst) > 0:
            try:
                season_obj = self.seasons_lst[season_no]
            except IndexError:
                season_obj = self.seasons_lst[-1]

            if self.is_modern_state:
                #new version config
                seasons = scraper_lib.Container(self.seasons_wrapper, tag='div',
                    container_class='accordion-item').get_container()
                
                s_title = scraper_lib.Element(block='', el_tag='ul',
                    get_text=True)

                season_content = scraper_lib.Container(block='', tag='div', first=True,
                        container_class='content')    
            else:
                #old version config
                seasons = scraper_lib.Container(self.seasons_wrapper, tag='p',
                    recursive=False).get_container()

                s_title = scraper_lib.Element(block='', el_tag='span',
                    get_text=True)
            
            for season in seasons:
                try:
                    s_title.block = season
                    title = s_title.get_element()
                except:
                    title = "nd"

                if title == season_obj.title:
                    if not self.is_modern_state:
                        content = scraper_lib.get_next_sibling(season)
                    else:
                        season_content.block = season
                        content = season_content.get_container()

                    all_episodes = self.get_all_episodes(content)
                    return all_episodes
        return None