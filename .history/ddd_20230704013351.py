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

import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к странице Википедии
url = 'https://www.wikipedia.org/'
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все заголовки статей на странице


# Выводим найденные заголовки
for title in article_titles:
    try:
        article_titles = soup.find_all('h1')
    print(title.text.strip())
    except Exception as e: 
    print('Title could not be found')

