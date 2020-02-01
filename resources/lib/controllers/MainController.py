from resources.lib import kodiutilsitem
from resources.lib.helpers.common import common
from resources.lib.views import MovieView
from resources.lib.views import SelectWebsiteView
from resources.lib.streaming_hosts import speedvideo, openload
from resources.lib import kodiplayer

def select_website(title):
    websites = ["fpt", "hdcloud"]
    SelectWebsiteView.show_websites(websites, title)

def select_tv_from_website(title):
    websites = ["gs", "tvshow_fpt"]
    SelectWebsiteView.show_websites(websites, title)

def search_from_websites(keyword=None):
	if keyword is None:
		keyword = kodiutilsitem.user_input()
    
	select_website(keyword)

def search_tv_from_websites(keyword=None):
	if keyword is None:
		keyword = kodiutilsitem.user_input()
    
	select_tv_from_website(keyword)

def play(title, streaming_url):
    streaming_source_name = kodiutilsitem.get_streaming_source_name(streaming_url)

    if streaming_source_name == "speedvideo":
        playable_url = speedvideo.get_stream_url(streaming_url)
        if streaming_url != '' and streaming_url != '404':
            kodiplayer.play_video(playable_url)
        else:
            kodiplayer.play_video_with_resolver(streaming_url)
    else:
        kodiplayer.play_video_with_resolver(streaming_url)

def play_direct(title, streaming_url):
    streaming_source_name = kodiutilsitem.get_streaming_source_name(streaming_url)

    if streaming_source_name == "speedvideo":

        playable_url = speedvideo.get_stream_url(streaming_url)
        if streaming_url != '' and streaming_url != '404':
            kodiplayer.play_video(playable_url)
        else:
            kodiplayer.play_video_with_resolver(streaming_url)
    else:
        kodiplayer.play_video(streaming_url)

def get_json_movies():
    movies = common.load_movies_from_json()
    MovieView.show_jsons(movies)

   