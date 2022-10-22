from aiogram import types, Dispatcher
from config import bot, dp, ADMIN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.db import sql_command_all, sql_command_delete

async def ban(message: types.Message):
    if message.chat.type == 'group':
        if not message.from_user.id in ADMIN:
            await message.answer('Ты не мой господин!')
        elif not message.reply_to_message:
            await message.answer('Команда должен быть ответом на сообщение')
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await bot.send_message(message.chat.id, f'{message.from_user.full_name} братан удалил '
                                                    f'{message.reply_to_message.from_user.full_name}')
    else:
        await message.answer('Пиши в группу')

async def pin_message(message: types.Message):
    if message.chat.type == 'group':
        if not message.from_user.id in ADMIN:
            await message.answer('Ты не мой господин')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение')
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

async def unpin_message(message: types.Message):
    if message.chat.type == 'group':
        if not message.from_user.id in ADMIN:
            await message.answer('Ты не мой господин')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение')
        else:
            await bot.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)

async def unpin_all_message(message: types.Message):
    if message.chat.type == 'group':
        if not message.from_user.id in ADMIN:
            await message.answer('Ты не мой господин')
        else:
            await bot.unpin_all_chat_messages(message.chat.id)

async def delete_data(message: types.Message):
    mentors = await sql_command_all()
    for mentor in mentors:
        await bot.send_message(message.from_user.id,
                               f"Name: {mentor[1]}\nDepartment: {mentor[2]}\n"
                               f"Age: {mentor[3]}\nGroup: {mentor[4]}",
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"delete {mentor[1]}",
                                                        callback_data=f"delete {mentor[0]}")))

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='This mentor was deleted from DB', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(unpin_message, commands=['unpin'], commands_prefix='!')
    dp.register_message_handler(unpin_all_message, commands=['unpinall'], commands_prefix='!')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))
