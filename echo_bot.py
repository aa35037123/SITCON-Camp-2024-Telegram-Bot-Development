import telebot
from datetime import datetime

# TODO: 輸入自己 Bot 的 TOKEN
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

print("It's a beautiful day outside. Birds are singing, flowers are blooming...")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """
    # TODO: 
    # 實作邏輯判斷，讓 Bot 可以對特定語句反應
    # 在 reply_to() 第二個參數填入不同回傳訊息
    """
    if message.text == :
        bot.reply_to(message, )
    else:
        bot.reply_to(message, )

bot.infinity_polling()

