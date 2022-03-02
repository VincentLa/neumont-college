# Will require something like
# /Users/vincentla/.pyenv/versions/3.9.7/bin/python -m pip install bs4
# in terminal.
# Hopefully just pip install works for most users.
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

the_tables = soup.find('table', {'class': {'wikitable'}})

# <tbody> tag in HTML defines the Table Body conent
# https://www.w3schools.com/tags/tag_tbody.asp
the_body = the_tables.find('tbody')

# <tr> Tag in HTML defines the table row
# https://www.w3schools.com/tags/tag_tr.asp
the_trs = the_body.find_all('tr')

game_list = []
for tr in the_trs:
    # <td> tag defines standard data cell in an HTML table
    the_tds = tr.find_all('td') 

    td_list = []
    for td in the_tds:
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
        game_list.append(td_list)

# print(game_list)

for game in game_list:
    for i, element in enumerate(game):
        if i < len(game) - 1:
            print(f"'{element}'", end=', ')
        else:
            print(f"'{element}'")

