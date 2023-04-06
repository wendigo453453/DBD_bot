from aiogram.dispatcher.filters import Text
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto
import hashlib
import json
import random
import sqlite_db

from keyboards.keyboard import *
from keyboards.keyboard_perk_builds import *
from keyboards.keyboard_sos import *
from keyboards.keyboard_art import *
from keyboards.keyboard_news import *

from db import Database

TOKEN_API = "6019776081:AAHyWrJ0LZGakPXKN05Vw_-N2g1iuxNcTUk"


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


with open('news/news_dict.json', 'r') as file:
    data = json.load(file)
with open('news/leaks_dict.json', 'r') as file:
    datal = json.load(file)
with open('art.json') as f:
    dataa = json.load(f)

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


#################################### SHRINE OF SECRETS ####################################

@dp.message_handler(Text(equals="🛒SHRINE OF SECRETS🛒"))
async def send_image(message: types.Message):
    if message.chat.type == 'private':
        if not dbu.user_exists(message.from_user.id):
            dbu.add_user(message.from_user.id)
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
    if message.chat.type == 'private':
        if not dbu.user_exists(message.from_user.id):
            dbu.add_user(message.from_user.id)
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
    if message.chat.type == 'private':
        if not dbu.user_exists(message.from_user.id):
            dbu.add_user(message.from_user.id)
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
    if message.chat.type == 'private':
        if not dbu.user_exists(message.from_user.id):
            dbu.add_user(message.from_user.id)
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


pick_f = True
###################################__CB__PERK_BUILD#####################################

