import telebot
from datetime import datetime
import random
import json

TOKEN = ""
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
    foods.append(message.text)

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

@bot.message_handler(commands=['export'])
def export_food_list(message):
    try:
        with open('food_list.json', 'w') as file:
            json.dump(foods, file, indent=4)
        bot.reply_to(message, "Food list has been successfully exported to food_list.json.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred while exporting the food list: {e}")

@bot.message_handler(commands=['import'])
def import_food_list(message):
    try:
        with open('food_list.json', 'r') as file:
            imported_foods = json.load(file)
            global foods
            foods = imported_foods
        bot.reply_to(message, "Food list has been successfully imported from food_list.json.")
    except FileNotFoundError:
        bot.reply_to(message, "No food_list.json file found. Please export a food list first.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred while importing the food list: {e}")


bot.infinity_polling()
