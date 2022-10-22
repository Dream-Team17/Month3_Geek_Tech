from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboard.client_kb import gender_markup, submit_markup, cancel_markup, start_markup
from database.db import sql_command_insert


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    department = State()
    age = State()
    group = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        if message.chat.type == 'private':
            await FSMAdmin.id.set()
            await message.answer(f"Hello @{message.from_user.username}\n"
                             f"Please write mentor's name", reply_markup=cancel_markup)
            await FSMAdmin.next()
        else:
            await message.reply('Type to private chat')
    else:
        await message.answer('You are not curator!')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Department?', reply_markup=cancel_markup)

async def load_department(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['department'] = message.text
    await FSMAdmin.next()
    await message.answer('Mentor\'s age?', reply_markup=cancel_markup)

async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 10 or int(message.text) > 80:
            await message.answer('She/He can\'t be mentor!')
            await state.finish()
            return

        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Which group?', reply_markup=cancel_markup)
    except:
        await message.answer('Please write numbers')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f" Name: {data['name']}\nDepartment: {data['department']}\nAge: {data['age']}\nGroup: {data['group']}")

    await FSMAdmin.next()
    await message.answer('Ok?', reply_markup=submit_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'yes':
        await sql_command_insert(state)
        await state.finish()
        await message.answer('You are registered', reply_markup=start_markup)

    if message.text.lower() == 'no':
        await state.finish()
        await message.answer('Cancelled', reply_markup=None)

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Cancelled', reply_markup=None)

def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*' )

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_department, state=FSMAdmin.department)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)