import telebot

# TODO: 輸入自己 Bot 的 TOKEN
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# TODO: 加入自訂的 command 到 commnad filters 中
@bot.message_handler(commands=[])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing?")

# TODO: 加上 infinity_polling() 函式，讓 Bot 可以不斷接收更新
bot.