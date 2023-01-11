import sqlite3, requests

# from ..Fetch.views import fetch_using_url
from time import sleep
from datetime import datetime
db = r"C:\Users\srini\OneDrive\Desktop\Demo\DataStore\db.sqlite3"
def fetch_using_url(url):
    response = requests.get(url).text
    desc = response.split("<title>")[1].split("</title>")[0]
    price = response.split(">₹")[1].split("<")[0].replace(",","")
    return {'url': url, 'desc': desc, 'price': price, 'created_on': datetime.now()}

while True:
    con = sqlite3.connect(db)
    cur = con.cursor()
    urls = cur.execute("SELECT distinct url FROM Fetch_pagedata where created_on > datetime('now' , '-7 days')")
    urls = urls.fetchall()
    for url in urls:
        url = url[0]
        d = fetch_using_url(url)
        query = "insert into Fetch_pagedata (url, desc, price, created_on) values ('{url}', '{desc}', {price}, '{created_on}')".format(**d)
        print(query)
        cur.execute(query)
    con.commit()
    cur.close()
    con.close()
    sleep(5)
