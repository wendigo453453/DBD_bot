from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto
import hashlib
import json
import random
import sqlite_db

import sqlite3 as sq
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from aiogram.utils import markdown as md


from keyboards.keyboard import *
from keyboards.keyboard_perk_builds import *
from keyboards.keyboard_sos import *
from keyboards.keyboard_art import *
from keyboards.keyboard_news import *
from keyboards.keyboard_guides import *

from db import Database
from query_hendlers.perk_builds import perk_builds
from query_hendlers.news import news
from query_hendlers.leaks import leaks
from query_hendlers.killer_tier_list import killer_tier_list
from query_hendlers.art import art
from message_handlers.map_clock_callouts import *
from config import *


TOKEN_API = TOKEN_API1

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)
pick_f = False

with open('news/news_dict.json', 'r') as file:
    data = json.load(file)
with open('news/leaks_dict.json', 'r') as file:
    datal = json.load(file)
with open('art.json') as f:
    dataa = json.load(f)

db = sq.connect('survivors_builds.db')
cur = db.cursor()

dbu = Database('survivors_builds.db')



async def on_startup(_):
    await sqlite_db.db_connect()
    print('connected to db')


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    if message.chat.type == 'private':
        if not dbu.user_exists(message.from_user.id):
            dbu.add_user(message.from_user.id)
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEHlSxj3jxl0ubka2pb7XCu5mQHPDpuOwAC0gADJ--KHOoe3vogG-VVLgQ")
    await message.answer(text="Greetings in the bot!",
                         reply_markup=kb_help)
    await message.delete()




@dp.message_handler(Text(equals="💰SUPORT AUTOR💰"))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://claypotchurchint.com/wp-content/uploads/2017/10/Donation-plugins-for-WordPress1.jpg",
                         caption="Any support would be greatly appreciated\n💳monobank💳 4441114440831905\n💵tether trc20💵 TH1KyZydKAEhmjnTiNhZtV9rP6v5gwYZUk""",
                         reply_markup=main_menu_kb)



@dp.message_handler(Text(equals="👥SEARCH TEAM👥"))
async def search(message: types.Message):
    await message.answer(text="Here you can find a team to play together, to do this you can create your own profile or view profiles of other players",
                         reply_markup=kb_SEARCH_TEAM)


class ClientStatesGroup(StatesGroup):
    photo = State()
    desc = State()

def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))

@dp.message_handler(Text(equals='questionnaire creation', ignore_case=True), state=None)
async def start_work(message: types.Message) -> None:
    await ClientStatesGroup.photo.set()
    await message.answer('First send us a picture that will be displayed to other players when viewing the questionnaire, for example, a screenshot of steem profile',
                         reply_markup=get_cancel())


@dp.message_handler(commands=['cancel'], state='*')
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply('cancelled',
                        reply_markup=main_menu_kb)
    await state.finish()

@dp.message_handler(lambda message: not message.photo, state=ClientStatesGroup.photo)
async def check_photo(message: types.Message):
    return await message.reply('This is not a picture!')


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await ClientStatesGroup.next()
    await message.reply('Now send us a description of your profile, tell us about yourself, how many hours you have, and be sure to enter your contact information how to get in touch with you!')


conn = sq.connect('survivors_builds.db')
cursor = conn.cursor()

@dp.message_handler(state=ClientStatesGroup.desc)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
        cursor.execute('INSERT INTO ankets (image_url, text) VALUES (?, ?)',
                       (data['photo'], data['desc']))
        conn.commit()
    async with state.proxy() as data:
        await message.reply('This is what your questionnaire looks like⬇️')
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=data['desc'])
    await message.reply('Your profile has been created!',
                         reply_markup=main_menu_kb)
    await state.finish()



def get_random_record():
    cursor.execute('SELECT * FROM ankets ORDER BY RANDOM() LIMIT 1')
    record = cursor.fetchone()
    return record

@dp.message_handler(Text(equals="questionnaire review"))
async def show_random_record(message: types.Message):
    record = get_random_record()

    if record is not None:
        image_url = record[1]
        text = record[2]
        await bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=text,
                         reply_markup=kb_SEARCH_TEAM)
    else:
        await message.reply('No data available',
                         reply_markup=kb_SEARCH_TEAM)





