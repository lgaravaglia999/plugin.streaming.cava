import string
from resources.lib import scraper_lib
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
        try:
            m = re.search(pattern, text)
            return m.group(1)
        except:
            return 'n'

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
    
    def get_final_url(self):
        r = scraper_lib.get_page_soup(url=self.page)
        
        try:
            #nuovo metodo ancora in test
            pattern = re.compile(r'window.location = "(.*?)";$', re.MULTILINE | re.DOTALL)
            script = r.find("script", text=pattern)
            window_location_value = pattern.search(script.text).group(1)
            r = scraper_lib.get_page_soup(url=self.mixdrop_domain + window_location_value)
        except:
            pass

        stream_url = self.return_first_regroup('\\s+?(eval\\(function\\(p,a,c,k,e,d\\).+)\\s+?', r.text)
        parameters = stream_url.split('return p')[-1].replace("}(", "").replace("))", "").split(",")
        p, a, c, k, e, d = parameters

        #potrei usare eval es: p = eval(p)
        #ma e' pericoloso. potenzialmente potrebbero eseguire codice a loro piacere
        p = str(p)
        a = int(a)
        c = int(c)
        k = k.split(".split")[0].split("|")
        e = int(e)
        d = json.loads(d)
        unpacked = self.unpack(p, a, c, k, e, d)
        final_url = self.return_first_regroup('MDCore.wurl="(.*)";', unpacked).split('";')[0]
        return "https:" + final_url
