from bs4 import BeautifulSoup
from urllib.request import urlopen

link = 'http://neumont.smartcatalogiq.com/2020-2021/Catalog/Academic-Calendar-2020-2021'

site = urlopen(link)

soup = BeautifulSoup(site, 'html.parser')

for tds in soup.find_all('div', {'class': {'combinedChild'}}):
    text = tds.text
    print(text)


data = open("example.txt", "w")
data.write(text)
data.close()