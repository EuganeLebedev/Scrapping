from bs4 import BeautifulSoup
import requests
import time
import json


def set_config(filename="data.json"):
    with open("data.json") as file:
        config = json.load(file)

    config["old_price"] = float(config.get("old_price"))

    if config["old_price"] == None:
        config["old_price"] = 999999

    return config


def override_price(data, filename="data.json"):
    with open("data.json", "w") as file:
        json.dump(data, file)


def get_data_from_url():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

    config = set_config()
    url = config.get("url")
    old_price = config.get("old_price")

    request_result = requests.get(url, headers=headers).text

    soup = BeautifulSoup(request_result, "html5lib").findChild("div",
                                                                  {
                                                                      "class": "offers-description__part ",
                                                                      "class": "offers-description__part_1"})
    subresult = soup.findChild("div", {"class": "offers-description__price"})
    price = (subresult.findChild("span", {"class": "helpers_hide_tablet"}))
    price_text = price.text

    new_price = float(price_text.split(" ")[0].replace(",", "."))

    if old_price > new_price:
        config["old_price"] = new_price
        override_price(config)
        message = f"Цена уменьщилась {config['old_price']}"
    elif old_price == new_price:

        message = 'Цена не изменилась'
    else:

        config["old_price"] = new_price
        override_price(config)
        message = f"Цена увеличилась {config['old_price']}"

    return message


if __name__ == "__main__":
    get_data_from_url()
