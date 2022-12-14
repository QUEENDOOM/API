# API
incluing :
- app.py
- myscraping.py
- /templates
  - index.html
  - response.html
 
 # introduction
- condos for rent in Bangkok only
- input range (scearch bar) : Name/Location/price/URL/DataAdd
- output : Name, Location, price, URL, DataAdd
- maximum data : 229 pages, testing : 50 pages

# reference
## app.py
ref : https://github.com/alexferl/flask-mysqldb

Database : XAMPP(MySQL)

## myscraping.py
url = 'https://th.zmyhome.com/search/result?id=1&type=Province&lat=&lng=&sort=distance&distance=1000&keyword=%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3&typePost%5B0%5D=5&typeProperty%5B0%5D=1&minPrice=&maxPrice=&transportDistance=&area=&age=&page='+str(page)+'&per-page=34'

## /template/index.html
link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"
script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js", "https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"
.CSS : background-image: url(https://c10.patreonusercontent.com/4/patreon-media/p/post/75467976/3b023cf60a3c404e91897e6480d9157a/eyJ3Ijo2MjB9/1.gif?token-time=1671580800&token-hash=IWfownqaqQ_SpXiQ9cnouQE1I5Q_9JxR9tGBHCEi3Qg%3D)



