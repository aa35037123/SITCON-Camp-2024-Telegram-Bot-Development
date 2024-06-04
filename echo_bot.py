import telebot
from datetime import datetime

TOKEN = "6355462545:AAF7_X-9X3JQnfWp_kvpKQ3eqBmNwwsa8bc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

print("It's a beautiful day outside. Birds are singing, flowers are blooming...")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "告訴老實說熊熊":
        bot.reply_to(message, "其實我不是人類，我是一台機器")
    else:
        bot.reply_to(message, message.text)

bot.infinity_polling()

