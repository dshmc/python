import requests
from bs4 import BeautifulSoup
import time


class Currency:

    DOLLAR_CHK = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%BA%D1%80%D0%BE%D0%BD%D0%B5&rlz=1C1SQJL_ruUA829UA829&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%BA%D1%80%D0%BE%D0%BD%D0%B5&aqs=chrome..69i57j0l7.2758j0j9&sourceid=chrome&ie=UTF-8'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    current_converted_price = 0
    difference = 1

    def __init__(self):
        self.current_converted_price = float(self.get_curremcy_price().replace(",", "."))


    def get_curremcy_price(self):
        full_page = requests.get(self.DOLLAR_CHK, headers=self.headers)
        #print(full_page.content)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_curremcy_price().replace(",", "."))
        if currency >= self.current_converted_price + self.difference:
            print("The course has grown a lot.")
        elif currency<= self.current_converted_price - self.difference:
            print("The course has fallen.")
        print("Current rate: 1 dollar = "+str(currency) +" czech koruna.")
        time.sleep(3)
        self.check_currency()

currency = Currency()
currency.check_currency()
