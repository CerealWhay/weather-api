from rest_framework import viewsets
from rest_framework.response import Response
from .models import Description
from rest_framework.decorators import action
import requests
from bs4 import BeautifulSoup


def parse(city):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 " \
                 "Safari/537.36 "
    LANGUAGE = "ru-RU,ru;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    # city = city.replace(' ', '+')
    # content = f"https://www.google.com/search?q=погода+{city}"
    content = f"https://www.google.com/search?q=погода+хабаровск"

    parse_data = session.get(content)
    return parse_data.text


class DescriptionViewSet(viewsets.ViewSet):
    queryset = Description.objects.all()

    @action(methods=('get',), detail=False)
    def resp(self, city_from_front):
        data = parse(city_from_front)

        soup = BeautifulSoup(data, 'html.parser')

        temperature = soup.find('span', attrs={'id': 'wob_tm'}).text
        weather_desc = soup.find('span', attrs={'id': 'wob_dc'}).text
        probOfPrecip = soup.find('span', attrs={'id': 'wob_pp'}).text
        wind = soup.find('span', attrs={'id': 'wob_tws'}).text
        wet = soup.find('span', attrs={'id': 'wob_hm'}).text
        time = soup.find('div', attrs={'id': 'wob_dts'}).text

        dict = {
            'temperature': temperature,
            'weather_desc': weather_desc,
            'probOfPrecip': probOfPrecip,
            'wind': wind,
            'wet': wet,
            'time': time,
        }

        return Response(dict)
