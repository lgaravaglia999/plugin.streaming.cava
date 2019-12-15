from resources.lib import kodiutilsitem

def show_websites(websites, movie_title):
    is_folder = True
    for website in websites:
        item_url = {
            'mode': website,
            '0': movie_title,
            }
        
        item_title = website
        
        kodiutilsitem.add_item(url_dict=item_url, title=item_title, is_folder=is_folder)

    kodiutilsitem.end_directory()