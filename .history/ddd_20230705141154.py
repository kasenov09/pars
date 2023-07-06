'''Работает таск номер 3'''
# import requests
# from bs4 import BeautifulSoup

# # Отправляем GET-запрос к странице Википедии
# url = 'https://www.wikipedia.org/'
# response = requests.get(url)

# # Создаем объект BeautifulSoup для парсинга HTML-кода страницы
# soup = BeautifulSoup(response.text, 'html.parser')

# # Находим все ссылки на языки в блоке "Языки"
# languages = soup.find('div', class_='central-featured-lang lang5').find_all('a')

# # Перебираем найденные ссылки
# for language in languages:
#     language_name = languages.text.strip()  
# print(language_name)

# import requests
# from bs4 import BeautifulSoup

# # def getTitle(url):
# #  = 'https://www.wikipedia.org/'
# # response = requests.get(url)

# # Создаем объект BeautifulSoup для парсинга HTML-кода страницы
# soup = BeautifulSoup(response.text, 'html.parser')

# # Находим все заголовки статей на странице


# # Выводим найденные заголовки
# for title in soup.find_all('h1'):
#     try:
#         print(title.text.strip())
#     except Exception as e: 
#         print('Title could not be found')

# getTitle()





import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к странице Википедии
url = 'https://www.wikipedia.org/'
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ссылки на языки в блоке "Языки"
languages = soup.find('div', class_='central-featured-lang lang5').find('a')

# Перебираем найденные ссылки
for language in languages:
    language_name = languages.text.strip()  
print(language_name)


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


# from bs4 import BeautifulSoup
# import requests


# def get_description(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     description_element = soup.find('href', class_='catalog-list-item')  # Пример поиска по классу
#     if description_element:
#         description = description_element.text.strip()  # Получение текста элемента без лишних пробелов
#         return description
#     else:
#         return None

# # Пример использования функции для получения описания с указанной ссылки
# url = 'https://cars.kg/offers/119'  # Замените ссылку на нужную
# description = get_description(url)
# print(description)