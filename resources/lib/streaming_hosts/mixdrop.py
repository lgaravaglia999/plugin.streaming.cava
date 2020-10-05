import string
from resources.lib import scraper_lib
from resources.lib.thirdparty import jsunpack
import re
import json

class Mixdrop(object):
    def __init__(self, page):
        self.page = page        
        self.dictionaries = {}
        self.digs = string.digits + string.ascii_letters
        self.mixdrop_domain = "https://mixdrop.co"

    def base_10_to_N(self, x, base):
        if x < 0:
            sign = -1
        elif x == 0:
            return self.digs[0]
        else:
            sign = 1

        x *= sign
        digits = []

        while x:
            digits.append(self.digs[int(x % base)])
            x = int(x / base)

        if sign < 0:
            digits.append('-')

        digits.reverse()

        return ''.join(digits)

    def return_first_regroup(self, pattern, text):
        m = re.search(pattern, text)
        return m.group(1)

    def swap_values(self, e):
        return self.dictionaries[e.group(0)]

    def unpack(self, p, a, c, k, e, d):
        e = lambda c : self.base_10_to_N(c, 36)

        if not "".replace('/^/', ''):
            for i in range(c-1, -1, -1):
                d[self.base_10_to_N(i, a)] = k[i] if k[i] else self.base_10_to_N(i, a)
            k=[lambda e: d[e]]
            e = lambda i: '\\w+'
            i = 1
        c = i
        start = c if  c < 2 else c-1
        self.dictionaries = d

        for i in range(start, -1, -1):
            if len(k) > i and k[i](str(i)):
                p = re.sub(r"\b\w+\b", self.swap_values, p)
        return p

    
    def find_multiple_matches(self, text, pattern):
        return re.findall(pattern, text, re.DOTALL)
    
    def get_final_url(self):
        final_url = ""
        r = scraper_lib.get_page_soup(url=self.page)
        try:
            pattern = re.compile(r'window.location = "(.*?)";$', re.MULTILINE | re.DOTALL)
            script = r.find("script", text=pattern)
            window_location_value = pattern.search(script.text).group(1)
            r = scraper_lib.get_page_soup(url=self.mixdrop_domain + window_location_value)
        except:
            pass

        stream_url = self.return_first_regroup('\\s+?(eval\\(function\\(p,a,c,k,e,d\\).+)\\s+?', r.text)
        unpacked = jsunpack.unpack(stream_url)
        res = self.find_multiple_matches(unpacked, r'MDCore\.\w+\s*=\s*"([^"]+)"')
        for match in res:
            if '.mp' in match:
                final_url = "https:" + match
                break

        return final_url