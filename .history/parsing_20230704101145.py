# '''Веб - скрейпинг'''
# # Это технология, получение данных с веб-страниц путем извлечение

# '''Парсинг -> анализ данных, автоматически сбор данных и их структурирование'''

# # requests -> отправляет запрос на сайт, в итоге получаем html код страницы

# # beatifulsoup4 -> помогает извлекать информацию из HTML.  Позваляет обращаться к определенным тегам и вытаскивать из них данных

# # lxml -> хорошо разбирается в html, выступает в роли парсера (анализирует, разбирает инфорамции на мелкие части для beutifulsoup4)


import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('data.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data ['image'], data['desctiption'], data['price']])


def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, "lxml")
    page_list = 
def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    # print(soup)
    product_list = soup.find('div', class_ = 'list-view').find_all('div', class_ = 'item')
    # print(product_list)
    for product in product_list:
        title = product.find('div', class_ = 'listbox_title').find('strong').text
        print(title)
#         image = 'https://www.kivano.kg' + product.find('img').get('src')
#         # print(image)
#         desc = product.find('div', class_='product_text').text.replace(title, '').strip()
#         # print(desc)
#         price = product.find('div', class_ = 'listbox_price').text.strip()
#         print(price)
#         product_dict = {
#             'title': title, 
#             'image': image, 
#             'desctiption': desc, 
#             'price': price
#         }
#         write_to_csv(product_dict)

def main():
 for i in range(1,190):
        notebook_url = 'https://www.kivano.kg/noutbuki?page=187'
        get_data(get_html(notebook_url))
        print(i)
    

with open('data.csv', 'w') as file:
    write_ = csv.writer(file)
    write_.writerow(['title     ', 'image     ', 'description     ','price     '])



main()

'''Таск 2'''
# from bs4 import BeautifulSoup 
# import requests 
# import csv 
# source = requests.get('http://www.example.com/').text 
# # print(source)

# my_page = BeautifulSoup(source, 'lxml') 
# print(my_page)
# # print('h1:', my_page.h1.text) 
# # print('p:', my_page.p.text) 
# # print('a:', my_page.a.get('href'))





# import requests
# from bs4 import BeautifulSoup

# # Отправляем GET-запрос к странице Википедии
# url = 'https://www.wikipedia.org/'
# response = requests.get(url)

# # Создаем объект BeautifulSoup для парсинга HTML-кода страницы
# soup = BeautifulSoup(response.text, 'html.parser')

# # Находим элемент с информацией о статьях на немецком языке
# deutsch_element = soup.find('a', href='/wiki/Deutsch')

# # Переходим на страницу со статистикой на немецком языке
# deutsch_url = 'https://www.wikipedia.org' + deutsch_element['href']
# deutsch_response = requests.get(deutsch_url)
# deutsch_soup = BeautifulSoup(deutsch_response.text, 'html.parser')

# # Находим элемент с количеством статей
# article_element = deutsch_soup.find('div', class_='central-textlogo__image')

# # Получаем текст из элемента и выводим его в консоль
# print(article_element.text.strip())




