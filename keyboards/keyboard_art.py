from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


ikb_random_art = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='yes❤️',
                                  callback_data="yes")
b2 = InlineKeyboardButton(text='no👎',
                                  callback_data="no")
b3 = InlineKeyboardButton(text='next➡️',
                                  callback_data="next_art")
ikb_random_art.add(b1, b2, b3)


kb_random_art = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('🎲Get random art🎲')
b2 = KeyboardButton('⬅️back to main menu')
kb_random_art.add(b1).add(b2)