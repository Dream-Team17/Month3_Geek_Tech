from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
one_time_keyboard=True)

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz')

share_location = KeyboardButton('Share location', request_location=True)
share_contact = KeyboardButton('Share contact', request_contact=True)

start_markup.add(start_button, info_button, quiz_button).add(share_location, share_contact)

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
one_time_keyboard=True)



submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
one_time_keyboard=True).add(KeyboardButton('yes'), KeyboardButton('no'))

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
one_time_keyboard=True).add(KeyboardButton('CANCEL'))


