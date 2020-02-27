from resources.lib.controllers import ItaliaserieOrgController
from websites_config import WebsitesConfig as cfg

base_path = cfg.get_path(cfg.ITALIASERIE_ORG)

URLS = [
    {base_path: ItaliaserieOrgController.tvshow_list},
    {"{0}/selected_tvshow".format(base_path): ItaliaserieOrgController.seasons},
    {"{0}/selected_season".format(base_path): ItaliaserieOrgController.episodes},
    {"{0}/selected_episode".format(base_path): ItaliaserieOrgController.playable_url}
]