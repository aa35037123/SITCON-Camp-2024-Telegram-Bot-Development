import telebot
from datetime import datetime
import json
# Replace with your actual bot token
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)
json_filename = f"accounting_data.json"

@bot.message_handler(commands=['test'])
def start(message):
    bot.send_poll(message.chat.id, 'chose', ['a', 'b'], is_anonymous = False)


@bot.poll_answer_handler(func=lambda call: True) #without lambda doesn't work too
def hadle_poll(call):
    print(call)

bot.infinity_polling()