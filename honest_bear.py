import telebot
from datetime import datetime

TOKEN = "6355462545:AAF7_X-9X3JQnfWp_kvpKQ3eqBmNwwsa8bc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing?")

@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.reply_to(message, f"當前時間：{current_time}")
ㄋ
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "告訴老實說熊熊":
        bot.reply_to(message, "其實我不是人類，我是一台機器")
    else:
        bot.reply_to(message, message.text)

bot.infinity_polling()


TOKEN = "your_api_token_here"
bot = telebot.TeleBot(TOKEN, parse_mode=None)