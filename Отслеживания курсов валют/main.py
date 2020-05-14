import requests
from bs4 import BeautifulSoup

DOLLAR_CHK = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%BA%D1%80%D0%BE%D0%BD%D0%B5&rlz=1C1SQJL_ruUA829UA829&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%BA%D1%80%D0%BE%D0%BD%D0%B5&aqs=chrome..69i57j0l7.2758j0j9&sourceid=chrome&ie=UTF-8'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

full_page = requests.get(DOLLAR_CHK, headers=headers)
#print(full_page.content)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

print(convert[0].text)
