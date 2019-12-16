from resources.lib.controllers import HDCloudController

base_path = "hdcloud"

URLS = [
    {"play_hd": HDCloudController.play_hd},
    {base_path: HDCloudController.show_movies},
    {"{0}/movies".format(base_path): HDCloudController.movie_streaming_options}
]