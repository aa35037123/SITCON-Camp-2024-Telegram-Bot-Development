import telebot
from datetime import datetime
import random

TOKEN = "6355462545:AAF7_X-9X3JQnfWp_kvpKQ3eqBmNwwsa8bc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"It's a beautiful day outside. \
                        \nBirds are singing, flowers are blooming...")
    
bot.infinity_polling()




