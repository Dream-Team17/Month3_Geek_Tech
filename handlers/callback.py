from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp

# @dp.callback_query_handler(lambda call: call.data =='button_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next', callback_data='button_2')
    markup.add(button_1)

    question = 'В каком известном романе фигурировали Джо, Мег, Бет и Эми Марч?'
    answer = [
        'Убить пересмешника',
        'Том Сойер',
        'Маленькие женщины',
        'Моби Дик'
    ]

    await bot.send_poll(chat_id=call.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        explanation='Любитель романов?',
                        reply_markup=markup)

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next', callback_data='button_3')
    markup.add(button_1)
    question = 'Какая игрушка была первой, которую рекламировали по телевидению?'
    answer = [
        'Барби',
        'Мистер картофельная голова',
        'Духовка с легкой выпечкой',
        'Ракетный гонщик'
    ]

    await bot.send_poll(chat_id=call.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        explanation='Молодец',
                        correct_option_id=1
                        )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data=='button_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data=='button_2')