from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from random import randint
from keyboard.client_kb import start_markup
from database.db import sql_command_random

# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Добро пожаловать Господин {message.from_user.first_name}\n'
                                                 f'Вам доступны команды: /quiz и /mem',
                           reply_markup=start_markup)

async def info_handler(message: types.Message):
    await message.reply('Сам разбирайся')

# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next', callback_data='button_1')
    markup.add(button_1)

    question='В сиквеле какого праздничного фильма снялся Дональд Трамп?'
    answer = [
        'Один дома',
        'Один дома 2: Затерянный в Нью-Йорке',
        'Ричи Рич',
        'Маленькие негодяи'
    ]

    await bot.send_poll(chat_id=message.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        explanation='Любитель фильма?',
                        reply_markup=markup)



# @dp.message_handler(commands=['mem'])
async def send_mem(message: types.Message):


    photo_1 = open('media/mem_1.jpeg', 'rb')
    photo_2 = open('media/mem_2.jpeg', 'rb')
    photo_3 = open('media/mem_3.jpeg', 'rb')
    photo_4 = open('media/mem_4.jpeg', 'rb')
    photo_lst = [photo_1, photo_2, photo_3, photo_4]
    a = randint(0, 3)
    await bot.send_photo(message.from_user.id, photo=photo_lst[a])

async def get_random_mentor(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_mem, commands=['mem'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(get_random_mentor, commands=['get'])



