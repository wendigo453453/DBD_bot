from aiogram.dispatcher.filters import Text
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto


from keyboards.keyboard_guides import *


from message_handlers.map_clock_callouts import *
TOKEN_API = "6019776081:AAHyWrJ0LZGakPXKN05Vw_-N2g1iuxNcTUk"


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(Text(equals="🗺Map clock callouts🗺"))
async def Map_clock_callouts(message: types.Message):
    await message.answer(text="choose the map⬇️",
                         reply_markup=kb_clock_callouts)

The_MacMillan_Estate = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452923527/ECEA60DE8BE47D9E5FEB935D9021D1CBDB90A573/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452923997/F2101227328E079ABCAB8B1556424414B23EA40E/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452924441/86B245CF751F9CC750587A2EECDACB598286E00C/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452924836/624C2E98127FA106FB2F8627925753A2D51BB15F/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452925877/B293BDCD3AF26889A5EC7CEA8FF329D617A02229/')
    ]
@dp.message_handler(Text(equals="The MacMillan Estate"))
async def MacMillan(message: types.Message):
    await message.answer(text="There The MacMillan Estate maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=The_MacMillan_Estate)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts)

Coldwind_Farm = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/2035099495173903670/53287664D701D424AF43C936F959B5971CA9A3E3/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452919193/74102E00A93DB4EFD32B6563A80A11D5FC6AD369/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/2035099495173903979/F48976E276D187E9FD09CB8AFE56B0B89B2E9634/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/2035099495173904322/832EAAF4E773A5ADD76832816C07645529D9D304/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452920509/5B0A1E55BDABBB5BAA44C1BF3AA7492AB8315DF1/')
    ]
@dp.message_handler(Text(equals="Coldwind Farm"))
async def Coldwind(message: types.Message):
    await message.answer(text="There The Coldwind Farm maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Coldwind_Farm)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts)

Autohaven_Wreckers = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452915619/4466B21401EB560B9C92194A936BD7628D4986DA/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452915916/6AC5E4C74EDB69A6B1DF4B6E09A2FF7E612AB0A7/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452916334/46A29516FA99D6E09DB0EB65BDB81ED39DC65DCA/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452917122/457BF869BFCC70558446F179846F79ACCD0C4C36/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452917467/22FB927AB168F0DC7AED7BEBF41F9900D4C4FE7D/')
    ]
@dp.message_handler(Text(equals="Autohaven Wreckers"))
async def Autohaven(message: types.Message):
    await message.answer(text="There The Autohaven Wreckers maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Autohaven_Wreckers)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts)

Crotus_Prenn_Asylum  = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452920989/73EDFE8271666F2B4DDD69744B5BA8B7542AE052/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452921472/2CCD7E8ED122FB3D6DFB4C93E44512451102FB62/')
    ]
