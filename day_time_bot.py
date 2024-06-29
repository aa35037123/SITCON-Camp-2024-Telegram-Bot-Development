from datetime import datetime
import telebot
from datetime import datetime

TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

print("It's a beautiful day outside. Birds are singing, flowers are blooming...")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing?")
    
@bot.message_handler(commands=['time'])
def send_time(message):
    current_time_str = get_current_time_str()
    bot.reply_to(message, f"{current_time_str}")

def get_current_time_str():
    now = datetime.now()
    formatted_time = now.strftime("現在時間：%-m 月 %-d 日 %H:%M:%S")
    return formatted_time


bot.infinity_polling()

