import telebot
from datetime import datetime
import json

# Replace with your actual bot token
TOKEN = "6355462545:AAF7_X-9X3JQnfWp_kvpKQ3eqBmNwwsa8bc"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# A list to store accounting data
# accounting_book = {}

class AccountingEntry:
    def __init__(self, item_name, cost, item_type):
        self.item_name = item_name
        self.cost = cost
        self.item_type = item_type
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day} [{self.timestamp}] {self.item_name}: ${self.cost} ({self.item_type})"
    
    def to_dict(self):
        return {
            "item_name": self.item_name,
            "cost": self.cost,
            "item_type": self.item_type,
            "timestamp": self.timestamp,
            "year": self.year,
            "month": self.month,
            "day": self.day
        }

class AccountingBook:
    def __init__(self):
        self.accouting_book = {}

    def add_entry(self, item_name, cost, item_type):
        entry = AccountingEntry(item_name, cost, item_type)
        self.entries.append(entry)

    def get_total_cost(self):
        return sum(entry.cost for entry in self.entries)

    def get_entries_by_type(self, item_type):
        return [entry for entry in self.entries if entry.item_type == item_type]

    def get_entries_by_name(self, item_name):
        return [entry for entry in self.entries if entry.item_name == item_name]

    def to_dict(self):
        return [entry.to_dict() for entry in self.entries]

# Create an instance of AccountingBook
accounting_book = AccountingBook()

def get_formatted_time():
    now = datetime.now()
    month = now.month
    day = now.day
    time = now.strftime("%H:%M:%S")
    formatted_time = f"現在時間：{month} 月 {day} 日 {time}"
    return formatted_time

# Command to start and help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Accounting Bot!\
                 \nAdd expense: /add <item_name> <cost> <item_type>\
                 \nGet consumption history: /history\
                 \nGet total cost: /total_cost\n")

@bot.message_handler(commands=['add'])
def add_expense(message):
    try:
        command_parts = message.text.split(maxsplit=3)
        if len(command_parts) < 4:
            bot.reply_to(message, "Usage: /add <item_name> <cost> <item_type>")
            return
        _, item_name, cost, item_type = command_parts
        cost = float(cost)
        accounting_book.add_entry(item_name, cost, item_type)
        bot.reply_to(message, f"Added: {item_name} costing {cost} as {item_type}")
    except ValueError:
        bot.reply_to(message, "Invalid cost value. Please enter a number for the cost.")

# Command to show current time
@bot.message_handler(commands=['time'])
def send_time(message):
    current_time = get_formatted_time()
    bot.reply_to(message, current_time)

@bot.message_handler(commands=['total_cost'])
def get_total_cost():
    total_cost = accounting_book.get_total_cost()
    return total_cost

# Command to show all expenses
@bot.message_handler(commands=['history'])
def show_expenses(message):
    if not accounting_book.entries:
        bot.reply_to(message, "No expenses recorded.")
        return
    response = "Expenses:\n"
    response += str(accounting_book)
    bot.reply_to(message, response)

# export accounting data to a json file
@bot.message_handler(commands=['export'])
def export_data(message):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"accounting_data_{timestamp}.json"
        with open(filename, "w") as file:
            json.dump(accounting_book.to_dict(), file, indent=4)
        bot.reply_to(message, f"Data successfully exported to {filename}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred while exporting data: {e}")


bot.infinity_polling()
