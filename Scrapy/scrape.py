from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh.html"
page = requests.get(url)
print(page)

with open('HCMC-Housing.csv', "w", encoding='UTF8', newline='') as f:
	thewriter =writer(f)
	header = ['roadWidth','floor','bedroom', 'parking','squareFeet','price','address' ]
	thewriter.writerow(header)

	while True:
	 soup = BeautifulSoup(page.content, 'html.parser')
	 lists = soup.find_all('div', class_='content-item')
	 try:
	  for list in lists:
	   roadWidth = list.find('span', class_='road-width').text
	   floor = list.find('span', class_='floors').text
	   bedroom = list.find('span', class_='bedroom').text
	   parking = list.find('span', class_='parking').text
	   squareFeet= list.find('div', class_='square-direct').text
	   price = list.find('div', class_='ct_price').text
	   address = list.find('div', class_='ct_dis').text
	   info = [roadWidth, floor, bedroom, parking, squareFeet, price, address ]
	   thewriter.writerow(header)
	 except:
	  break