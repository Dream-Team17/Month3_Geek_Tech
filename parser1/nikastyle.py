import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://www.nikastyle.ru/poleznaya-informatsiya/tkani-i-materialy/"

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):

    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='fabrics_item')
    shop = []
    for item in items:
        shop.append({
            'title': item.find('span', class_="item_right_title").getText(),
            'img_url': item.find('img').get('src'),
            'description': item.find('span', class_="item_right_desc").getText(),
        })

    return shop

def parser_shop():
    html = get_html(URL)
    pars = get_data(html.text)
    return pars







