from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

def get_weather():

    url = 'https://weather.com/weather/today/l/30dc2d623ef5eebf53bc11940237593bcd782edb2db8b83ce5fc129e16f50ac4'

    request = Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0')

    page = urlopen(request)

    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    the_weathercard = soup.find('div', {'class': {'TodayWeatherCard--TableWrapper--13jpa'}}).contents[0]
    the_anchors = the_weathercard.find_all('a')

    weather_list = []

    for anchor in the_anchors:
        title = anchor.find('span', {'class': {'Ellipsis--ellipsis--lfjoB'}}).contents[0]

        tempurature = anchor.find('span', {'data-testid': {'TemperatureValue'}}).contents[0]
        
        
        precip = anchor.find('span', {'class': {'Column--precip--2H5Iw'}})

        precip_child = anchor.find('span', {'class': {'Accessibility--visuallyHidden--1432w'}})

        precip_chance = ''
        if precip_child != None:
            precip_chance = precip_child.contents[0]
            precip_child.decompose()

        precip = precip.contents[0]

        # print(title, tempurature, precip, precip_chance)
        weather_list.append(f"{title} {tempurature} {precip} {precip_chance}")
    
    return weather_list

if __name__ == '__main__':
    print(get_weather())


