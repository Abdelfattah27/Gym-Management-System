import telebot
import json
# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
bot = telebot.TeleBot('7057204042:AAHHO4fxQPIE8-upBioXarSqo7JNsI53Oww')

# Define a handler for the '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print( "9" , message)
    bot.reply_to(message, "Welcome! How can I assist you today?")

# Define a handler for the '/help' command
@bot.message_handler(commands=['help'])
def send_help(message):
    print(15 , message)
    bot.reply_to(message, "Here are the commands you can use:\n/start - Welcome message\n/help - Help information")

# Define a handler for text messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    # print(message.from_user.first_name)
    if message.from_user.username == "Hoda2035" : 
        
        bot.reply_to(message,f"بحبك يا هداااا")
    else : 
        bot.reply_to(message,f"Abdo Loves You {message.from_user.first_name}")

# Start polling to handle incoming messages
bot.polling()
