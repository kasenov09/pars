import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url):
    return response
def main():
    url = 'https://cars.kg/offers'
    html = 