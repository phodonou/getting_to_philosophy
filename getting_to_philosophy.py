import sys
import requests
from bs4 import BeautifulSoup

MAX_HOPS = 100

def get_first_link(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    parser_output_el = soup.find('div', {'id': 'mw-content-text'}).find('div', {'class': 'mw-parser-output'})
    candidates = parser_output_el.findChildren("p", recursive=False)

    for candidate in candidates:
        link = candidate.findChild('a', attrs={'class': None}, recursive=False)
        if(link != None):
            return 'https://en.wikipedia.org' + link['href']

    return ''


def get_to_philosophy():
    url = sys.argv[1]
    hops = 0

    while url.lower() != 'https://en.wikipedia.org/wiki/philosophy' and hops < MAX_HOPS:
        url = get_first_link(url)
        print(url)
        hops +=1
    
    print(hops, " hops")

get_to_philosophy()