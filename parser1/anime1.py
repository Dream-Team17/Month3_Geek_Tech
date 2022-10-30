import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://rezka.ag/animation/"

HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req

def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_="b-content__inline_item")
    anime = []
    for item in items:
        info = item.find('div', class_="b-content__inline_item-link").find('div').getText().split(', ')
        anime.append({
            'title': item.find('div', class_="b-content__inline_item-link").find('a').getText(),
            'link': item.find('div', class_="b-content__inline_item-link").find('a').get('href'),
            'last': item.find('span', class_='info').getText()
            if item.find('span', class_='info') is not None else "Movie",
            'year': info[0],
            'country': info[1],
            'genre': info[2],
        })
    return anime

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f'{URL}page/{i}')
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception('Error in parser!')
