from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

kb_help = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('🔎help🔍')
b2 = KeyboardButton('continue➡️')
kb_help.add(b1, b2)

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('🛒SHRINE OF SECRETS🛒')
b2 = KeyboardButton('💠PERK BUILDS💠')
b3 = KeyboardButton('🌄ART🌄')
b4 = KeyboardButton('📬NEWS📬')
main_menu_kb.add(b1, b2, b3, b4)