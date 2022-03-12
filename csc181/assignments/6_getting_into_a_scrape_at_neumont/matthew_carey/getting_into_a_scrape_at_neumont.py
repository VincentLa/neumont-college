import datetime

import requests
from bs4 import BeautifulSoup

url = "http://neumont.smartcatalogiq.com/2021-2022/Catalog/Academic-Calendar-2021-2022"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
tables = soup.find_all("table")
quarters = soup.find_all("caption")
events = soup.find_all("td")

for table in tables:
    quarter = table.find("caption")
    events = table.find_all("td")
    date = str(datetime.date.today())
    year = str(quarter.text)+" "
    for x in range(0, len(events),2):
        month = events[x].text[0:3]
        month_num = 0
        if int(year[-5:-1]) >= int(date[0:4]):
            file1 = open("scrape_results.txt", "a")
            log = (quarter.text+" "+events[x].text+" " + events[x+1].text)
            file1.write(log+"\n"*2)
            file1.close()
            print(quarter.text+" "+events[x].text+" " + events[x+1].text, end="\n"*2)


