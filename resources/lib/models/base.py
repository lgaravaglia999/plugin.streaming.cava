class Base(object):
    def __init__(self, title):
        self._title = title
        self._overview = ""
        self._image_url = ""
        self._release_date = 1900

    @property
    def title(self):
        return self._title

    @property
    def overview(self):
        return self._overview

    @property
    def image_url(self):
        return self._image_url

    @property
    def release_date(self):
        return self._release_date

    @title.setter
    def title(self, titl):
        self._title = titl

    @overview.setter
    def overview(self, ovrw):
        self._overview = ovrw

    @image_url.setter
    def image_url(self, img_url):
        self._image_url = img_url

    @release_date.setter
    def release_date(self, rls_date):
        self._release_date = rls_date