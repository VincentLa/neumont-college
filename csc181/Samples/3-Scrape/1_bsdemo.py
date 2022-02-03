from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

the_tables = soup.find('table', {'class': {'wikitable'}})
the_body = the_tables.find('tbody')
the_trs = the_body.find_all('tr')


game_list = []
for tr in the_trs:
    the_tds = tr.find_all('td') 

    td_list = []
    for td in the_tds:

        if td.find('sup'):
            the_sup = td.find('sup')
            the_sup.decompose()

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

