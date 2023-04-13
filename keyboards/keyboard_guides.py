from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


kb_guide = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Tier List')
b3 = KeyboardButton('Wich survivors shood i unlock first?')
b4 = KeyboardButton('How too loop deafult constructions')
b5 = KeyboardButton('🗺Map clock callouts🗺')
b2 = KeyboardButton('⬅️back to main menu')
kb_guide.add(b1, b3, b4, b5, b2)

kb_tier_list = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('🔪Killer Tier List🔪')
b3 = KeyboardButton('💠Killer Perk Tier List💠')
b4 = KeyboardButton('💠Survivor Perk Tier List💠')
b5 = KeyboardButton('🗺Map Tier List🗺')
b2 = KeyboardButton('⬅️back to 📖GUIDES📖')
kb_tier_list.add(b1, b3, b4, b5, b2)

kb_clock_callouts = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('The MacMillan Estate')
b2 = KeyboardButton('Coldwind Farm')
b3 = KeyboardButton('Autohaven Wreckers')
b4 = KeyboardButton('Crotus Prenn Asylum')
b5 = KeyboardButton('Haddonfield')
b6 = KeyboardButton('Backwater Swamp')
b7 = KeyboardButton('Lerys Memorial Institute')
b8 = KeyboardButton('⬅️back to 📖GUIDES📖')
b9 = KeyboardButton('Following maps2️⃣➡️')
kb_clock_callouts.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)

kb_clock_callouts2 = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Red Forest')
b2 = KeyboardButton('Gideon Meat Plant')
b3 = KeyboardButton('Yamaoka Estate')
b4 = KeyboardButton('Ormond')
b5 = KeyboardButton('Dead Dawg Saloon')
b6 = KeyboardButton('Silent Hill')
b7 = KeyboardButton('⬅️1️⃣Previous maps')
b8 = KeyboardButton('⬅️back to 📖GUIDES📖')
b9 = KeyboardButton('Following maps3️⃣➡️')
kb_clock_callouts2.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)

kb_clock_callouts3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
b1 = KeyboardButton('Eyrie of Crows')
b2 = KeyboardButton('Garden of Joy')
b3 = KeyboardButton('The Shattered Square')
b7 = KeyboardButton('⬅️2️⃣Previous maps')
b8 = KeyboardButton('⬅️back to 📖GUIDES📖')
kb_clock_callouts3.add(b1, b2, b3, b7, b8)

ikb_fun_perk = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='For beginners',
                                  callback_data="For beginners")
b2 = InlineKeyboardButton(text='For fun',
                                  callback_data="For fun")
ikb_fun_perk.add(b1, b2)


ikb_k_t_l = InlineKeyboardMarkup(row_width=3)
b10 = InlineKeyboardButton(text='Tier List',
                                  callback_data="Tier List")
b1 = InlineKeyboardButton(text='NURSE',
                                  callback_data="NURSE")
b2 = InlineKeyboardButton(text='BLIGHT',
                                  callback_data="BLIGHT")
b3 = InlineKeyboardButton(text='SPIRIT',
                                  callback_data="SPIRIT")
b4 = InlineKeyboardButton(text='ARTIST',
                                  callback_data="ARTIST")
b5 = InlineKeyboardButton(text='PLAGUE',
                                  callback_data="PLAGUE")
b6 = InlineKeyboardButton(text='ONI',
                                  callback_data="ONI")
b7 = InlineKeyboardButton(text='EXECUTIONER',
                                  callback_data="EXECUTIONER")
b9 = InlineKeyboardButton(text='next2️⃣➡️',
                                  callback_data="2next")
ikb_k_t_l.add(b10, b1, b2, b3, b4, b5, b6, b7, b9)


ikb_k_t_l2 = InlineKeyboardMarkup(row_width=3)
b8 = InlineKeyboardButton(text='MASTERMIND',
                                  callback_data="MASTERMIND")
b1 = InlineKeyboardButton(text='HUNTERESS',
                                  callback_data="HUNTERESS")
b2 = InlineKeyboardButton(text='HAG',
                                  callback_data="HAG")
b3 = InlineKeyboardButton(text='TWINS',
                                  callback_data="TWINS")
b4 = InlineKeyboardButton(text='CENOBITE',
                                  callback_data="CENOBITE")
b5 = InlineKeyboardButton(text='CANIBAL',
                                  callback_data="CANIBAL")
b11 = InlineKeyboardButton(text='⬅️1️⃣BACK',
                                  callback_data="1BACK")
b6 = InlineKeyboardButton(text='DEMOGORGON',
                                  callback_data="DEMOGORGON")
b9 = InlineKeyboardButton(text='next3️⃣➡️',
                                  callback_data="3next")
ikb_k_t_l2.add(b8, b1, b2, b3, b4, b5, b11, b6, b9)


ikb_k_t_l3 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='DEADSLINGER',
                                  callback_data="DEADSLINGER")
b2 = InlineKeyboardButton(text='NEMESIS',
                                  callback_data="NEMESIS")
b3 = InlineKeyboardButton(text='DREDGE',
                                  callback_data="DREDGE")
b4 = InlineKeyboardButton(text='HILLBILLY',
                                  callback_data="HILLBILLY")
b5 = InlineKeyboardButton(text='TRICKSTER',
                                  callback_data="TRICKSTER")
b6 = InlineKeyboardButton(text='DOCTOR',
                                  callback_data="DOCTOR")
b11 = InlineKeyboardButton(text='⬅️2️⃣BACK',
                                  callback_data="2BACK")
b8 = InlineKeyboardButton(text='LEGION',
                                  callback_data="LEGION")
b9 = InlineKeyboardButton(text='next4️⃣➡️',
                                  callback_data="4next")
ikb_k_t_l3.add(b1, b2, b3, b4, b5, b6, b11, b8, b9)

ikb_k_t_l4 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='GHOSTFACE',
                                  callback_data="GHOSTFACE")
b2 = InlineKeyboardButton(text='PIG',
                                  callback_data="PIG")
b3 = InlineKeyboardButton(text='WRAITH',
                                  callback_data="WRAITH")
b4 = InlineKeyboardButton(text='CLOWN',
                                  callback_data="CLOWN")
b5 = InlineKeyboardButton(text='NIGHTMARE',
                                  callback_data="NIGHTMARE")
b6 = InlineKeyboardButton(text='SHAPE',
                                  callback_data="SHAPE")
b7 = InlineKeyboardButton(text='ONRYO',
                                  callback_data="ONRYO")
b11 = InlineKeyboardButton(text='⬅️3️⃣BACK',
                                  callback_data="3BACK")
b8 = InlineKeyboardButton(text='TRAPPER',
                                  callback_data="TRAPPER")
ikb_k_t_l4.add(b1, b2, b3, b4, b5, b6, b11, b7, b8)
