# bot/management/commands/start_bot.py
from django.core.management.base import BaseCommand
from bot.tasks import run_telegram_bot

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):
        run_telegram_bot.delay()
