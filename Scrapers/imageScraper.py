import csv
import re
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from pandas.core.indexes import base
from shutil import copyfileobj
import os
import PIL
from PIL import Image
import base64

links = []
my_csv = pd.read_csv("test.csv")
links = my_csv['Blog']


for (i,base_url) in enumerate(links):
    print(base_url)
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
    
   

    page = requests.get(base_url,proxies=proxy)
    
    soup = BeautifulSoup(page.content, 'html.parser')
   
    images = soup.findAll('img')
    
    for j in images:
        if j.attrs["src"]:
            url_ext = j.attrs['src']
        else:
            url_ext = j.attrs['data-src']
        url_ext= url_ext.replace("https://","")
        print(url_ext)
        full_url = base_url + url_ext
        r = requests.get(full_url, stream=True)
        q = requests.get("https:"+url_ext,stream=True)
        filename = os.path.join("images","image"+str(i)+".jpg")
        print(filename)
        if r.status_code == 200:                     #200 status code = OK
            with open(filename, 'wb') as f: 
                print(f)
                r.raw.decode_content = True
                copyfileobj(r.raw, f)
                try:
                    im = Image.open(f)
                    im.verify()
                    im.close()
                except Exception as e:
                    print("block 1",e)
                    continue
                else:
                    break

        elif q.status_code == 200:                     #200 status code = OK
            with open(filename, 'wb') as f: 
                print(f)
                q.raw.decode_content = True
                copyfileobj(q.raw, f)
                try:
                    im = Image.open(f)
                    im.verify()
                    im.close()
                except Exception as e:
                    print("block 2",e)
                    continue 
                else:
                    break      
     
               
        



 
        


