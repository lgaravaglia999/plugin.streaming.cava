from resources.lib import kodiutilsitem
from resources.lib.router_urls.websites_config import WebsitesConfig as cfg

def show_websites(websites_cfg, movie_title):
    is_folder = True
    for website_cfg in websites_cfg:
        item_url = {
            'mode': cfg.get_path(website_cfg),
            '0': movie_title,
            }
        
        item_title =  cfg.get_name(website_cfg)
        
        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder)

    kodiutilsitem.end_directory()