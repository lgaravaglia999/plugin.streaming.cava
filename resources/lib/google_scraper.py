from resources.lib import scraper_lib

request_pattern = "http://www.google.com/search?q={0} inurl:{1}" # testo, url del sito di destinazione

def __get_request_url(search, destination_url):
    return request_pattern.format(search, destination_url)


def get_first_result(search_string, destination_url):
    soup = scraper_lib.get_page_soup(url=__get_request_url(search_string, destination_url))
    first_result = soup.find('div', class_='r')
    if (first_result):
        first_anchor = first_result.find('a')
        if first_anchor:
            return first_anchor["href"]
    return None

def get_results(search_string, destination_url):
    soup = scraper_lib.get_page_soup(url=__get_request_url(search_string, destination_url))
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    
    return results