# This example show how to use inline keyboards and process button presses
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

TOKEN = "6355462545:AAF7_X-9X3JQnfWp_kvpKQ3eqBmNwwsa8bc"

bot = telebot.TeleBot(TOKEN)
bot_info = bot.get_me()  # Fetches the bot's information
bot_name = bot_info.first_name  # Gets the bot's first name


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('🐶', callback_data="cb_dog"),
                InlineKeyboardButton('🐱', callback_data="cb_cat"),
                InlineKeyboardButton('🐭', callback_data="cb_mouse"))
    return markup

@bot.message_handler(commands=['inline'])
def message_handler(message):
    bot.send_message(message.chat.id, "Let's play! It's your turn~", reply_markup=gen_markup())

bot.infinity_polling()