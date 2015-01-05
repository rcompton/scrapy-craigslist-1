"""
Craigslist-specific data
"""
import os
from bs4 import BeautifulSoup

try:
    from urllib import urlopen
except ImportError,e:
    raise
    from urllib.request import urlopen, URLError

SITES_URL = 'http://www.craigslist.org/about/sites'
subdomains = []
categories = []

def _get_html(url):
    """Utility function to fetch HTML from a given URL.
    """
    html = None
    tmpfile = 'craigslist.sites.html'
    """Cache the results if possible"""
    try:
        with open(tmpfile, 'r') as fd:
            html = fd.read()
        return html
    except IOError:
        pass

    try:
        html = urlopen(url).read()
        with open(tmpfile, 'w') as fd:
            fd.write(html)
    except (IOError, URLError):
        pass

    return html

def get_current_regions():
    """Returns a parsed dict of regions/states/cities from SITES_URL.
    """
    html = _get_html(SITES_URL)
    if html is None:
        raise ValueError("Can't find any HTML to parse!")

    soup = BeautifulSoup(html)
    countries = [tag.text.encode('UTF-8') for tag in soup.find_all('h1')]
    region_list = [tag for tag in soup.find_all('div', {'class': 'colmask'})]
    pairs = {country: divTag for (country, divTag) in zip(countries, region_list)}

    result = {}    
    for country in pairs:
        result[country] = {}
        region = pairs[country]
        """Region is a div containing the links, among other stuff.
        States are <h4> tags, followed by an <ul> with the city links.
        """
        states = [state.text.encode('UTF-8') for state in 
                  region.find_all('h4')]
        city_lists = [city for city in region.find_all('ul')]

        states_cities = {state: city_list for (state, city_list) in 
                         zip(states, city_lists)}

        for state in states_cities:
            city = states_cities[state]
            result[country][state] = {}
            cities = {a.text.encode('UTF-8'): a['href'] for a in 
                      city.find_all('a')}
            for city in cities:
                result[country][state][city] = cities[city]

    return result
            

if __name__ == "__main__":
    _all = get_current_regions()
    for country in _all:
        print(" [+] %s" % country)
        for state in _all[country]:
            print("     [+] %s" % state)
            for city in _all[country][state]:
                print("         [+] %s" % city)
                print("              (%s)" % _all[country][state][city])
