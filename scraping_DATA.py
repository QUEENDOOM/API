from email import header
from webbrowser import Mozilla
import bs4
import json
import requests

#ค้นหาเช่าคอนโด ภายในกรุงเทพ
page=1
ฐานข้อมูล = ""
dict_place = {}
while page <= 4:
    url = 'https://th.zmyhome.com/search/result?id=1&type=Province&lat=&lng=&sort=distance&distance=1000&keyword=%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3&typePost%5B0%5D=5&typeProperty%5B0%5D=1&minPrice=&maxPrice=&transportDistance=&area=&age=&page='+str(page)+'&per-page=34'
    data = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'})
    soup = bs4.BeautifulSoup(data.text,'html.parser')
    place_data = soup.find_all('article', {'class': 'card-property__item--article'})
    for i in place_data :
        name = i.find('li',{'class':'name'}).text.rstrip().replace('\n','').lstrip()
        dict_place["รายละเอียดโครงการ"] = name
        location = i.find('li',{'class':'location'}).text.rstrip().replace('\n','').lstrip()
        dict_place["ตำแหน่งที่ตั้ง"] = location
        price = i.find('li',{'class':'card-property__price-room--priceRoom'}).text.split()[0].replace('\n','').replace(',','')
        dict_place["ราคา"] = price
        url_list = i.find("a",{'target':'_blank'}).get('href').rstrip().replace(" ","")
        dict_place["url"]= 'https://th.zmyhome.com'+url_list
        ฐานข้อมูล += str(dict_place)
        ฐานข้อมูล += "\n"
        dict_place.clear()
    print('เก็บข้อมูลถึงหน้าที่:',page)    
    page += 1 

print(ฐานข้อมูล)
