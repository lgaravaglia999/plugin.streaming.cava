import urlparse
import urlresolver
import sys
from urllib import urlencode
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import sys

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
STREAMING_SOURCES = ["speedvideo", "openload", "rapidcrypt", "vcrypt"]

def build_url(query):
    return '{0}?{1}'.format(base_url, urlencode(query))

def add_menu_item(url_dict, item_title, image=None):
    url = build_url(url_dict)
    if image is not None:
        li = xbmcgui.ListItem(item_title, iconImage=image)
    else:
        li = xbmcgui.ListItem(item_title)

    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                        listitem=li, isFolder=True)

def add_item(url_dict, title, is_folder=False, properties=None, info=None, arts=None):
        url = build_url(url_dict)

        kodi_item = xbmcgui.ListItem(title)
        if arts is not None:
            kodi_item.setArt(arts)
        if info is not None:
            kodi_item.setInfo('video', info)
        else:
            kodi_item.setInfo('video', {})
        if properties is not None:
            prop_key = properties["prop_key"]
            prop_value = properties["prop_value"]
            kodi_item.setProperty(prop_key, prop_value)

        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                            listitem=kodi_item, isFolder=is_folder)

def end_directory():
        xbmcplugin.endOfDirectory(addon_handle)

def get_streaming_source_name(url):
    for source in STREAMING_SOURCES:
        if source in url:
            return source
    return "n.d."

def user_input():
    kb = xbmc.Keyboard('default', 'heading')
    kb.setDefault('')
    kb.setHeading('CercaFilm')
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        search_term = kb.getText()
        return search_term
    else:
        return None
