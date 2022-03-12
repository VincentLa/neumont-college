from urllib.request import urlopen, Request
import ssl
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()

url = 'http://neumont.smartcatalogiq.com/2021-2022/Catalog/Academic-Calendar-2021-2022'
page = urlopen(url, context=context)

soup = BeautifulSoup(page, 'html.parser')

the_tables = soup.find( {'class': {'main'}})

print(the_tables)

the_head = soup.find('thead')

the_body = the_tables.find('tbody')


the_trs = the_body.find_all('tr')

quarter_list = []
for tr in the_trs:
    # <td> tag defines standard data cell in an HTML table
    the_tds = tr.find_all('td')

    td_list = []
    for td in the_tds:
        # ipdb is an interactive debugger. Can comment out if you want the whole file to run
        # import ipdb; ipdb.set_trace()

        # <sup> tag defines superscript text
        # https://www.w3schools.com/tags/tag_sup.asp
        if td.find('sup'):
            the_sup = td.find('sup')
            the_sup.decompose()

        # <a> tag defines hyperlink
        if td.find('a'):
            contents = td.find('a').contents[0]
        elif td.find('span'):
            contents = td.find('span').contents[0]
        else:
            contents = td.contents[0]

        contents = str(contents)
        contents = contents.replace('\n', '')

        td_list.append(contents)

    if len(td_list) > 0:
        quarter_list.append(td_list)

# print(game_list)

file = open('scrape_result.txt', 'a')
file.write(quarter_list)
file.close

for quarter in quarter_list:
    for i, element in enumerate(quarter):
        if i < len(quarter) - 1:
            print(f"'{element}'", end=', ')
        else:
            print(f"'{element}'")