import json
import random
import sqlite_db

from keyboards.keyboard import *
from keyboards.keyboard_perk_builds import *
from keyboards.keyboard_sos import *
from keyboards.keyboard_art import *
from keyboards.keyboard_news import *
from keyboards.keyboard_guides import *

from db import Database

with open('news/news_dict.json', 'r') as file:
    data = json.load(file)


async def news(callback: types.CallbackQuery):
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