import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    response = requests.get(url)
    return response.text



def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['description'], data['mileage'], data['image']])

def get_description(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    description_element = soup.find('href', class_='catalog-list-item')  # Пример поиска по классу
    if description_element:
        description = description_element.text.strip()  # Получение текста элемента без лишних пробелов
        return description
    else:
        return None

# Пример использования функции для получения описания с указанной ссылки
url = 'https://cars.kg/offers/119'  # Замените ссылку на нужную
description = get_description(url)
print(description)

# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     cars_list = soup.find('div', class_ = 'catalog-list').find_all('a')
#     # print(cars_list[0].text)
    
#     for car in cars_list[:20]:
#         try:
#             title = car.find('span', class_ = 'catalog-item-caption').text.strip()
#         except AttributeError:
#             title = ''
#         # print(title)

#         try:
#             price = car.find('span', class_ = 'catalog-item-price').text
#         except:
#             price = ''
#         # print(price)

#         try:
#             image = car.find('img', class_ = 'catalog-item-cover-img').get('src')
#         except:
#             image = ''
#         # print(image)

#         try:
#             description = car.find('span', class_ = 'catalog-item-descr').text.split()
#             description = ' '.join(description)
#         except:
#             description = ''
#         # print(description)

#         try:
#             mileage = car.find('span', class_ = 'catalog-item-mileage').text
#         except:
#             mileage = ''
#         # print(mileage)



        data = {
            'title': title,
            'image': image,
            'description': description,
            'price': price,
            'mileage': mileage
        }
        write_to_csv(data)



def main():
    url = 'https://cars.kg/offers'
    html = get_html(url)
    get_data(html)




with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'price', 'description','mileage', 'image'])



main()