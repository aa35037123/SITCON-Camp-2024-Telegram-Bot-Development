# This example show how to use inline keyboards and process button presses
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# TODO: 輸入自己 Bot 的 TOKEN
TOKEN = ""

bot = telebot.TeleBot(TOKEN)
bot_info = bot.get_me()  # Fetches the bot's information
bot_name = bot_info.first_name  # Gets the bot's first name

emoji = {
    'rock': '👊',
    'paper': '🖖',
    'scissors': '🤞'
}

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    # TODO: 自訂不同按鈕的 callback_data 的字串內容
    markup.add(InlineKeyboardButton(emoji['rock'], callback_data=""),
                                InlineKeyboardButton(emoji['paper'], callback_data=""),
                                InlineKeyboardButton(emoji['scissors'], callback_data=""))
    
    return markup

choices = ['rock', 'paper', 'scissors']

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # TODO: 用 random 隨機選擇 Bot 要出的拳
    bot_action = random.choice(choices)
    # TODO: call.data 等於 gen_markup() 內按鈕的 callback_data
    player_action = call.data

    # TODO: 使用 if elif else 語法來判斷勝負
    if : 
        result = "It's a tie!"
    elif :
        result = "You win!"
    else:
        result = "You lose!"

    reply_message = f"{bot_name}'s action: {emoji[bot_action]}, Your action: {emoji[player_action]}\n{result}"
    # TODO: 從 CallbackQuery.message.chat.id 物件中得到所在聊天室的 id
    bot.send_message(, reply_message)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Hello! Welcome to the Rock-Paper-Scissors game! \
                        \nUse /game to start the game. \
                        \nChoose your action by clicking the buttons below. \
                        \nI will randomly choose one of the actions and compare with yours. \
                        \nLet's see who will win!")

@bot.message_handler(commands=['game'])
def message_handler(message):
    bot.send_message(message.chat.id, "Let's play! It's your turn~", reply_markup=gen_markup())

bot.infinity_polling()