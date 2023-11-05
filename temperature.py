import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Temperature:
    """
    Represents the temperature obtained from site timeanddate.com/weather
    based on country and city.
    """

    some_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 
                'Accept-Language': 'ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7' }

    base_url =  'https://www.timeanddate.com/weather'

    def __init__(self, country, city):
        self.country = country.replace(' ', '-').lower()
        self.city = city.replace(' ', '-').lower()
 
    def _create_link(self):
        """
        Returns url for the country and city provided
        """
        return f'{self.base_url}/{self.country}/{self.city}'
    

    def _scrape(self):
        """
        Scrapes the above url to pick the temperature as a string
        """
        link = self._create_link()
        r = requests.get(link, headers=self.some_headers)
        soup = BeautifulSoup(r.text, 'lxml')
        raw_temperature = soup.find('div', class_='h2')
        return raw_temperature

    def get(self):
        """
        Converts the raw temperature data into integer
        """
        raw_temperature = self._scrape()
        int_temperature = int(raw_temperature.text.strip(' °C'))
        return int_temperature


