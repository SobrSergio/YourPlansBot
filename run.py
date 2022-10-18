from db import db_start, check_time_function, every_day_week
from handlers import client, client_callbackes
from states import states
from create_bot import dp
from aiogram import executor
import asyncio
import logging





async def on_startup(_):
    await db_start()
    asyncio.create_task(check_time_function())
    asyncio.create_task(every_day_week())

    
client.register_message(dp)
states.register_states_client(dp)
client_callbackes.register_call_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
