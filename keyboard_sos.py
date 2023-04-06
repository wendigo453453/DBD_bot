from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


shrine_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('📝read description of the perks📝')
b2 = KeyboardButton('⬅️back to main menu')
shrine_kb.add(b1, b2)


survivior_rb_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('📝descriptions of the preks📝')
b2 = KeyboardButton('⬅️back to main menu')
survivior_rb_kb.add(b1, b2)


descriptions_shrine_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
b1 = KeyboardButton('📝description of the perk 1📝')
b2 = KeyboardButton('📝description of the perk 2📝')
b3 = KeyboardButton('📝description of the perk 3📝')
b4 = KeyboardButton('📝description of the perk 4📝')
b5 = KeyboardButton('⬅️back to main menu')
descriptions_shrine_kb.add(b1, b2, b3, b4, b5)