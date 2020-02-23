from resources.lib.controllers import GuardaserieController
from websites_config import WebsitesConfig as cfg

#base_path = "gs"
base_path = cfg.get_path(cfg.GUARDASERIE)

URLS = [
    {base_path: GuardaserieController.gs_tvshow_list},
    {"{0}/selected_tvshow".format(base_path): GuardaserieController.gs_seasons},
    {"{0}/selected_season".format(base_path): GuardaserieController.gs_episodes},
    {"{0}/selected_episode".format(base_path): GuardaserieController.gs_playable_url}
]