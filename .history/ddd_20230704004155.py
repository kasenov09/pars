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
# deutsch_url = 'https://www.wikipedia.org'
# deutsch_response = requests.get(deutsch_url)
# deutsch_soup = BeautifulSoup(deutsch_response.text, 'html.parser')

# # Находим элемент с количеством статей
# article_element = deutsch_soup.find('div', class_='central-textlogo__image')

# # Получаем текст из элемента и выводим его в консоль
# print(article_element.text.strip())

import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к странице Википедии
url = 'https://www.wikipedia.org/'
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ссылки на языки в блоке "Языки"
languages = soup.find('div', class_='central-featured-lang').find_all('a')

# Перебираем найденные ссылки
for language in languages:
    language_name = language.text.strip()  # Имя языка
    if language_name == 'Deutsch':
        article_count = language.find_next_sibling('strong').text.strip()  # Количество статей
        break

# Выводим информацию о статьях на немецком языке
print(language_name)
print(article_count)
