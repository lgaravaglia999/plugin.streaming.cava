from resources.lib import scraper_lib
import requests
import time
import base64

class HDLoad():
    def __init__(self, hdload_url):
        self.hdload_encoded_url = "https://nuovo.hdload.space/getHost/{0}?t={1}"
        self.player_url = 'https://hdpass.cloud/film.php'
        self.current_url = hdload_url
        self.hdpass_page = None
        self.embed_value_input_id = "urlEmbed"

    def get_all_players(self):
        self.hdpass_page = scraper_lib.get_page_soup(self.current_url)

        hosts = scraper_lib.Container(self.hdpass_page, 'div', container_class='hosts-bar',
            first=True).get_container()

        players = scraper_lib.Container(hosts, 'li').get_container()

        return [scraper_lib.get_text(player) for player in players]

    def decode_embed_values(self, embed_val):
        return base64.b64decode(embed_val).decode("utf-8")

    def get_embed_values_by_player(self, player_name):
        href = None
        if self.hdpass_page is None:
            self.hdpass_page = scraper_lib.get_page_soup(self.current_url)

        hosts = scraper_lib.Container(self.hdpass_page, 'div', container_class='hosts-bar',
            first=True).get_container()

        players = scraper_lib.Container(hosts, 'li').get_container()
        for player in players:
            if player_name == scraper_lib.get_text(player):
                a_href = scraper_lib.get_tag(player, 'a')
                href = a_href["href"].replace("amp;", "")
                break

        if href is not None:
            r = scraper_lib.get_page_soup(url=href)
            return scraper_lib.Element(r, 'iframe', el_property="custom-src").get_element()
        
        return None

    
    def get_final_url(self, player_name):
        embed_value = self.get_embed_values_by_player(player_name)
        decoded_url = self.decode_embed_values(embed_value)
        return decoded_url