'''Веб - скрейпинг'''
# Это технология, получение данных с веб-страниц путем извлечение

'''Парсинг -> анализ данных, автоматически сбор данных и их структурирование'''

# requests -> отправляет запрос на сайт, в итоге получаем html код страницы

# beatifulsoup4 -> помогает извлекать информацию из HTML.  Позваляет обращаться к определенным тегам и вытаскивать из них данных

# lxml -> хорошо разбирается в html, выступает в роли парсера (анализирует, разбирает инфорамции на мелкие части для beutifulsoup4)


import requests
from bs4 import BeautifulSoup
import csv



def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['image'], data['description'], data['price']])



def get_html(url):
    response = requests.get(url)
    return response.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div', class_ = 'pager-wrap').find_all('li')
    last_page = page_list[-1].text
    return int(last_page)



# get_total_pages(get_html('https://www.kivano.kg/noutbuki'))



def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    # print(soup)
    product_list = soup.find('div', class_ = 'list-view').find_all('div', class_ = 'item')
    # print(product_list)
    for product in product_list:
        title = product.find('div', class_ = 'listbox_title').find('strong').text
        # print(title)
        image = 'https://www.kivano.kg' + product.find('img').get('src')
        # print(image)
        desc = product.find('div', class_='product_text').text.replace(title, '').strip()
        # print(desc)
        price = product.find('div', class_ = 'listbox_price text-center').text.strip()
        # print(prise)

        product_dict = {
            'title': title, 
            'image': image, 
            'description': desc, 
            'price': price
        }
        write_to_csv(product_dict)



def main():
    notebook_url = 'https://www.kivano.kg/noutbuki'
    html = get_html(notebook_url)
    get_data(html)
    number = get_total_pages(html)
    for i in range(2, number+1):
        url_with_page = notebook_url + '?page=' +str(i)
        html = get_html(url_with_page)
        get_data(html)



with open('data.csv', 'w') as file:
    write_ = csv.writer(file)
    write_.writerow(['title     ', 'image     ', 'description     ','price     '])



main()