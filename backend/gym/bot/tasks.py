# bot/tasks.py
from celery import shared_task
import telebot

@shared_task
def run_telegram_bot():
    bot = telebot.TeleBot('YOUR_BOT_TOKEN')

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Welcome! How can I assist you today?")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(message, "Here are the commands you can use:\n/start - Welcome message\n/help - Help information")

    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        if message.from_user.username == "Hoda2035":
            bot.reply_to(message, f"بحبك يا هداااا")
        else:
            bot.reply_to(message, f"Abdo Loves You {message.from_user.first_name}")

    bot.polling()
