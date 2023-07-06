'''Веб - скрейпинг'''
# Это технология, получение данных с веб-страниц путем извлечение

'''Парсинг -> анализ данных, автоматически сбор данных и их структурирование'''

# requests -> отправляет запрос на сайт, в итоге получаем html код страницы

# beatifulsoup4 -> помогает извлекать информацию из HTML.  Позваляет обращаться к определенным тегам и вытаскивать из них данных

# lxml -> хорошо разбирается в html, выступает в роли парсера (анализирует, разбирает инфорамции на мелкие части для beutifulsoup4)


# import requests
# from bs4 import BeautifulSoup
# import csv



# def write_to_csv(data):
#     with open('data.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'], data['image'], data['description'], data['price']])



# def get_html(url):
#     response = requests.get(url)
#     return response.text


# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     page_list = soup.find('div', class_ = 'pager-wrap').find_all('li')
#     last_page = page_list[-1].text
#     return int(last_page)



# # get_total_pages(get_html('https://www.kivano.kg/noutbuki'))



# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     # print(soup)
#     product_list = soup.find('div', class_ = 'list-view').find_all('div', class_ = 'item')
#     # print(product_list)
#     for product in product_list:
#         title = product.find('div', class_ = 'listbox_title').find('strong').text
#         # print(title)
#         image = 'https://www.kivano.kg' + product.find('img').get('src')
#         # print(image)
#         desc = product.find('div', class_='product_text').text.replace(title, '').strip()
#         # print(desc)
#         price = product.find('div', class_ = 'listbox_price text-center').text.strip()
#         # print(prise)

#         product_dict = {
#             'title': title, 
#             'image': image, 
#             'description': desc, 
#             'price': price
#         }
#         write_to_csv(product_dict)



# def main():
#     notebook_url = 'https://www.kivano.kg/noutbuki'
#     html = get_html(notebook_url)
#     get_data(html)
#     number = get_total_pages(html)
#     for i in range(2, number+1):
#         url_with_page = notebook_url + '?page=' +str(i)
#         html = get_html(url_with_page)
#         get_data(html)



# with open('data.csv', 'w') as file:
#     write_ = csv.writer(file)
#     write_.writerow(['title     ', 'image     ', 'description     ','price     '])



# main()


import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('ul', class_ = 'pagination').find_all('a')
    last_page = page_list[-1].attrs.get('data-page')
    return int(last_page)   

def write_to_csv(data):
    with open('sedan.csv', "a") as file:
        write = csv.writer(file)
        write.writerow([data['title'], 
                        data['info'], 
                        data['img'],
                        data['price_som'],
                        data['price_doll']])

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    cars_list = soup.find('div', class_= "table-view-list").find_all('div', class_='list-item')
    for car in cars_list[:5]:
        try:
            title = car.find('div', class_= 'block title').text.strip()
        except AttributeError:
            title = ''
        # print(title)
        try:
            price_doll = car.find('div', class_= 'block price').find('strong').text.split()
            price_doll = ''.join(price_doll)
            price_som = car.find('div', class_= 'block price').text.split()
            price_som = ''.join(price_som)
        except:
            price_som = ''
            price_doll = ''
        # print(price_som.replace(price_doll, ''))
        # print(price_doll)
        try:
            img = car.find('img').attrs.get('data-src')
        except:
            img = ''
        # print(img)
        try:
            info = car.find('div', class_= 'block info-wrapper item-info-wrapper').text.split()
            info = ''.join(info)
        except:
            info = ''
        # print(info)
        data = {
            "title": title,
            'info': info,
            'img': img,
            'price_som': price_som.replace(price_doll,""),
            "price_doll": price_doll
        }
        write_to_csv(data)


def main():
    url = "https://www.mashina.kg/search/all/"
    html = get_html(url)
    get_data(html)
    number = get_pages(html)
    for i in range(2, number+1):
         url_with_page = url + '?page=' + str(i)
         html = get_html(url_with_page)
         get_data(html)

with open('sedan.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title', 'info', 'img', 'price_som', 'price_doll'])

main()