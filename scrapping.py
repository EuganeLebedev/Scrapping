from bs4 import BeautifulSoup
import requests
import time
import json

url = "https://catalog.onliner.by/robotcleaner/xiaomi/mirovamoprwhgl"
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

request_result = requests.get(url, headers=headers).text

soup = BeautifulSoup(request_result, "html5lib").findChildren("div", {"class": "offers-description__part offers-description__part_1"})
#print(price_data).findChildren("span", {"class": "helpers_show_tablet"})
subresult = soup[0].findChildren("div", {"class": "offers-description__price"})
price = (subresult[0].findChildren("span", {"class": "helpers_hide_tablet"}))
price_text = price[0].text


new_price=float(price_text.split(" ")[0].replace(",", "."))

old_price = 1000
if old_price <= new_price:
    print('Less')
else:
        print('Bigger')


with open("data.json") as file:
    config = json.load(file)