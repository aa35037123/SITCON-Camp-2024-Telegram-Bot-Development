import telebot

# TODO: 輸入自己 Bot 的 TOKEN
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# TODO: 當輸入 /reply 時，讓 Bot 可以用回覆方式傳送訊息
@bot.message_handler(commands=['reply'])
def send_welcome(message):
    bot.

# TODO: 當輸入 /send 時，讓 Bot 可以直接傳送訊息到聊天室當中
@bot.message_handler(commands=['send'])
def send_welcome(message):
    bot.
    
bot.infinity_polling()

