# '''Веб - скрейпинг'''
# # Это технология, получение данных с веб-страниц путем извлечение

# '''Парсинг -> анализ данных, автоматически сбор данных и их структурирование'''

# # requests -> отправляет запрос на сайт, в итоге получаем html код страницы

# # beatifulsoup4 -> помогает извлекать информацию из HTML.  Позваляет обращаться к определенным тегам и вытаскивать из них данных

# # lxml -> хорошо разбирается в html, выступает в роли парсера (анализирует, разбирает инфорамции на мелкие части для beutifulsoup4)


data.csv
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




