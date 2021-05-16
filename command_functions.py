from os.path import join
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import json
from settings import app_id
from datetime import datetime


"""Список використовуваних ботом команд"""
command_functions_list = ['kill', 'commands', 'list', 'exchange']


def commands(**kwargs):
    def commands(update: Update, context: CallbackContext) -> None:
        """Повертає список використовуваних ботом команд"""
        update.message.reply_text(
            f'Список доступних команд - {command_functions_list}')
    return commands


def kill(**kwargs):
    def kill(update: Update, context: CallbackContext) -> None:
        """Фан-функція, формат виклику /kill 'name' """
        if len(update.message.text) <= 6:
            update.message.reply_text('Nobody to kill')
        else:
            update.message.reply_text(
                f'We will kill {update.message.text[6:]} for you')
    return kill



def list(**kwargs):
    """Команда для отримання поточної погоди у Києві"""
    def list(update: Update, context: CallbackContext) -> None:
        try:
            with open('exchange_rates_file.json', 'r') as read_file:
                data = json.load(read_file)
                now = datetime.now()
                my_time = datetime.timestamp(now)
                if my_time>= data['timestamp']+600:
                    with open('exchange_rates_file.json', 'w') as write_file:
                        response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={app_id}')
                        if response.status_code ==200:
                            result = response.text
                            write_file.write(result)
                        else:
                            print('No connection to server')
                    with open('exchange_rates_file.json', 'r') as read_file:
                        data = json.load(read_file)
                        user_data = {}
                        for key, item in data['rates'].items():
                            if round(item, 2) == 0:
                                user_data[key] = item
                            else:
                                user_data[key] = round(item, 2)
                        user_answer = json.dumps(user_data, indent=4)
                        update.message.reply_text(f'{user_answer[1:-1]}')
                        
                else:
                    user_data = {}
                    for key, item in data['rates'].items():
                        if round(item, 2) == 0:
                            user_data[key] = item
                        else:
                            user_data[key] = round(item, 2)
                    user_answer = json.dumps(user_data, indent=4)
                    update.message.reply_text(f'{user_answer[1:-1]}')
              
             
        except FileNotFoundError:
            with open('exchange_rates_file.json', 'w') as write_file:
                response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={app_id}')
                if response.status_code ==200:
                    result = response.text
                    write_file.write(result)
                else:
                    print('No connection to server')
            with open('exchange_rates_file.json', 'r') as read_file:
                data = json.load(read_file)
                user_data = {}
                for key, item in data['rates'].items():
                    if round(item, 2) == 0:
                        user_data[key] = item
                    else:
                        user_data[key] = round(item, 2)
                user_answer = json.dumps(user_data, indent=4)
                update.message.reply_text(f'{user_answer[1:-1]}')

    return list


def exchange(**kwargs):
    def exchange(update: Update, context: CallbackContext) -> None:
        try:
            with open('exchange_rates_file.json', 'r') as read_file:
                data = json.load(read_file)
                now = datetime.now()
                my_time = datetime.timestamp(now)
                if my_time>= data['timestamp']+600:
                    with open('exchange_rates_file.json', 'w') as write_file:
                        response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={app_id}')
                        if response.status_code ==200:
                            result = response.text
                            write_file.write(result)
                        else:
                            print('No connection to server')
                    with open('exchange_rates_file.json', 'r') as read_file:
                        data = json.load(read_file)
                        if len(update.message.text) <= 10:
                            update.message.reply_text('Nothing to convert')
                        else:
                            first_list = update.message.text.split('$')
                            if len(first_list)==1:
                                row = str(first_list)
                                second_list = row.split(' ')
                                number_dollars = int(second_list[1])
                                currency = second_list[-1][:-2]
                            if len(first_list)==2:
                                row = str(first_list[1])
                                second_list = row.split(' ')
                                number_dollars = int(second_list[0])
                                currency = second_list[-1]
                            exchange_rate = data['rates'][f'{currency}']
                            user_answer = round(number_dollars*exchange_rate, 2)
                            update.message.reply_text(f'{user_answer} - {currency}')
                        
                else:
                    with open('exchange_rates_file.json', 'r') as read_file:
                        data = json.load(read_file)
                        if len(update.message.text) <= 10:
                            update.message.reply_text('Nothing to convert')
                        else:
                            first_list = update.message.text.split('$')
                            if len(first_list)==1:
                                row = str(first_list)
                                second_list = row.split(' ')
                                number_dollars = int(second_list[1])
                                currency = second_list[-1][:-2]
                            if len(first_list)==2:
                                row = str(first_list[1])
                                second_list = row.split(' ')
                                number_dollars = int(second_list[0])
                                currency = second_list[-1]
                            exchange_rate = data['rates'][f'{currency}']
                            user_answer = round(number_dollars*exchange_rate, 2)
                            update.message.reply_text(f'{user_answer} - {currency}')
              
             
        except FileNotFoundError:
            with open('exchange_rates_file.json', 'w') as write_file:
                response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={app_id}')
                if response.status_code ==200:
                    result = response.text
                    write_file.write(result)
                else:
                    print('No connection to server')
            with open('exchange_rates_file.json', 'r') as read_file:
                data = json.load(read_file)
                if len(update.message.text) <= 10:
                    update.message.reply_text('Nothing to convert')
                else:
                    first_list = update.message.text.split('$')
                    if len(first_list)==1:
                        row = str(first_list)
                        second_list = row.split(' ')
                        number_dollars = int(second_list[1])
                        currency = second_list[-1][:-2]
                    if len(first_list)==2:
                        row = str(first_list[1])
                        second_list = row.split(' ')
                        number_dollars = int(second_list[0])
                        currency = second_list[-1]
                    exchange_rate = data['rates'][f'{currency}']
                    user_answer = round(number_dollars*exchange_rate, 2)
                    update.message.reply_text(f'{user_answer} - {currency}')
    return exchange