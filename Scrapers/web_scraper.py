import requests,csv
from bs4 import BeautifulSoup
import pandas as pd
links = []
my_csv = pd.read_csv("test.csv")
links = my_csv['Blog']
f = open('text_sample.csv', 'w', newline='',encoding='utf-8') 
fieldnames = ['Blog','Text']
writer = csv.DictWriter(f, fieldnames=fieldnames)

writer.writeheader()

proxy = {
    "http": "http://111.233.225.166:1234",
    "http": "http://252.144.107.56:1234",
"http":"http://171.32.34.13:1234",
"http":"http://150.13.9.131:1234",
"http":"http:/128.170.203.123:1234",
"http":"http:/146.130.167.8:1234",
"http":"http:/219.97.113.146:1234",
"http":"http:/232.92.177.67:1234",
"http":"http:/216.135.133.215:1234",
"http":"http:/35.183.240.38:1234",
"http":"http:/196.229.174.127:1234"
    }

for i in links:
    print(i)

    URL = i
    page = requests.get(URL,proxies=proxy)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('p')

    temp_text = ''
    for j in results:
        temp_text+=j.text

    writer.writerow({'Blog':i,'Text':temp_text})
    

