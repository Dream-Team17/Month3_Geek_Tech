from aiogram import types, Dispatcher
from config import bot, dp
from random import randint

# @dp.message_handler()
async def echo(message: types.Message):
    answer = f'@{message.from_user.username}' if message.from_user.username is not None \
        else message.from_user.full_name
    bad_words = ['java', 'html', 'дурак', 'глупый', 'козел', 'черт']
    for word in bad_words:
        if word in message.text.lower():
            await bot.delete_message(message.chat.id, message.message_id)
            await message.reply_to_message(f'Не матерись {answer}, сам ты {word}!')

    if message.text.startswith('game'):
        emoji =['⚽️', '🏀', '🎲', '🎯', '🎳', '🎰']
        await bot.send_dice(message.chat.id, emoji=emoji[randint(0, 5)])

    if message.text == 'dice':
        await message.answer(f'a die for {answer}')
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        a = a.dice.value
        bot_name = await bot.get_me()
        await message.answer(f'a die for {bot_name.full_name}')
        b = await bot.send_dice(message.chat.id, emoji='🎲')
        b = b.dice.value
        if a > b:
            await message.answer(f'Congratulations, {answer} is winner!')
        elif a < b:
            await message.answer(f'Thank you, {bot_name.full_name} is winner!')
        else:
            await message.answer(f'Well, {answer}, we have a draw!')

    if message.text.lower() == 'id':
        await bot.send_message(message.chat.id, f'ID твоего аккаунта в телеграмме: {message.from_user.id}')


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
