from aiogram import types, Dispatcher
from config import bot, dp

async def ban(message: types.Message):
    if message.chat.id.type == group:
        if not message.from_user.id in ADMIN:
            await message.answer('Голум: Ты не мой господин!')
        elif not message.reply_to_message:
            await message.answer('Команда должен быть ответом на сообщение')
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    else:
        await message.answer('Пиши в группу')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')