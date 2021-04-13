import requests
from bs4 import BeautifulSoup
URL = 'https://www.eatthis.com/best-foods-to-stop-hair-loss/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('p')

f = open("temp_text.txt", "w")


for i in results:
    #print(i.text)
    f.write(i.text)

f.close() 