@dp.message_handler(commands=['sendall'])
async def help_command(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 555231712:
            text = message.text[9:]
            users = dbu.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        dbu.set_active(row[0], 1)
                except:
                    dbu.set_active(row[0], 0)
            await bot.send_message(message.from_user.id, "ycпешная рассылка")



@dp.message_handler(Text(equals="🔎help🔍"))
async def help_command(message: types.Message):
    await message.answer(text="the bot was created for the dbd community, then I will add a help text",
                         reply_markup=main_menu_kb)


@dp.message_handler(Text(equals="continue➡️"))
async def continue_command(message: types.Message):
    await message.answer(text="Welcome to main menu!",
                         reply_markup=main_menu_kb)

@dp.message_handler(Text(equals="⬅️back to main menu"))
async def backfromshrine_command(message: types.Message):
    await message.answer(text="Welcome back to main menu!",
                         reply_markup=main_menu_kb)


####################################___GUIDES___####################################

@dp.message_handler(Text(equals="📖GUIDES📖"))
async def send_image(message: types.Message):
    await message.answer(text="choose what you want too see",
                         reply_markup=kb_guide)

@dp.message_handler(Text(equals="Tier List"))
async def send_image(message: types.Message):
    await message.answer(text="choose what tier list do you want too wach",
                         reply_markup=kb_tier_list)


@dp.message_handler(Text(equals="Wich survivors shood i unlock first?"))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.ibb.co/47n7bQV/Screenshot-5.jpg",
                         caption="Here you can see which survivors i  recomend too buy for a new player. \nYou can also see survivor with the most fun perk too use⬇️",
                         reply_markup=ikb_fun_perk)


@dp.message_handler(Text(equals="🔪Killer Tier List🔪"))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.ibb.co/1bvN0Zn/Screenshot-9.jpg",
                         caption="You can see more information about individual killers using the button below⬇️",
                         reply_markup=ikb_k_t_l)


@dp.message_handler(Text(equals="💠Killer Perk Tier List💠"))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.ibb.co/GPPVR0K/Screenshot-9.jpg",
                         reply_markup=kb_tier_list)

@dp.message_handler(Text(equals="💠Survivor Perk Tier List💠"))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.ibb.co/n0kqgTz/Screenshot-9.jpg",
                         reply_markup=kb_tier_list)


@dp.message_handler(Text(equals="🗺Map Tier List🗺"))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://i.ibb.co/Z26DNHw/Screenshot-9.jpg",
                         reply_markup=kb_tier_list)


@dp.message_handler(Text(equals='How too loop deafult constructions'))
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://external-preview.redd.it/N6ql-UJMNjLk_iIHfcDhh3A6M_HO_R0HzDBTklJak6A.png?auto=webp&v=enabled&s=8f65501dd5a906bf3719c6c149df92e91dd89607",
                         reply_markup=kb_guide)


#################################### SHRINE OF SECRETS ####################################

@dp.message_handler(Text(equals="🛒SHRINE OF SECRETS🛒"))
async def send_image(message: types.Message):
    sos1 = await sqlite_db.sos_1()
    for survivors_builds in sos1:
        await message.answer(text=survivors_builds[1])
        await bot.send_photo(chat_id=message.chat.id,
                             photo=survivors_builds[2],
                             reply_markup=shrine_kb)


@dp.message_handler(Text(equals="📝read description of the perks📝"))
async def send_image(message: types.Message):
    await message.answer(text="choose which perk you want to read the description for",
                         reply_markup=descriptions_shrine_kb)


@dp.message_handler(Text(equals="📝description of the perk 1📝"))
async def send_image(message: types.Message):
    sos2 = await sqlite_db.sos_2()
    for survivors_builds in sos2:
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[2],
                         caption=f"perk: {survivors_builds[1]}")
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[3],
                         reply_markup=descriptions_shrine_kb)


@dp.message_handler(Text(equals="📝description of the perk 2📝"))
async def send_image(message: types.Message):
    sos3 = await sqlite_db.sos_3()
    for survivors_builds in sos3:
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[2],
                         caption= f"perk: {survivors_builds[1]}")
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[3],
                         reply_markup=descriptions_shrine_kb)


@dp.message_handler(Text(equals="📝description of the perk 3📝"))
async def send_image(message: types.Message):
    sos4 = await sqlite_db.sos_4()
    for survivors_builds in sos4:
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[2],
                         caption= f"perk: {survivors_builds[1]}")
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[3],
                         reply_markup=descriptions_shrine_kb)


