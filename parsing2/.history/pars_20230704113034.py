import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars_list = soup.find('div', class_ = 'catalog-list').find_all('a')
    русской печати

def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    get_data(html)
main()