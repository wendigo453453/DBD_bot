from aiogram.dispatcher.filters import Text
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto
import random


from keyboards.keyboard_art import *
from keyboards.keyboard_news import *
from keyboards.keyboard_guides import *

with open('art.json') as f:
    dataa = json.load(f)
pick_f = False
async def art(callback: types.CallbackQuery):
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
        pick_f = False
        random_link = random.choice(dataa['links'])
        await callback.message.edit_media(types.InputMedia(media=(random_link['address']),
                                                               type='photo',
                                                               caption="how do you like this art?"),
                                                               reply_markup=ikb_random_art)