@dp.message_handler(Text(equals="📝description of the perk 4📝"))
async def send_image(message: types.Message):
    sos5 = await sqlite_db.sos_5()
    for survivors_builds in sos5:
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[2],
                         caption= f"perk: {survivors_builds[1]}")
        await bot.send_photo(chat_id=message.chat.id,
                         photo=survivors_builds[3],
                         reply_markup=descriptions_shrine_kb)


@dp.message_handler(Text(equals="📝descriptions of the preks📝"))
async def send_image(message: types.Message):
    await message.answer(text="Select the description of which perk you want to see",
                         reply_markup=descriptions_shrine_kb)


#################################### ART ####################################

@dp.message_handler(Text(equals="🌄ART🌄"))
async def send_art(message: types.Message):
    await message.answer(text="Do you want too see random art?",
                         reply_markup=kb_random_art)


@dp.message_handler(Text(equals="🎲Get random art🎲"))
async def help_command(message: types.Message):
    art1 = await sqlite_db.art_1()
    for survivors_builds in art1:
        global pick_f
        pick_f = not pick_f
        random_link = random.choice(dataa['links'])
        await bot.send_photo(chat_id=message.chat.id,
                         photo=(random_link['address']),
                         caption='how do you like the art?',
                         reply_markup=ikb_random_art)
        await message.delete()
############################################--PERK BUILDS--##########################################################

@dp.message_handler(Text(equals="💠PERK BUILDS💠"))
async def perk_bilds_command(message: types.Message):
    await message.answer(text="Which side do you want to see builds for?",
                         reply_markup=pick_side_kb)


@dp.message_handler(Text(equals="🛠Survivor🛠"))
async def perk_bildss_command(message: types.Message):
    sb1 = await sqlite_db.surv_b1()
    for survivors_builds in sb1:
        await bot.send_photo(chat_id=message.chat.id,
                             photo=survivors_builds[1],
                             caption=survivors_builds[2],
                             reply_markup=ikb_sb1)


@dp.message_handler(Text(equals="🔪Killer🔪"))
async def perk_bilds_command(message: types.Message):
    kb1 = await sqlite_db.killer_b1()
    for survivors_builds in kb1:
        await bot.send_photo(chat_id=message.chat.id,
                             photo=survivors_builds[1],
                             caption=survivors_builds[2],
                             reply_markup=ikb_kb1)



##############################__rand perk builds__###############################

@dp.message_handler(Text(equals="🎲RANDOM PERK BUILDS🎲"))
async def send_image(message: types.Message):
    await message.answer(text="Which side do you want to see random builds for",
                         reply_markup=kb_rand_p_b)


@dp.message_handler(Text(equals="🎲RANDOM SURVIVORS PERK BUILDS🎲"))
async def send_image(message: types.Message):
    with open('Survivor_random_p_b.json', 'r') as f:
        datar = json.load(f)

    random_values = random.sample(list(datar.items()), 4)

    icon_name_1, icon_url_1 = random_values[0]
    icon_name_2, icon_url_2 = random_values[1]
    icon_name_3, icon_url_3 = random_values[2]
    icon_name_4, icon_url_4 = random_values[3]

    photos = [
        types.InputMediaPhoto(icon_url_1),
        types.InputMediaPhoto(icon_url_2),
        types.InputMediaPhoto(icon_url_3),
        types.InputMediaPhoto(icon_url_4)
    ]
    icon_name_1 = icon_name_1[11:]
    icon_name_2 = icon_name_2[11:]
    icon_name_3 = icon_name_3[11:]
    icon_name_4 = icon_name_4[11:]

    await bot.send_media_group(chat_id=message.chat.id,
                               media=photos)
    await message.answer(text=f"🎲Your random perks🎲:\n📍{icon_name_1}\n📍{icon_name_2}\n📍{icon_name_3}\n📍{icon_name_4}",
                         reply_markup=kb_rand_p_b)

@dp.message_handler(Text(equals="🎲RANDOM KILLERS PERK BUILDS🎲"))
async def send_image(message: types.Message):
    with open('Killer_random_p_b.json', 'r') as f:
        datak = json.load(f)

    krandom_values = random.sample(list(datak.items()), 4)

    kicon_name_1, kicon_url_1 = krandom_values[0]
    kicon_name_2, kicon_url_2 = krandom_values[1]
    kicon_name_3, kicon_url_3 = krandom_values[2]
    kicon_name_4, kicon_url_4 = krandom_values[3]

    kphotos = [
        types.InputMediaPhoto(kicon_url_1),
        types.InputMediaPhoto(kicon_url_2),
        types.InputMediaPhoto(kicon_url_3),
        types.InputMediaPhoto(kicon_url_4)
    ]

    await bot.send_media_group(chat_id=message.chat.id,
                               media=kphotos)
    await message.answer(text=f"🎲Your random perks🎲:\n📍{kicon_name_1}\n📍{kicon_name_2}\n📍{kicon_name_3}\n📍{kicon_name_4}",
                         reply_markup=kb_rand_p_b)


