import telebot
from datetime import datetime
import random
import json

# TODO: 輸入自己 Bot 的 TOKEN
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)


foods = []

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f"Hello, what do you want to eat today? \
                            \nUse /add to tell me your favorite food\
                            \nUse /list to see the whole food list\
                            \nI will help you decide what to eat Use /eat")

# 使用方法：/add [食物名稱]
@bot.message_handler(commands=['add'])
def add_food(message):
    bot.reply_to(message, "Okay")
    """
    # TODO: 
    # 用 append() 方法，將 message.text 加入 foods list 當中
    # 記得用中括號  [] 選擇訊息中有用的字串
    """
    foods.append()

@bot.message_handler(commands=['list'])
def list_food(message):
    bot.reply_to(message, f"Here is the food list: {foods}")
    

@bot.message_handler(commands=['eat'])
def decide_food(message):
    if len(foods) == 0:
        bot.reply_to(message, "There is no food in the list")
    else:
        # TODO: 使用 random.choice() 方法，從 foods list 中隨機選擇一個食物
        food = 
        bot.reply_to(message, f"You should eat {food}")

@bot.message_handler(commands=['export'])
def export_food_list(message):
    try:
        # TODO: 使用 open() 方法，將 foods list 寫入 food_list.json 檔案中
        with open('', 'w') as file:
            # TODO: 使用 json.dump() 方法，將 foods list 寫入 file 當中 
            json.dump(, file, indent=4)
        bot.reply_to(message, "Food list has been successfully exported to food_list.json.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred while exporting the food list: {e}")

@bot.message_handler(commands=['import'])
def import_food_list(message):
    try:
        with open('food_list.json', 'r') as file:
            # TODO: 使用 json.load() 方法，將 file 中的資料讀取到 imported_foods 變數中
            imported_foods = json.load()
            global foods
            foods = imported_foods
        bot.reply_to(message, "Food list has been successfully imported from food_list.json.")
    except FileNotFoundError:
        bot.reply_to(message, "No food_list.json file found. Please export a food list first.")
    except Exception as e:
        bot.reply_to(message, f"An error occurred while importing the food list: {e}")


bot.infinity_polling()
