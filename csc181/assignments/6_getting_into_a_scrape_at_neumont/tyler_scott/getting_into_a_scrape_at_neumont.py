from urllib.request import urlopen, Request

from bs4 import BeautifulSoup 

import os

import ssl
file_path = os.path.dirname(os.path.realpath(__file__))
context = ssl._create_unverified_context()

url = 'http://neumont.smartcatalogiq.com/2021-2022/Catalog/Academic-Calendar-2021-2022'
page = urlopen(url, context=context)

soup = BeautifulSoup(page, 'html.parser')

the_tables = soup.find('table')


the_body = the_tables.find('tbody')
the_trs = the_body.find_all('tr')

game_list = []
for tr in the_trs:
    the_tds = tr.find_all('td')
    # print(the_tds)

    td_list = []
    for td in the_tds:
        
        if td.find('sup'):
            the_sup = td.find('sup')
            the_sup.decompose()

        if td.find('a'):
            contents = ''
            for c in td.find_all('a'):
                contents += " " + str(c.contents[0])
        elif td.find('span'):
            contents = td.find('span').contents[0]
        else:
            contents = td.contents[0]

        contents = str(contents)
        contents = contents.replace('\n', '')

        td_list.append(contents)
        # print(contents)

    if len(td_list) > 0:
        game_list.append(td_list)


# print(game_list)
for schedule in game_list:
    for i, element in enumerate(schedule):
        print(element)
        with open(os.path.join(file_path, "scrape_results.txt"), 'a') as f:
            if i < len(schedule) - 1:
                f.write(f"{element} " + ' | ')
            else:
                f.write(f"{element}")