@dp.message_handler(Text(equals="Crotus Prenn Asylum"))
async def Crotus(message: types.Message):
    await message.answer(text="There The Crotus Prenn Asylum  maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Crotus_Prenn_Asylum)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts)

@dp.message_handler(Text(equals="Haddonfield"))
async def Haddonfield(message: types.Message):
    await message.answer(text="There The Haddonfield maps⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132452922757/0C1155F5A5262CE7ECBDAD3BF81BF622F65E5BC7/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts)

Backwater_Swamp = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452918078/6F3910BF120F1A67AED3A97738AD6AC58C9DC151/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452917783/E25A8E7B1945131E27FA486E4C17EA071393B51B/')
    ]
@dp.message_handler(Text(equals="Backwater Swamp"))
async def Swamp(message: types.Message):
    await message.answer(text="There The Backwater Swamp maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Backwater_Swamp)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts)

@dp.message_handler(Text(equals="Lerys Memorial Institute"))
async def Institute(message: types.Message):
    await message.answer(text="There The Lerys Memorial Institute maps⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132452923131/B1460C49BC70113B97DBFDADDEA6FF01259F8C2B/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts)

Red_Forest = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452927097/6602D4E026635CF7AC71F7B95066B67B75947467/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452927859/A9623893B08E2A2D3A069614AF85DDE102C52D53/')
    ]
@dp.message_handler(Text(equals="Red Forest"))
async def Red__Forest(message: types.Message):
    await message.answer(text="There The Red Forest maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Red_Forest)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts2)

@dp.message_handler(Text(equals="Following maps2️⃣➡️"))
async def Following_maps2(message: types.Message):
    await message.answer(text="choose the map⬇️",
                         reply_markup=kb_clock_callouts2)

Badham = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452928421/AE6309F5297D6E1E299FBD89809D79953475602D/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452928854/F63BBC8331B675179BCE4020904FFFF9A4E83BA6/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452929378/DBACA23D17F29E815F5A703BECE5BE5E160829E4/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452929860/B0E81E64FB9826E0DA085AA7AA52FB51D85C6A83/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452930298/8E13F490C0601BED799958D81E1819A9464BCF4B/'),
    ]
@dp.message_handler(Text(equals="Badham"))
async def Badham(message: types.Message):
    await message.answer(text="There The Badham maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Badham)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts2)

@dp.message_handler(Text(equals="Gideon Meat Plant"))
async def Gideon(message: types.Message):
    await message.answer(text="There The Gideon Meat Plant map⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132464322936/FE2FED9E8216EE6D960A9D3E3939EF3B89501375/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts2)

Yamaoka_Estate = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452931202/D9CB9A7E2E77BED8CDE71469830B57F19BB56AEB/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132452931557/FEE6D7B482C6DA5FE5D7CC0EC82910109F4C3855/')
    ]
@dp.message_handler(Text(equals="Yamaoka Estate"))
async def Yamaoka(message: types.Message):
    await message.answer(text="There The Family Residence maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Yamaoka_Estate)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts2)

@dp.message_handler(Text(equals="Ormond"))
async def Ormond(message: types.Message):
    await message.answer(text="There The Ormond map⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132452926570/3D72151CE266FC7207498BF081D6131F87ED64BA/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts2)

@dp.message_handler(Text(equals="Dead Dawg Saloon"))
async def Saloon(message: types.Message):
    await message.answer(text="There The Dead Dawg Saloon map⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/2035097135958922950/09F9036EEE52D068262C4A5AD96A993F1858AC37/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts2)

@dp.message_handler(Text(equals="Silent Hill"))
async def Hill(message: types.Message):
    await message.answer(text="There The Silent Hill map⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132464322046/798A13979912FF8FD65F68546A817DD3353A2493/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts2)

Raccoon_City = [
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132464318769/A7F17C0A373533D24FCD20FDC3BDFC8566A97EB4/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132464319860/8271C87DDC0184D141219406BFF918AD0F738787/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132464320471/F5952B69465B3043BDC3F6CBDBE4225D697D28CE/'),
        types.InputMediaPhoto('https://steamuserimages-a.akamaihd.net/ugc/5100921132464321346/706CCD99C259E3679BE3DDDCC84B688BA4DFAE4D/'),
    ]
@dp.message_handler(Text(equals="Raccoon City"))
async def Raccoon(message: types.Message):
    await message.answer(text="There The Raccoon City  maps⬇️")
    await bot.send_media_group(chat_id=message.chat.id,
                               media=Raccoon_City)
    await message.answer(text="choose the next map⬇️",
                             reply_markup=kb_clock_callouts2)

@dp.message_handler(Text(equals="⬅️Previous maps"))
async def Previous_maps(message: types.Message):
    await message.answer(text="choose the map⬇️",
                         reply_markup=kb_clock_callouts)

@dp.message_handler(Text(equals="Following maps➡️"))
async def Following_maps(message: types.Message):
    await message.answer(text="choose the map⬇️",
                         reply_markup=kb_clock_callouts3)

@dp.message_handler(Text(equals="Eyrie of Crows"))
async def Eyrie(message: types.Message):
    await message.answer(text="There The Eyrie of Crows map⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132464304362/70984D62890218E2B5088749ECAB18726D670D89/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts3)

@dp.message_handler(Text(equals="Garden of Joy"))
async def Garden(message: types.Message):
    await message.answer(text="There The Garden of Joy map⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132452930778/2D16451F38BD57953E81DFEB16985F06F8F59833/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts3)

@dp.message_handler(Text(equals="The Shattered Square"))
async def Shattered(message: types.Message):
    await message.answer(text="There The Shattered Square map⬇️")
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://steamuserimages-a.akamaihd.net/ugc/5100921132452918374/73D9B54E46BD21B241A9A324AEDD3DEE80BDD6CA/",
                         caption="choose the next map⬇️",
                         reply_markup=kb_clock_callouts3)

@dp.message_handler(Text(equals="Following maps3️⃣➡️"))
async def Following_maps3(message: types.Message):
    await message.answer(text="choose the map⬇️",
                         reply_markup=kb_clock_callouts3)

@dp.message_handler(Text(equals="⬅️1️⃣Previous maps"))
async def Previous_maps1(message: types.Message):
    await message.answer(text="choose the map⬇️",
                         reply_markup=kb_clock_callouts)

@dp.message_handler(Text(equals="⬅️2️⃣Previous maps"))
async def Previous_maps2(message: types.Message):
    await message.answer(text="choose the map⬇️",
                         reply_markup=kb_clock_callouts2)

@dp.message_handler(Text(equals="⬅️back to 📖GUIDES📖"))
async def back_to_GUIDES(message: types.Message):
    await message.answer(text="choose what you want too see",
                         reply_markup=kb_guide)