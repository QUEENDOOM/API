#Dotproperty - Bangkok - rent
import datetime
import bs4
import requests
import time
import mysql.connector
#max page = 229
page = 1
url = 'https://th.zmyhome.com/search/result?id=1&type=Province&lat=&lng=&sort=distance&distance=1000&keyword=%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3&typePost%5B0%5D=5&typeProperty%5B0%5D=1&minPrice=&maxPrice=&transportDistance=&area=&age=&page='+str(page)+'&per-page=34'
name_list = []
price_list = []
location_list = []
url_list = []
while page <= 50 :
      url = 'https://th.zmyhome.com/search/result?id=1&type=Province&lat=&lng=&sort=distance&distance=1000&keyword=%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3&typePost%5B0%5D=5&typeProperty%5B0%5D=1&minPrice=&maxPrice=&transportDistance=&area=&age=&page='+str(page)+'&per-page=34'
      data = requests.get(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36'})
      data.encoding = "utf-8"
      data_get = bs4.BeautifulSoup(data.text, 'html.parser')
      place_data = data_get.find_all('article', {'class': 'card-property__item--article'})
      dict_place = {}
      storage = ""
      for i in place_data:
            name = i.find('li',{'class':'name'}).text.rstrip().replace('\n','').lstrip()
            name_list.append(name)
            price = i.find('li',{'class':'card-property__price-room--priceRoom'}).text.split()[0].replace('\n','').replace(',','')
            price_list.append(price)
            location = i.find('li',{'class':'location'}).text.rstrip().replace('\n','').lstrip()
            location_list.append(location)
            url = i.find("a",{'target':'_blank'}).get('href').rstrip().replace(" ","")
            url_list.append('https://th.zmyhome.com'+url)

      print("==========PAGE "+str(page)+" already==========")
      page += 1

item_count = len(name_list)

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    db = "scraping_data"
)

cursorpy = con.cursor()
for i in range(item_count) :
    date_now = datetime.datetime.now()
    query = "INSERT INTO condo (Name,Price,Location,Url,DateAdd) VALUES (%s , %s , %s ,%s, %s)"
    vaule = (name_list[i],int(price_list[i]),location_list[i],url_list[i],date_now)
    cursorpy.execute(query , vaule)

con.commit()
print(cursorpy)

#ลบข้อมูลที่ scraped เพื่อทำใหม่
#ทำ web เรียกดู
#DELETE FROM condo WHERE 1