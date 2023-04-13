import json

from keyboards.keyboard_news import *
from keyboards.keyboard_guides import *

with open('news/leaks_dict.json', 'r') as file:
    datal = json.load(file)


async def leaks(callback: types.CallbackQuery):
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