@dp.callback_query_handler()
async def some_callback_handler(callback: types.CallbackQuery):
    if callback.data == 'description_sb1':
        sb1 = await sqlite_db.surv_b1()
        for survivors_builds in sb1:
            await callback.message.answer(text=survivors_builds[3])
            await callback.answer()
    if callback.data == 'next->2':
        sb2 = await sqlite_db.surv_b2()
        for survivors_builds in sb2:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_sb2)
    if callback.data == 'description_sb2':
        sb2 = await sqlite_db.surv_b2()
        for survivors_builds in sb2:
            await callback.message.answer(text=survivors_builds[3])
            await callback.answer()
    if callback.data == '1<-previous':
        sb1 = await sqlite_db.surv_b1()
        for survivors_builds in sb1:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_sb1)
    if callback.data == 'next->3':
        sb3 = await sqlite_db.surv_b3()
        for survivors_builds in sb3:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_sb3)
    if callback.data == 'description_sb3':
        sb3 = await sqlite_db.surv_b3()
        for survivors_builds in sb3:
            await callback.message.answer(text=survivors_builds[3])
            await callback.answer()
    if callback.data == '2<-previous':
        sb2 = await sqlite_db.surv_b2()
        for survivors_builds in sb2:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_sb2)

    if callback.data == 'description_kb1':
        kb1 = await sqlite_db.killer_b1()
        for survivors_builds in kb1:
            await callback.message.answer(text=survivors_builds[3])
            await callback.answer()

    if callback.data == 'next_kb->2':
        kb2 = await sqlite_db.killer_b2()
        for survivors_builds in kb2:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_kb2)
    if callback.data == 'description_kb2':
        kb2 = await sqlite_db.killer_b2()
        for survivors_builds in kb2:
            await callback.message.answer(text=survivors_builds[3])
            await callback.answer()
    if callback.data == '1<-previous_kb':
        kb1 = await sqlite_db.killer_b1()
        for survivors_builds in kb1:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_kb1)
    if callback.data == 'next_kb->3':
        kb3 = await sqlite_db.killer_b3()
        for survivors_builds in kb3:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_kb3)
    if callback.data == 'description_kb3':
        kb3 = await sqlite_db.killer_b3()
        for survivors_builds in kb3:
            await callback.message.answer(text=survivors_builds[3])
            await callback.answer()
    if callback.data == '2<-previous_kb':
        kb2 = await sqlite_db.killer_b2()
        for survivors_builds in kb2:
            await callback.message.edit_media(types.InputMedia(media=survivors_builds[1],
                                                               type='photo',
                                                               caption=survivors_builds[2]),
                                              reply_markup=ikb_kb2)

    ###################################__CB__NEWS__################################################

    if callback.data == 'read more_n1':
        await callback.message.answer(text=(data['0']['news_text']))
        await callback.answer()
    if callback.data == 'next_n1->':
        await callback.message.edit_media(types.InputMedia(media=(data['1']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['1']['news_date_time'])}📆\n📃{(data['1']['news_title'])}📃\n\n📑{(data['1']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news2)
        await callback.answer()

    if callback.data == '<-previous_n2':
        await callback.message.edit_media(types.InputMedia(media=(data['0']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['0']['news_date_time'])}📆\n📃{(data['0']['news_title'])}📃\n\n📑{(data['0']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news1)
    if callback.data == 'next_n2->':
        await callback.message.edit_media(types.InputMedia(media=(data['2']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['2']['news_date_time'])}📆\n📃{(data['2']['news_title'])}📃\n\n📑{(data['2']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news3)
    if callback.data == 'read more_n2':
        await callback.message.answer(text=(data['1']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n3':
        await callback.message.edit_media(types.InputMedia(media=(data['1']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['1']['news_date_time'])}📆\n📃{(data['1']['news_title'])}📃\n\n📑{(data['1']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news2)
    if callback.data == 'next_n3->':
        await callback.message.edit_media(types.InputMedia(media=(data['3']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['3']['news_date_time'])}📆\n📃{(data['3']['news_title'])}📃\n\n📑{(data['3']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news4)
    if callback.data == 'read more_n3':
        await callback.message.answer(text=(data['2']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n4':
        await callback.message.edit_media(types.InputMedia(media=(data['2']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['2']['news_date_time'])}📆\n📃{(data['2']['news_title'])}📃\n\n📑{(data['2']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news3)
    if callback.data == 'next_n4->':
        await callback.message.edit_media(types.InputMedia(media=(data['4']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['4']['news_date_time'])}📆\n📃{(data['4']['news_title'])}📃\n\n📑{(data['4']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news5)
    if callback.data == 'read more_n4':
        await callback.message.answer(text=(data['3']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n5':
        await callback.message.edit_media(types.InputMedia(media=(data['3']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['3']['news_date_time'])}📆\n📃{(data['3']['news_title'])}📃\n\n📑{(data['3']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news4)
    if callback.data == 'next_n5->':
        await callback.message.edit_media(types.InputMedia(media=(data['5']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['5']['news_date_time'])}📆\n📃{(data['5']['news_title'])}📃\n\n📑{(data['5']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news6)
    if callback.data == 'read more_n5':
        await callback.message.answer(text=(data['4']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n6':
        await callback.message.edit_media(types.InputMedia(media=(data['4']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['4']['news_date_time'])}📆\n📃{(data['4']['news_title'])}📃\n\n📑{(data['4']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news5)
    if callback.data == 'next_n6->':
        await callback.message.edit_media(types.InputMedia(media=(data['6']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['6']['news_date_time'])}📆\n📃{(data['6']['news_title'])}📃\n\n📑{(data['6']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news7)
    if callback.data == 'read more_n6':
        await callback.message.answer(text=(data['5']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n7':
        await callback.message.edit_media(types.InputMedia(media=(data['5']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['5']['news_date_time'])}📆\n📃{(data['5']['news_title'])}📃\n\n📑{(data['5']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news6)
    if callback.data == 'next_n7->':
        await callback.message.edit_media(types.InputMedia(media=(data['7']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['7']['news_date_time'])}📆\n📃{(data['7']['news_title'])}📃\n\n📑{(data['7']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news8)
    if callback.data == 'read more_n7':
        await callback.message.answer(text=(data['6']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n8':
        await callback.message.edit_media(types.InputMedia(media=(data['6']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['6']['news_date_time'])}📆\n📃{(data['6']['news_title'])}📃\n\n📑{(data['6']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news7)
    if callback.data == 'next_n8->':
        await callback.message.edit_media(types.InputMedia(media=(data['8']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['8']['news_date_time'])}📆\n📃{(data['8']['news_title'])}📃\n\n📑{(data['8']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news9)
    if callback.data == 'read more_n8':
        await callback.message.answer(text=(data['7']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n9':
        await callback.message.edit_media(types.InputMedia(media=(data['7']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['7']['news_date_time'])}📆\n📃{(data['7']['news_title'])}📃\n\n📑{(data['7']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news8)
    if callback.data == 'next_n9->':
        await callback.message.edit_media(types.InputMedia(media=(data['9']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['9']['news_date_time'])}📆\n📃{(data['9']['news_title'])}📃\n\n📑{(data['9']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news10)
    if callback.data == 'read more_n9':
        await callback.message.answer(text=(data['8']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n10':
        await callback.message.edit_media(types.InputMedia(media=(data['8']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(data['8']['news_date_time'])}📆\n📃{(data['8']['news_title'])}📃\n\n📑{(data['8']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news9)
    if callback.data == 'read more_n10':
        await callback.message.answer(text=(data['9']['news_text']))
        await callback.answer()

    ###################################__CB__LEAKS__################################################

    if callback.data == 'read more_n1_l':
        await callback.message.answer(text=(datal['10']['news_text']))
        await callback.answer()
    if callback.data == 'next_n1->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['11']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['11']['news_date_time'])}📆\n📃{(datal['11']['news_title'])}📃\n\n📑{(datal['11']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news2_l)
        await callback.answer()

    if callback.data == '<-previous_n2_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['10']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['10']['news_date_time'])}📆\n📃{(datal['10']['news_title'])}📃\n\n📑{(datal['10']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news1_l)
    if callback.data == 'next_n2->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['12']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['12']['news_date_time'])}📆\n📃{(datal['12']['news_title'])}📃\n\n📑{(datal['12']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news3_l)
    if callback.data == 'read more_n2_l':
        await callback.message.answer(text=(datal['11']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n3_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['11']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['11']['news_date_time'])}📆\n📃{(datal['11']['news_title'])}📃\n\n📑{(datal['11']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news2_l)
    if callback.data == 'next_n3->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['13']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['13']['news_date_time'])}📆\n📃{(datal['13']['news_title'])}📃\n\n📑{(datal['13']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news4_l)
    if callback.data == 'read more_n3_l':
        await callback.message.answer(text=(datal['12']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n4_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['12']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['12']['news_date_time'])}📆\n📃{(datal['12']['news_title'])}📃\n\n📑{(datal['12']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news3_l)
    if callback.data == 'next_n4->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['14']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['14']['news_date_time'])}📆\n📃{(datal['14']['news_title'])}📃\n\n📑{(datal['14']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news5_l)
    if callback.data == 'read more_n4_l':
        await callback.message.answer(text=(datal['13']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n5_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['13']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['13']['news_date_time'])}📆\n📃{(datal['13']['news_title'])}📃\n\n📑{(datal['13']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news4_l)
    if callback.data == 'next_n5->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['15']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['15']['news_date_time'])}📆\n📃{(datal['15']['news_title'])}📃\n\n📑{(datal['15']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news6_l)
    if callback.data == 'read more_n5_l':
        await callback.message.answer(text=(datal['14']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n6_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['14']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['14']['news_date_time'])}📆\n📃{(datal['14']['news_title'])}📃\n\n📑{(datal['14']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news5_l)
    if callback.data == 'next_n6->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['16']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['16']['news_date_time'])}📆\n📃{(datal['16']['news_title'])}📃\n\n📑{(datal['16']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news7_l)
    if callback.data == 'read more_n6_l':
        await callback.message.answer(text=(datal['15']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n7_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['15']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['15']['news_date_time'])}📆\n📃{(datal['15']['news_title'])}📃\n\n📑{(datal['15']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news6_l)
    if callback.data == 'next_n7->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['17']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['17']['news_date_time'])}📆\n📃{(datal['17']['news_title'])}📃\n\n📑{(datal['17']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news8_l)
    if callback.data == 'read more_n7_l':
        await callback.message.answer(text=(datal['16']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n8_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['16']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['16']['news_date_time'])}📆\n📃{(datal['16']['news_title'])}📃\n\n📑{(datal['16']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news7_l)
    if callback.data == 'next_n8->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['18']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['18']['news_date_time'])}📆\n📃{(datal['18']['news_title'])}📃\n\n📑{(datal['18']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news9_l)
    if callback.data == 'read more_n8_l':
        await callback.message.answer(text=(datal['17']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n9_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['17']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['17']['news_date_time'])}📆\n📃{(datal['17']['news_title'])}📃\n\n📑{(datal['17']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news8_l)
    if callback.data == 'next_n9->_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['19']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['19']['news_date_time'])}📆\n📃{(datal['19']['news_title'])}📃\n\n📑{(datal['19']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news10_l)
    if callback.data == 'read more_n9_l':
        await callback.message.answer(text=(datal['18']['news_text']))
        await callback.answer()

    if callback.data == '<-previous_n10_l':
        await callback.message.edit_media(types.InputMedia(media=(datal['18']['news_pictures']),
                                                           type='photo',
                                                           caption=f"📆Date{(datal['18']['news_date_time'])}📆\n📃{(datal['18']['news_title'])}📃\n\n📑{(datal['18']['news_description'])}📑"),
                                          reply_markup=ikb_dbd_news9_l)
    if callback.data == 'read more_n10_l':
        await callback.message.answer(text=(datal['19']['news_text']))
        await callback.answer()

####################################___CB__ART___############################################################

    global pick_f
    if callback.data == 'yes':
        if not pick_f:
            await callback.answer(text='good')
            pick_f = not pick_f
        else:
            await callback.answer(text='you have already appreciated')
    if callback.data == 'no':
        if not pick_f:
            await callback.answer(text='Too bad(')
            pick_f = not pick_f
        else:
            await callback.answer(text='you have already appreciated')
    if callback.data == 'next_art':
        random_link = random.choice(dataa['links'])
        await callback.message.edit_media(types.InputMedia(media=(random_link['address']),
                                                               type='photo',
                                                               caption="how do you like this art?"),
                                              reply_markup=ikb_random_art)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)