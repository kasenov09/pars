import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars_list = soup.find()'div', calss_

def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)