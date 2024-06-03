import telebot
from datetime import datetime
import random

TOKEN = "6355462545:AAF7_X-9X3JQnfWp_kvpKQ3eqBmNwwsa8bc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


foods = []

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f"Hello, what do you want to eat today? \
                            \nUse /add to tell me your favorite food\
                            \nUse /list to see the whole food list\
                            \nI will help you decide what to eat Use /eat")

@bot.message_handler(commands=['add'])
def add_food(message):
    bot.reply_to(message, "Okay")
    foods.append(message.text[4:])

@bot.message_handler(commands=['list'])
def list_food(message):
    bot.reply_to(message, f"Here is the food list: {foods}")
    

@bot.message_handler(commands=['eat'])
def decide_food(message):
    if len(foods) == 0:
        bot.reply_to(message, "There is no food in the list")
    else:
        food = random.choice(foods)
        bot.reply_to(message, f"You should eat {food}")

bot.infinity_polling()

