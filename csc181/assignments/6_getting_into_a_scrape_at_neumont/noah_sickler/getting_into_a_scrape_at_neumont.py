import requests
from bs4 import BeautifulSoup
results = []

page = requests.get("http://neumont.smartcatalogiq.com/2021-2022/Catalog/Academic-Calendar-2021-2022")

soup = BeautifulSoup(page.content, 'html.parser')
trs = soup.find_all("tr")

with open ('scrape_result.txt', 'w', encoding='utf-8') as f:
    for tr1 in soup.find_all('tr')[0:]:
        tds = tr1.find_all('td')
        tds = tr1.text
        f.writelines(str(tds))
            

for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.text)
        


    


	    
    





