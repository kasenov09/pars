# # import requests
# # from bs4 import BeautifulSoup
# # import csv



# # def get_html(url):
# #     response = requests.get(url)
# #     return response.text



# # def write_to_csv(data):
# #     with open('data.csv', 'a') as file:
# #         writer = csv.writer(file)
# #         writer.writerow([data['title'], data['price'], data['description'], data['mileage'], data['image']])
# #         last_page = writer[-1].text
# #         return (last_page)


# # def get_data(html):
# #     soup = BeautifulSoup(html, 'lxml')
# #     cars_list = soup.find('div', class_ = 'catalog-list').find_all('a')
# #     # print(cars_list[0].text)
    
# #     for car in cars_list[:20]:
# #         try:
# #             title = car.find('span', class_ = 'catalog-item-caption').text.strip()
# #         except AttributeError:
# #             title = ''
# #         # print(title)

# #         try:
# #             price = car.find('span', class_ = 'catalog-item-price').text
# #         except:
# #             price = ''
# #         # print(price)

# #         try:
# #             image = car.find('img', class_ = 'catalog-item-cover-img').get('src')
# #         except:
# #             image = ''
# #         # print(image)

# #         try:
# #             description = car.find('span', class_ = 'catalog-item-descr').text.split()
# #             description = ' '.join(description)
# #         except:
# #             description = ''
# #         # print(description)

# #         try:
# #             mileage = car.find('span', class_ = 'catalog-item-mileage').text
# #         except:
# #             mileage = ''
# #         # print(mileage)



# #         data = {
# #             'title': title,
# #             'image': image,
# #             'description': description,
# #             'price': price,
# #             'mileage': mileage
# #         }
# #         write_to_csv(data)



# # def main():
# #     url = 'https://cars.kg/offers'
# #     html = get_html(url)
# #     get_data(html)
# #     number = get_data(html)
# #     for i in range(number+1):
# #         url_with_page = url + '?page=' +str(i)
# #         html = get_html(url_with_page)
# #         get_data(html)




# # with open('data.csv', 'w') as file:
# #     writer = csv.writer(file)
# #     writer.writerow(['title', 'price', 'description','mileage', 'image'])



# # main()


# import requests
# from bs4 import BeautifulSoup
# import csv

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def write_to_csv(data):
#     with open('data.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'], data['price'], data['description'], data['mileage'], data['image']])

# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     cars_list = soup.find('div', class_='catalog-list').find_all('a')
    
#     for car in cars_list[:20]:
#         try:
#             title = car.find('span', class_='catalog-item-caption').text.strip()
#         except AttributeError:
#             title = ''

#         try:
#             price = car.find('span', class_='catalog-item-price').text
#         except:
#             price = ''

#         try:
#             image = car.find('img', class_='catalog-item-cover-img').get('src')
#         except:
#             image = ''

#         try:
#             description = car.find('span', class_='catalog-item-descr').text.split()
#             description = ' '.join(description)
#         except:
#             description = ''

#         try:
#             mileage = car.find('span', class_='catalog-item-mileage').text
#         except:
#             mileage = ''

#         data = {
#             'title': title,
#             'image': image,
#             'description': description,
#             'price': price,
#             'mileage': mileage
#         }
#         write_to_csv(data)

# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     page_list = soup.find('div', class_='pager-wrap').find_all('li')
#     last_page = page_list[-1].text
#     return int(last_page)

# def main():
#     url = 'https://cars.kg/offers'
#     html = get_html(url)
#     get_data(html)
#     number = get_total_pages(html)
#     for i in range(2, number + 1):
#         url_with_page = url + '?page=' + str(i)
#         html = get_html(url_with_page)
#         get_data(html)

# with open('data.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['title', 'price', 'description', 'mileage', 'image'])

# main()






import requests
from bs4 import BeautifulSoup as bs
import csv

def get_html(url):
  response=requests.get(url)
  return response.text

def main():
  url='https://vesti.kg/'
  html=get_html(url)
  print(total_page(html))
  get_data(html)

def write_to_csv(data_list):
    with open('news_kg.csv','w') as file:
        writer = csv.writer(file)
        for title in data_list:
          writer.writerow([title.text.strip()])

def get_data(html):
  soup=bs(html,'lxml')
  data_list=soup.find('div',class_='itemList').find_all('h2')
  last_page=soup.find()
  write_to_csv(data_list)

def total_page(html):
   soup=bs(html,'lxml')
   last_page=soup.find('li',class_='pagination-end').find('a',class_= 'pagenav').get('href').split('=')[-1]
   return last_page
for l in range():
   print(l)
main()