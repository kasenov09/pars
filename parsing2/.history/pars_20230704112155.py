import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url):
    return response

def_get_data():
    soup = BeautifulSoup(html, '')
def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)