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
b5 = KeyboardButton('📖GUIDES📖')
b6 = KeyboardButton('👥SEARCH TEAM👥')
b7 = KeyboardButton('💰SUPORT AUTOR💰')
main_menu_kb.add(b1, b2, b3, b4, b5, b6, b7)


kb_SEARCH_TEAM = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('questionnaire creation')
b2 = KeyboardButton('questionnaire review')
b3 = KeyboardButton('⬅️back to main menu')
kb_SEARCH_TEAM.add(b1, b2, b3)