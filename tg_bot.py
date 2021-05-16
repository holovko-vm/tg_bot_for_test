from command_functions import command_functions_list
import command_functions
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


class My_tg_bot:
    def __init__(self, token):
        """Створюємо Об'єкт, що слідкує за новинами,
        Вставте токен Вашого бота settings.py.default --> settings.py >> token = 'Токен Вашого бота'
        """
        self.updater = Updater(token=token)
        """Створюємо Об'єкт, який направляє новину відповідному обробнику"""
        self.dispatcher = self.updater.dispatcher
        """Створюємо метод, який зберігає контекст користувачів
        (вибраний обробник повідомлень, положення користувача у відповідному сценарії)"""
        self.users_ctx = {'user_state': {}, 'user_handler':{}}
    
    def add_command_handlers(self, command_handlers=None):
        """Метод для створення обробників команд згідно списку команд
         з command_functions.command_functions_list"""
        for command in command_handlers:
            try:
                self.dispatcher.add_handler(CommandHandler(
                    command, getattr(command_functions, command)(users_ctx=self.users_ctx)))
            except AttributeError:
                logging.error(
                    f'Невідома функція - {command}, додайте її до файлу command_functions.py')

  

    def run(self, command_handlers=None):
        """Створюємо обробників"""
        self.add_command_handlers(command_handlers)
        """Слухаємо сервер"""
        self.updater.start_polling()
        self.updater.idle()