####################################   NEWS   ####################################

@dp.message_handler(Text(equals="📬NEWS📬"))
async def perk_bilds_command(message: types.Message):
    await message.answer(text="Pick what type of news you want to read",
                         reply_markup=news_main)


@dp.message_handler(Text(equals="📬DBD NEWS📬"))
async def perk_bilds_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=(data['0']['news_pictures']),
                         caption=f"📆Date{(data['0']['news_date_time'])}📆\n📃{(data['0']['news_title'])}📃\n\n📑{(data['0']['news_description'])}📑",
                         reply_markup=ikb_dbd_news1)

@dp.message_handler(Text(equals="📬💧DBD LEAKS💧📬"))
async def perk_bilds_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=(datal['10']['news_pictures']),
                         caption=f"📆Date{(datal['10']['news_date_time'])}📆\n📃{(datal['10']['news_title'])}📃\n\n📑{(datal['10']['news_description'])}📑",
                         reply_markup=ikb_dbd_news1_l)




#################################### InLinemode "@" ####################################

@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    sos2 = await sqlite_db.sos_2()
    for survivors_builds2 in sos2:
        sos3 = await sqlite_db.sos_3()
        for survivors_builds3 in sos3:
            sos4 = await sqlite_db.sos_4()
            for survivors_builds4 in sos4:
                sos5 = await sqlite_db.sos_5()
                for survivors_builds5 in sos5:
                    sos1 = await sqlite_db.sos_1()
                    for survivors_builds1 in sos1:
                            text = f"A friend sent you a shrine of secrets, take a look at it🧐 \n📍{survivors_builds2[1]}, \n📍{survivors_builds3[1]}, \n📍{survivors_builds4[1]}, \n📍{survivors_builds5[1]}"
                            input_content = InputTextMessageContent(text)
                            result_id: str = hashlib.md5(text.encode()).hexdigest()

                            item = InlineQueryResultPhoto(
                                photo_url='https://i.pinimg.com/564x/71/06/73/710673ff26399a8237f8e55d20e7c142.jpg',
                                id=result_id,
                                title='shrine of secret',
                                description='send a shrine of secret to a friend',
                                caption=f'A friend sent you a shrine of secrets, take a look at it🧐 \n📍{survivors_builds2[1]}, \n📍{survivors_builds3[1]}, \n📍{survivors_builds4[1]}, \n📍{survivors_builds5[1]}',
                                thumb_url=survivors_builds1[2]
                            )

                            await bot.answer_inline_query(
                                        inline_query_id=inline_query.id,
                                        results=[item],
                                        cache_time=1
                                    )
