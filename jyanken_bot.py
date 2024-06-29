# This example show how to use inline keyboards and process button presses
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

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
    # buttoms = [InlineKeyboardButton(emoji['rock'], callback_data="cb_rock")]
    markup.add(InlineKeyboardButton(emoji['rock'], callback_data="cb_rock"),
                                InlineKeyboardButton(emoji['paper'], callback_data="cb_paper"),
                                InlineKeyboardButton(emoji['scissors'], callback_data="cb_scissors"))
    
    return markup

choices = ['rock', 'paper', 'scissors']

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    bot_action = random.choice(choices)
    player_action = call.data[3:]

    if player_action == bot_action:
        # return "It's a tie!"
        bot.send_message(call.message.chat.id, f"{bot_name}'s action is: {emoji[bot_action]} Your action is: {emoji[player_action]}\
                            \nIt's a tie!")
    elif (player_action == 'rock' and bot_action == 'scissors') or \
            (player_action == 'scissors' and bot_action == 'paper') or \
            (player_action == 'paper' and bot_action == 'rock'):
        # return "You win!"
        bot.send_message(call.message.chat.id, f"{bot_name}'s action is: {emoji[bot_action]} Your action is: {emoji[player_action]}\
                            \nYou win!\nIt's quite a fun game, isn't it?")
    else:
        # return "You lose!"
        bot.send_message(call.message.chat.id, f"{bot_name}'s action is: {emoji[bot_action]} Your action: {emoji[player_action]}\
                            \nYou lose! Fight me next time~\nKeep your determination.")

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