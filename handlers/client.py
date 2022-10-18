from aiogram import types, Dispatcher
from create_bot import bot 
from keyboard.client_buttons import *
from states.create_states import *
from keyboard.client_inline_buttons import *
from db import create_profile, give_week_today, check_user
from datetime import datetime





async def default_commands(message: types.Message):
    if message.text == '/start':
        await message.delete()
        check = await check_user(user_id=message.from_user.id)
        if check == 1:
            await bot.send_message(message.chat.id, '✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b>', parse_mode='HTML', reply_markup=main_frame)
        else:
            await create_profile(user_id=message.from_user.id)
            await bot.send_message(message.chat.id, """❓ <b>Как пользоваться ботом?</b>
                               
/start - Главная кнопка со всеми основными функциями.

/help - Вызов инструкции по использованию бота.


Все Кнопки в боте:

🆘 <b>Помощь</b> - Показывает контакты для связи с создателем бота.

📝 <b>Добав. напомин.</b> - кнопка добавление напоминания. В разных сообщениях нужно написать название, потом время. Напоминание можно создать только на сегодняшний день.

📝 <b>Удал. напомин.</b> - кнопка удаления напоминания. В одном сообщении написать название и время.

📔 <b>План на неделю</b> - кнопка показывающая все дни недели на выбор (Пн, Вт, Ср, Чт, Пт, Cб, Вс). Нажатие на одну из кнопок, выведет ваш план на неделю.

📔 <b>Изменить неделю</b> - кнопка для измение твоей недели (добавлять, изменять, удалять планы на каждый из дней недели)

🗓️ <b>План на сегодня</b> - кнопка, которая выдает план на сегодняшний день недели.


""", parse_mode='HTML')
            await bot.send_message(message.chat.id, '✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b>', parse_mode='HTML', reply_markup=main_frame)
        
        
    elif message.text == '/help':
        await message.delete()
        await bot.send_message(message.chat.id, """❓ <b>Как пользоваться ботом?</b>
                               
/start - Главная кнопка со всеми основными функциями.

/help - Вызов инструкции по использованию бота.


Все Кнопки в боте:

🆘 <b>Помощь</b> - Показывает контакты для связи с создателем бота.

📝 <b>Добав. напомин.</b> - кнопка добавление напоминания. В разных сообщениях нужно написать название, потом время. Напоминание можно создать только на сегодняшний день.

📝 <b>Удал. напомин.</b> - кнопка удаления напоминания. В одном сообщении написать название и время.

📔 <b>План на неделю</b> - кнопка показывающая все дни недели на выбор (Пн, Вт, Ср, Чт, Пт, Cб, Вс). Нажатие на одну из кнопок, выведет ваш план на неделю.

📔 <b>Изменить неделю</b> - кнопка для измение твоей недели (добавлять, изменять, удалять планы на каждый из дней недели)

🗓️ <b>План на сегодня</b> - кнопка, которая выдает план на сегодняшний день недели.
""", parse_mode='HTML')





async def send_message(user_id, text_message, time):
    await bot.send_message(chat_id=user_id, text=f"""
❗️<b>Напоминание</b>❗️

{text_message}

Время: {time}""", parse_mode='HTML')
        




async def answer_mesage(user_id):
    now = datetime.now()
    weekday = str(datetime.weekday(now))
    list = await give_week_today(user_id=user_id, week=weekday)
    await bot.send_message(chat_id=user_id, text=f"""☀️ <b>Доброе утро!</b> Вот твой план на сегодня!
                           
{list}""")





def register_message(dp: Dispatcher):
    
    dp.register_message_handler(default_commands, commands=['start', 'help'])
    