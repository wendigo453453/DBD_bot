from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup



pick_side_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('🛠Survivor🛠')
b2 = KeyboardButton('🔪Killer🔪')
b3 = KeyboardButton('🎲RANDOM PERK BUILDS🎲')
b4 = KeyboardButton('⬅️back to main menu')
pick_side_kb.add(b1, b2, b3, b4)


kb_rand_p_b = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('🎲RANDOM SURVIVORS PERK BUILDS🎲')
b2 = KeyboardButton('🎲RANDOM KILLERS PERK BUILDS🎲')
b3 = KeyboardButton('⬅️back to main menu')
kb_rand_p_b.add(b1, b2, b3)


ikb_sb1 = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text='📝description📝',
                                  callback_data="description_sb1")
b2 = InlineKeyboardButton(text='next➡️2️⃣',
                                  callback_data="next->2")
ikb_sb1.add(b1, b2)


ikb_sb2 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='1️⃣⬅️previous',
                                  callback_data="1<-previous")
b2 = InlineKeyboardButton(text='📝description📝',
                                  callback_data="description_sb2")
b3 = InlineKeyboardButton(text='next➡️3️⃣',
                                  callback_data="next->3")
ikb_sb2.add(b1, b2, b3)

ikb_sb3 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='2️⃣⬅️previous',
                                  callback_data="2<-previous")
b2 = InlineKeyboardButton(text='📝description📝',
                                  callback_data="description_sb3")
ikb_sb3.add(b1, b2)




ikb_kb1 = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text='📝description📝',
                                  callback_data="description_kb1")
b2 = InlineKeyboardButton(text='next➡️2️⃣',
                                  callback_data="next_kb->2")
ikb_kb1.add(b1, b2)

ikb_kb2 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='1️⃣⬅️previous',
                                  callback_data="1<-previous_kb")
b2 = InlineKeyboardButton(text='📝description📝',
                                  callback_data="description_kb2")
b3 = InlineKeyboardButton(text='next➡️3️⃣',
                                  callback_data="next_kb->3")
ikb_kb2.add(b1, b2, b3)

ikb_kb3 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='2️⃣⬅️previous',
                                  callback_data="2<-previous_kb")
b2 = InlineKeyboardButton(text='📝description📝',
                                  callback_data="description_kb3")
ikb_kb3.add(b1, b2)