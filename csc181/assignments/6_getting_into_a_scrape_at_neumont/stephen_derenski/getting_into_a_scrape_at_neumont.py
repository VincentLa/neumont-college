from urllib.request import urlopen, Request
import os
import ipdb
from bs4 import BeautifulSoup
from datetime import date, datetime

TODAY = date.today()

dir_path = os.path.dirname(os.path.realpath(__file__))

FILENAME = os.path.join(dir_path, "scrape_results.txt")

def writingToFile(a):
    file_exists = os.path.exists(FILENAME)
    if file_exists:
        with open(FILENAME, 'a') as file:
            file.write("\n" + a)
    else:
        with open(FILENAME, 'w') as file:
            file.write(a)


url = 'http://neumont.smartcatalogiq.com/2021-2022/Catalog/Academic-Calendar-2021-2022'
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

combinedTables = soup.find('div', {'class': {'combinedChild'}})
theTables = combinedTables.find_all('table')
for table in theTables:
    contents = ''
    # Getting the caption for the date
    term = table.find('caption').contents[0]
    termYear = term.split(" ")
    the_body = table.find('tbody')

    the_trs = the_body.find_all('tr')

    for tr in the_trs:
        dateAfter = True
        the_tds = tr.find_all('td')

        contents = term
        tdCounter = 0
        for td in the_tds:
            # ipdb.set_trace()
            if tdCounter == 0:
                dateCal = td.contents[0].split(" ")
                dateCal = td.contents[0].split("-")
                dateCal = " ".join(dateCal[0].split())
                termYear[2].strip()
                dateCal = dateCal + " " + termYear[2]
                if datetime.date(datetime.strptime(dateCal, "%b %d %Y")) < TODAY:
                    dateAfter = False
                    contents = ""
                    tdCounter += 1
                else:
                    dateAfter = True
                    contents += " " + str(td.contents[0])
                    tdCounter += 1
            else:
                if dateAfter == True:
                    # ipdb.set_trace()
                    contents += " " + str(td.contents[0])
                    writingToFile(contents)
                    tdCounter += 1

print("Finished Writing!")
