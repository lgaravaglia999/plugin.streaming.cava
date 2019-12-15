from resources.lib import scraper_lib
import requests
import time
import base64

class HDLoad():
    def __init__(self, hdload_url):
        self.hdload_encoded_url = "https://nuovo.hdload.space/getHost/{0}?t={1}"
        self.player_url = 'https://hdpass.cloud/film.php'
        self.current_url = hdload_url
        self.embed_value_input_id = "urlEmbed"

    def get_players(self):
        return

    def decode_embed_values(self, embed_val):
        decoded_url = ""
        size = len(embed_val)
        if size % 2 == 0:
            half = int(size / 2)
            first_half = embed_val[0:half]
            second_half = embed_val[half:size]
            embed_val = second_half + first_half
            base = embed_val[::-1]
            decoded_url = base64.b64decode(base).decode("utf-8")
        else:
            last_char = embed_val[-1]
            embed_val[-1] = " "
            embed_val = embed_val.strip()
            new_size = len(embed_val)
            half = int(new_size / 2)
            first_half = embed_val[0:half]
            second_half = embed_val[half:size]
            embed_val = second_half + first_half
            base = embed_val[::-1]
            base = base + last_char
            decoded_url = base64.b64decode(base).decode("utf-8")
        return decoded_url

    def get_embed_values_by_player(self, player_name):

        input_value = '<input name="play_chosen" type="hidden" value="{0}"'.format(player_name)
        hdload_page = scraper_lib.get_page_soup(self.current_url)
        forms = scraper_lib.Container(hdload_page, 'form').get_container()
        for form in forms:
            if input_value in str(form):
                inputs = scraper_lib.Container(form, 'input').get_container()
                params = {}
                for inpt in inputs:
                    params[inpt["name"]] = inpt["value"]

        r = scraper_lib.get_page_soup(url=self.player_url, params=params)
        embed_url_value = scraper_lib.Element(r, el_tag="input", el_id=self.embed_value_input_id,
                el_property="value").get_element()       
        return embed_url_value
    
    def get_final_url(self, player_name):
        embed_value = self.get_embed_values_by_player(player_name)
        decoded_url = self.decode_embed_values(embed_value)
        return decoded_url