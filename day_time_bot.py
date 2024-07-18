from datetime import datetime
import telebot
from datetime import datetime

# TODO: 輸入自己 Bot 的 TOKEN
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

print("It's a beautiful day outside. Birds are singing, flowers are blooming...")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Howdy, how are you doing?")

# TODO: 實作自訂的 /time 指令
@bot.message_handler(commands=[''])
def send_time(message):
    current_time_str = get_current_time_str()
    bot.reply_to(message, f"{current_time_str}")

# TODO: 使用 strftime 寫出想要的時間字串格式
def get_current_time_str():
    now = datetime.now()
    formatted_time = now.strftime("")
    return formatted_time


bot.infinity_polling()





