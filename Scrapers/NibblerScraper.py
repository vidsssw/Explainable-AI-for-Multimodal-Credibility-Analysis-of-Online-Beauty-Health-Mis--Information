import requests,csv
from bs4 import BeautifulSoup
import time

import re
import pandas as pd
links = []
my_csv = pd.read_csv("test.csv")
links = my_csv['Blog']

f = open('sample.csv', 'w', newline='') 
fieldnames = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
writer = csv.DictWriter(f, fieldnames=fieldnames)

writer.writeheader()

postHeaders = {
    'Host': 'nibbler.silktide.com',
    'Connection': 'keep-alive',
'Content-Length': '41',
'Cache-Control': 'max-age=0',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
'sec-ch-ua-mobile': '?0',
'Upgrade-Insecure-Requests': '1',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Origin': 'https://nibbler.silktide.com',
    'Referer': 'https://nibbler.silktide.com/en_US',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'time_zone_offset=-330; time_zone_dst=0; time_zone_offset=-330; time_zone_dst=0; _ga=GA1.2.1862016562.1611567082; intercom-id-fzbqnrme=c13d99bb-1f9e-4acd-9f20-4bcae61d4c33; intercom-id-bc9h3qxr=99eb845d-eb67-4a8d-b1ef-d1874f7d376f; PHPSESSID=5a0029oa5lqq4tq1643n4arbm1; time_zone_offset=-330; time_zone_dst=0; _gid=GA1.2.1419393420.1619875906; _gat=1; _gat_UA-2673340-16=1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36'
}

'''
'Connection': keep-alive
Content-Length: 41
Cache-Control: max-age=0
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: https://nibbler.silktide.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://nibbler.silktide.com/en_US
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: time_zone_offset=-330; time_zone_dst=0; time_zone_offset=-330; time_zone_dst=0; _ga=GA1.2.1862016562.1611567082; intercom-id-fzbqnrme=c13d99bb-1f9e-4acd-9f20-4bcae61d4c33; intercom-id-bc9h3qxr=99eb845d-eb67-4a8d-b1ef-d1874f7d376f; PHPSESSID=5a0029oa5lqq4tq1643n4arbm1; time_zone_offset=-330; time_zone_dst=0; _gid=GA1.2.1419393420.1619875906; _gat=1; _gat_UA-2673340-16=1
'''
for i in links:
    i = i.replace("https://","")
    i = i.replace("http://","")
    print(i)
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
    
    #data = {'url':str(i)}
    #page = requests.post('https://nibbler.silktide.com/en_US/reports/submit', data = data,proxies=proxy,headers=postHeaders)
    #print(page)
    
    URL = 'https://nibbler.silktide.com/en_US/reports/'+i
    

    page = requests.get(URL,proxies=proxy,headers=postHeaders)
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
   
    results = {}
    results['1'] = soup.find(id='Nav_Test_Page_Links').text[-3:]
    
    results['2']=soup.find(id='Nav_Test_Page_Mobile').text[-3:]
    results['3']=soup.find(id='Nav_Test_Page_Headings').text[-3:]
    results['4']=soup.find(id='Nav_Test_Page_PageTitles').text[-3:]
    results['5']=soup.find(id='Nav_Test_Page_UrlFormat').text[-3:]
    results['6']=soup.find(id='Nav_Test_Page_AmountOfContent').text[-3:]
    results['7']=soup.find(id='Nav_Test_Site_Popularity').text[-3:]
    results['8']=soup.find(id='Nav_Test_Page_Freshness').text[-3:]
    results['9']=soup.find(id='Nav_Test_Page_TwitterAccount').text[-3:]
    results['10']=soup.find(id='Nav_Test_Page_Images').text[-3:]
    results['11']=soup.find(id='Nav_Test_Page_Printability').text[-3:]
    results['12']=soup.find(id='Nav_Test_Page_MetaTags').text[-3:]
    results['13']=soup.find(id='Nav_Test_Site_ServerBehaviour').text[-3:]
    results['14']=soup.find(id='Nav_Test_Page_Analytics').text[-3:]
    results['15']=soup.find(class_='summary-overall').text[7:10]

    writer.writerow(results)
 
        


