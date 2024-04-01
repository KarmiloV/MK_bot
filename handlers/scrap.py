from aiogram import types, Dispatcher
from config import bot
from database import db


from scraping.asyncscrap import Asyncscrap


async def scrap(call: types.CallbackQuery):
    datab = db.Database()
    scrapper = Asyncscrap()
    links = await scrapper.get_page()
    for link in links[0][:5]:
        datab.insert_scrap_table(link=link)
        await bot.send_message(chat_id=call.from_user.id, text=link)




def register_scrap(dp: Dispatcher):
    dp.register_callback_query_handler(scrap, lambda call: call.data == 'scrap')