######################___MAP__CLOCK_CALLOUTS___################################
dp.register_message_handler(Map_clock_callouts, Text(equals="🗺Map clock callouts🗺"))
dp.register_message_handler(MacMillan, Text(equals="The MacMillan Estate"))
dp.register_message_handler(Coldwind, Text(equals="Coldwind Farm"))
dp.register_message_handler(Autohaven, Text(equals="Autohaven Wreckers"))
dp.register_message_handler(Crotus, Text(equals="Crotus Prenn Asylum"))
dp.register_message_handler(Swamp, Text(equals="Backwater Swamp"))
dp.register_message_handler(Institute, Text(equals="Lerys Memorial Institute"))
dp.register_message_handler(Red__Forest, Text(equals="Red Forest"))
dp.register_message_handler(Following_maps2, Text(equals="Following maps2️⃣➡️"))
dp.register_message_handler(Badham, Text(equals="Badham"))
dp.register_message_handler(Gideon, Text(equals="Gideon Meat Plant"))
dp.register_message_handler(Yamaoka, Text(equals="Yamaoka Estate"))
dp.register_message_handler(Ormond, Text(equals="Ormond"))
dp.register_message_handler(back_to_GUIDES, Text(equals="⬅️back to 📖GUIDES📖"))
dp.register_message_handler(Haddonfield, Text(equals="Haddonfield"))
dp.register_message_handler(Saloon, Text(equals="Dead Dawg Saloon"))
dp.register_message_handler(Hill, Text(equals="Silent Hill"))
dp.register_message_handler(Raccoon, Text(equals="Raccoon City"))
dp.register_message_handler(Previous_maps, Text(equals="⬅️Previous maps"))
dp.register_message_handler(Following_maps, Text(equals="Following maps➡️"))
dp.register_message_handler(Eyrie, Text(equals="Eyrie of Crows"))
dp.register_message_handler(Garden, Text(equals="Garden of Joy"))
dp.register_message_handler(Shattered, Text(equals="The Shattered Square"))
dp.register_message_handler(Following_maps3, Text(equals="Following maps3️⃣➡️"))
dp.register_message_handler(Previous_maps1, Text(equals="⬅️1️⃣Previous maps"))
dp.register_message_handler(Previous_maps2, Text(equals="⬅️2️⃣Previous maps"))
######################___PERK__BUILDS___################################
dp.register_callback_query_handler(perk_builds, text='description_sb1')
dp.register_callback_query_handler(perk_builds, text='next->2')
dp.register_callback_query_handler(perk_builds, text='description_sb2')
dp.register_callback_query_handler(perk_builds, text='1<-previous')
dp.register_callback_query_handler(perk_builds, text='next->3')
dp.register_callback_query_handler(perk_builds, text='description_sb3')
dp.register_callback_query_handler(perk_builds, text='2<-previous')
dp.register_callback_query_handler(perk_builds, text='description_kb1')
dp.register_callback_query_handler(perk_builds, text='next_kb->2')
dp.register_callback_query_handler(perk_builds, text='description_kb2')
dp.register_callback_query_handler(perk_builds, text='1<-previous_kb')
dp.register_callback_query_handler(perk_builds, text='next_kb->3')
dp.register_callback_query_handler(perk_builds, text='description_kb3')
dp.register_callback_query_handler(perk_builds, text='2<-previous_kb')
###############################___NEWS___################################
dp.register_callback_query_handler(news, text='read more_n1')
dp.register_callback_query_handler(news, text='next_n1->')
dp.register_callback_query_handler(news, text='<-previous_n2')
dp.register_callback_query_handler(news, text='next_n2->')
dp.register_callback_query_handler(news, text='read more_n2')
dp.register_callback_query_handler(news, text='<-previous_n3')
dp.register_callback_query_handler(news, text='next_n3->')
dp.register_callback_query_handler(news, text='read more_n3')
dp.register_callback_query_handler(news, text='<-previous_n4')
dp.register_callback_query_handler(news, text='next_n4->')
dp.register_callback_query_handler(news, text='read more_n4')
dp.register_callback_query_handler(news, text='<-previous_n5')
dp.register_callback_query_handler(news, text='next_n5->')
dp.register_callback_query_handler(news, text='read more_n5')
dp.register_callback_query_handler(news, text='<-previous_n6')
dp.register_callback_query_handler(news, text='next_n6->')
dp.register_callback_query_handler(news, text='read more_n6')
dp.register_callback_query_handler(news, text='<-previous_n7')
dp.register_callback_query_handler(news, text='next_n7->')
dp.register_callback_query_handler(news, text='read more_n7')
dp.register_callback_query_handler(news, text='<-previous_n8')
dp.register_callback_query_handler(news, text='next_n8->')
dp.register_callback_query_handler(news, text='read more_n8')
dp.register_callback_query_handler(news, text='<-previous_n9')
dp.register_callback_query_handler(news, text='next_n9->')
dp.register_callback_query_handler(news, text='read more_n9')
dp.register_callback_query_handler(news, text='<-previous_n10')
dp.register_callback_query_handler(news, text='read more_n10')
###############################___LEAKS___################################
dp.register_callback_query_handler(leaks, text='read more_n1_l')
dp.register_callback_query_handler(leaks, text='next_n1->_l')
dp.register_callback_query_handler(leaks, text='<-previous_n2_l')
dp.register_callback_query_handler(leaks, text='next_n2->_l')
dp.register_callback_query_handler(leaks, text='read more_n2_l')
dp.register_callback_query_handler(leaks, text='<-previous_n3_l')
dp.register_callback_query_handler(leaks, text='next_n3->_l')
dp.register_callback_query_handler(leaks, text='read more_n3_l')
dp.register_callback_query_handler(leaks, text='<-previous_n4_l')
dp.register_callback_query_handler(leaks, text='next_n4->_l')
dp.register_callback_query_handler(leaks, text='read more_n4_l')
dp.register_callback_query_handler(leaks, text='<-previous_n5_l')
dp.register_callback_query_handler(leaks, text='next_n5->_l')
dp.register_callback_query_handler(leaks, text='read more_n5_l')
dp.register_callback_query_handler(leaks, text='<-previous_n6_l')
dp.register_callback_query_handler(leaks, text='next_n6->_l')
dp.register_callback_query_handler(leaks, text='read more_n6_l')
dp.register_callback_query_handler(leaks, text='<-previous_n7_l')
dp.register_callback_query_handler(leaks, text='next_n7->_l')
dp.register_callback_query_handler(leaks, text='read more_n7_l')
dp.register_callback_query_handler(leaks, text='<-previous_n8_l')
dp.register_callback_query_handler(leaks, text='next_n8->_l')
dp.register_callback_query_handler(leaks, text='read more_n8_l')
dp.register_callback_query_handler(leaks, text='<-previous_n9_l')
dp.register_callback_query_handler(leaks, text='next_n9->_l')
dp.register_callback_query_handler(leaks, text='read more_n9_l')
dp.register_callback_query_handler(leaks, text='<-previous_n10_l')
dp.register_callback_query_handler(leaks, text='read more_n10_l')
###############################___KILLER TIER LIST___################################
dp.register_callback_query_handler(killer_tier_list, text='NURSE')
dp.register_callback_query_handler(killer_tier_list, text='BLIGHT')
dp.register_callback_query_handler(killer_tier_list, text='SPIRIT')
dp.register_callback_query_handler(killer_tier_list, text='ARTIST')
dp.register_callback_query_handler(killer_tier_list, text='PLAGUE')
dp.register_callback_query_handler(killer_tier_list, text='ONI')
dp.register_callback_query_handler(killer_tier_list, text='EXECUTIONER')
dp.register_callback_query_handler(killer_tier_list, text='MASTERMIND')
dp.register_callback_query_handler(killer_tier_list, text='HUNTERESS')
dp.register_callback_query_handler(killer_tier_list, text='HAG')
dp.register_callback_query_handler(killer_tier_list, text='TWINS')
dp.register_callback_query_handler(killer_tier_list, text='CENOBITE')
dp.register_callback_query_handler(killer_tier_list, text='CANIBAL')
dp.register_callback_query_handler(killer_tier_list, text='DEMOGORGON')
dp.register_callback_query_handler(killer_tier_list, text='DEADSLINGER')
dp.register_callback_query_handler(killer_tier_list, text='NEMESIS')
dp.register_callback_query_handler(killer_tier_list, text='DREDGE')
dp.register_callback_query_handler(killer_tier_list, text='HILLBILLY')
dp.register_callback_query_handler(killer_tier_list, text='TRICKSTER')
dp.register_callback_query_handler(killer_tier_list, text='DOCTOR')
dp.register_callback_query_handler(killer_tier_list, text='LEGION')
dp.register_callback_query_handler(killer_tier_list, text='GHOSTFACE')
dp.register_callback_query_handler(killer_tier_list, text='PIG')
dp.register_callback_query_handler(killer_tier_list, text='WRAITH')
dp.register_callback_query_handler(killer_tier_list, text='CLOWN')
dp.register_callback_query_handler(killer_tier_list, text='NIGHTMARE')
dp.register_callback_query_handler(killer_tier_list, text='SHAPE')
dp.register_callback_query_handler(killer_tier_list, text='ONRYO')
dp.register_callback_query_handler(killer_tier_list, text='TRAPPER')
dp.register_callback_query_handler(killer_tier_list, text='2next')
dp.register_callback_query_handler(killer_tier_list, text='1BACK')
dp.register_callback_query_handler(killer_tier_list, text='3next')
dp.register_callback_query_handler(killer_tier_list, text='2BACK')
dp.register_callback_query_handler(killer_tier_list, text='4next')
dp.register_callback_query_handler(killer_tier_list, text='3BACK')
dp.register_callback_query_handler(killer_tier_list, text='3BACK')
dp.register_callback_query_handler(killer_tier_list, text='For fun')
dp.register_callback_query_handler(killer_tier_list, text='For beginners')
##################################___ART___################################
dp.register_callback_query_handler(art, text='yes')
dp.register_callback_query_handler(art, text='no')
dp.register_callback_query_handler(art, text='next_art')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)