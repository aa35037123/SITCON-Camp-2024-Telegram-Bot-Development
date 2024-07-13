import telebot

TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing?")

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, it's a beautiful day outside.\
                        \nBirds are singing, flowers are blooming...")

bot.infinity_polling()