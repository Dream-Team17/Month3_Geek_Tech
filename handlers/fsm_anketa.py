from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboard.client_kb import gender_markup, submit_markup, cancel_markup


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
                             f"Say hello")
        else:
            await message.reply('Type to private chat')
    else:
        await message.answer('You are not curator!')

async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = 1
    await message.answer(f"Mentor's ID is {data['id']}")
    await FSMAdmin.next()
    await message.answer(f"Mentor's name?")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Department?')

async def load_department(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['department'] = message.text
    await FSMAdmin.next()
    await message.answer('Mentor\'s age?')

async def load_age(message: types.Message, state: FSMContext):
    try:
        if int(message.text) < 18 or int(message.text) > 50:
            await message.answer('She/He can\'t be mentor!')
            await state.finish()
            return

        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('Which group?', reply_markup=gender_markup)
    except:
        await message.answer('Please write numbers')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"{data['id']}. {data['name']}, {data['department']}, {data['age']}, {data['group']}")

    await FSMAdmin.next()
    await message.answer('Ok?', reply_markup=cancel_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'yes':
        await state.finish()
        await message.answer('You are registered', reply_markup=None)

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
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_department, state=FSMAdmin.department)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)