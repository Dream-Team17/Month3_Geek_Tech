from aiogram import types, Dispatcher
from config import bot, dp

# @dp.message_handler()
async def echo(message: types.Message):
    answer = f'@{message.from_user.username}' if message.from_user.username is not None \
        else message.from_user.full_name
    bad_words = ['java', 'html', 'дурак', 'глупый', 'козел', 'черт']
    for word in bad_words:
        if word in message.text.lower():
            await bot.delete_message(message.chat.id, message.message_id)
            await message.answer(f'Не матерись {answer} сам ты {word}!')

    if message.text.startswith('!'):
            await bot.pin_chat_message(message.chat.id, message.message_id)
    if message.text.startswith('?'):
            await bot.unpin_chat_message(message.chat.id)

    if message.text == 'dice':
        a = await bot.send_dice(message.chat.id, emoji='🎳')
        print(a.dice.value)

    if message.text.lower() == 'id':
        await bot.send_message(message.chat.id, message.from_user.id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
