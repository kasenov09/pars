import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars_list = soup.find('div', class_ = 'catalog-list').find_all('a')
    
    for car in cars_list[:20]:
        try:
            title = car.find('span', class_ = 'catalog-item-caption').text.strip()
        except:
            title = 'у этого объекта нет название'
        # print(title)

        try:
            price = car.find('span', class_ = 'catalog-item-price').text

        except:
            price = ''
        # print(price) 

        try:
            image = car.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            image = ''
        # print(image)
        try:
            desc = car.find('span', class_ = 'catalog-item-descr').text.split()
            desc = ' '.join(desc)
        except:
            desc = ''
        print(desc)
        try:
            r = car.find('span', class_ = 'catalog-item-mileage').text
        except:
            r = ''
        data = {
            'title':title,
            'image': image
        }
        
def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    get_data(html)
main()