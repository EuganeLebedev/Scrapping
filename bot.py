import telebot
from scrapping import get_data_from_url
import time
import json


if __name__ == "__main__":
    while True:
        with open("settings.json") as file:
            settings = json.load(file)

        bot_token = settings.get("bot_token")
        channel = settings.get("channel")


        message = get_data_from_url()
        bot = telebot.TeleBot(bot_token)
        bot.send_message(channel, message)
        time.sleep(60*60*12)




