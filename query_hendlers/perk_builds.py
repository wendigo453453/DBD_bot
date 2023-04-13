from aiogram.dispatcher.filters import Text
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto
import hashlib
import json
import random
import sqlite_db

from keyboards.keyboard_perk_builds import *
from keyboards.keyboard_guides import *

async def perk_builds(callback: types.CallbackQuery):
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