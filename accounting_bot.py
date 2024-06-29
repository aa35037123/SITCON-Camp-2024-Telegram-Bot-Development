import telebot
from datetime import datetime
import json

# Replace with your actual bot token
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)
json_filename = f"accounting_data.json"

class AccountingEntry:
    def __init__(self, item_name, cost, item_type, timestamp=None, year=None, month=None, day=None):
        self.item_name = item_name
        self.cost = cost
        self.item_type = item_type
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day

    def __str__(self):
        return f"[{self.item_type}] {self.item_name}: ${self.cost} at {self.year}/{self.month}/{self.day} {self.timestamp}"
    
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
        self.accouting_book = []

    def add_entry(self, item_name, cost, item_type):
        entry = AccountingEntry(item_name, cost, item_type)
        self.accouting_book.append(entry)

    def get_total_cost(self):
        return sum(entry.cost for entry in self.accouting_book)
    
    def add_entry_from_dict(self, entry_dict):
        entry = AccountingEntry(
            item_name=entry_dict["item_name"],
            cost=entry_dict["cost"],
            item_type=entry_dict["item_type"],
            timestamp=entry_dict["timestamp"],
            year=entry_dict["year"],
            month=entry_dict["month"],
            day=entry_dict["day"]
        )
        self.accouting_book.append(entry)

    def get_entries_by_type(self, item_type):
        return [entry for entry in self.accouting_book if entry.item_type == item_type]

    def get_entries_by_name(self, item_name):
        return [entry for entry in self.accouting_book if entry.item_name == item_name]

    def to_dict(self):
        return [entry.to_dict() for entry in self.accouting_book]
    def get_history_str(self):
        # return "\n".join(str(entry) for entry in self.accouting_book)
        history_str = ""
        for entry in self.accouting_book:
            history_str += str(entry) + "\n"
        return history_str

# Create an instance of AccountingBook
accounting_book = AccountingBook()

def import_data():
    try:
        with open(json_filename, "r") as file:
            data = json.load(file)
            for entry_dict in data:
                accounting_book.add_entry_from_dict(entry_dict)
        print(f"Data successfully imported from {json_filename}")
    except FileNotFoundError:
        print(f"File {json_filename} not found.")
    except Exception as e:
        print(f"An error occurred while importing data: {e}")

# import_data()

def get_formatted_time():
    now = datetime.now()
    month = now.month
    day = now.day
    time = now.strftime("%H:%M:%S")
    formatted_time = f"現在時間：{month} 月 {day} 日 {time}"
    return formatted_time

# Command to start and help
@bot.message_handler(commands=[ 'help'])
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
        # cost = int(cost)
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
    if not accounting_book.accouting_book:
        bot.reply_to(message, "No expenses recorded.")
        return
    response = "Expenses:\n"
    response += accounting_book.get_history_str()
    bot.reply_to(message, response)

# export accounting data to a json file
@bot.message_handler(commands=['export'])
def export_data(message):
    try:
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        to
        with open(json_filename, "a") as file:
            json.dump(accounting_book.to_dict(), file, indent=4)
        bot.reply_to(message, f"Data successfully exported to {json_filename}")
    except Exception as e:
        bot.reply_to(message, f"An error occurred while exporting data: {e}")


bot.infinity_polling()
