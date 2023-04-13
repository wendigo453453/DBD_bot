from aiogram.dispatcher.filters import Text
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto

from keyboards.keyboard_guides import *



async def killer_tier_list(callback: types.CallbackQuery):
    if callback.data == 'NURSE':
        media = types.InputMedia(
            media='https://i.ibb.co/z5b5w7L/Screenshot-14.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == 'BLIGHT':
        media = types.InputMedia(
            media='https://i.ibb.co/hs7Nr8n/Screenshot-15.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == 'SPIRIT':
        media = types.InputMedia(
            media='https://i.ibb.co/mvLbptB/Screenshot-16.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == 'ARTIST':
        media = types.InputMedia(
            media='https://i.ibb.co/pPM1R9R/Screenshot-17.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == 'PLAGUE':
        media = types.InputMedia(
            media='https://i.ibb.co/x6YcXq5/Screenshot-18.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == 'ONI':
        media = types.InputMedia(
            media='https://i.ibb.co/zhVzL30/Screenshot-19.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == 'EXECUTIONER':
        media = types.InputMedia(
            media='https://i.ibb.co/X25wZBG/Screenshot-20.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == 'MASTERMIND':
        media = types.InputMedia(
            media='https://i.ibb.co/zJX5nfm/Screenshot-21.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == 'HUNTERESS':
        media = types.InputMedia(
            media='https://i.ibb.co/dPmXH9c/Screenshot-22.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == 'HAG':
        media = types.InputMedia(
            media='https://i.ibb.co/LdYt5sY/Screenshot-23.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == 'TWINS':
        media = types.InputMedia(
            media='https://i.ibb.co/rdpWZ6S/Screenshot-24.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == 'CENOBITE':
        media = types.InputMedia(
            media='https://i.ibb.co/y5mgrfZ/Screenshot-25.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == 'CANIBAL':
        media = types.InputMedia(
            media='https://i.ibb.co/Jd1MN3v/Screenshot-26.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == 'DEMOGORGON':
        media = types.InputMedia(
            media='https://i.ibb.co/643nyq3/Screenshot-27.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == 'DEADSLINGER':
        media = types.InputMedia(
            media='https://i.ibb.co/fDG2RxR/Screenshot-28.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'NEMESIS':
        media = types.InputMedia(
            media='https://i.ibb.co/N33CS3d/Screenshot-29.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'DREDGE':
        media = types.InputMedia(
            media='https://i.ibb.co/t45gHrG/Screenshot-30.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'HILLBILLY':
        media = types.InputMedia(
            media='https://i.ibb.co/wyQ5S04/Screenshot-31.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'TRICKSTER':
        media = types.InputMedia(
            media='https://i.ibb.co/RpWq9Qb/Screenshot-32.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'DOCTOR':
        media = types.InputMedia(
            media='https://i.ibb.co/vdzgwSq/Screenshot-33.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'LEGION':
        media = types.InputMedia(
            media='https://i.ibb.co/x54P9xG/Screenshot-34.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'GHOSTFACE':
        media = types.InputMedia(
            media='https://i.ibb.co/BNf1ZjS/Screenshot-35.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == 'PIG':
        media = types.InputMedia(
            media='https://i.ibb.co/d6CVj4r/Screenshot-36.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == 'WRAITH':
        media = types.InputMedia(
            media='https://i.ibb.co/RYQfvY2/Screenshot-37.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == 'CLOWN':
        media = types.InputMedia(
            media='https://i.ibb.co/bNvVKtg/Screenshot-38.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == 'NIGHTMARE':
        media = types.InputMedia(
            media='https://i.ibb.co/Rj7Mgzr/Screenshot-39.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == 'SHAPE':
        media = types.InputMedia(
            media='https://i.ibb.co/Mfvb6Hb/Screenshot-40.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == 'ONRYO':
        media = types.InputMedia(
            media='https://i.ibb.co/dP5ddGN/Screenshot-41.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == 'TRAPPER':
        media = types.InputMedia(
            media='https://i.ibb.co/C18Q0RS/Screenshot-42.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == '2next':
        media = types.InputMedia(
            media='https://i.ibb.co/1bvN0Zn/Screenshot-9.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == '1BACK':
        media = types.InputMedia(
            media='https://i.ibb.co/1bvN0Zn/Screenshot-9.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l)
    if callback.data == '3next':
        media = types.InputMedia(
            media='https://i.ibb.co/1bvN0Zn/Screenshot-9.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == '2BACK':
        media = types.InputMedia(
            media='https://i.ibb.co/1bvN0Zn/Screenshot-9.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l2)
    if callback.data == '4next':
        media = types.InputMedia(
            media='https://i.ibb.co/1bvN0Zn/Screenshot-9.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l4)
    if callback.data == '3BACK':
        media = types.InputMedia(
            media='https://i.ibb.co/1bvN0Zn/Screenshot-9.jpg',
            caption='You can see more information about individual killers using the button below⬇️'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_k_t_l3)
    if callback.data == 'For fun':
        media = types.InputMedia(
            media='https://i.ibb.co/P9qyjCn/Screenshot-6.jpg',
            caption='Here you can see survivor with the most fun perk too use.\nYou can also see which survivors i recomend too buy for a new player.'
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_fun_perk)
    if callback.data == 'For beginners':
        media = types.InputMedia(
            media='https://i.ibb.co/47n7bQV/Screenshot-5.jpg',
            caption="Here you can see which survivors i  recomend too buy for a new player. \nYou can also see survivor with the most fun perk too use⬇️"
        )
        await callback.message.edit_media(media=media, reply_markup=ikb_fun_perk)