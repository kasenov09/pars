'''Работает таск номер 3'''
import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к странице Википедии
url = 'https://www.wikipedia.org/'
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ссылки на языки в блоке "Языки"
languages = soup.find('div', class_='central-featured-lang lang5').find_all('a')

# Перебираем найденные ссылки
for language in languages:
    language_name = languages.text.strip()  
print(language_name)




