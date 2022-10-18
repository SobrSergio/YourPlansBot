from datetime import datetime
from aiogram import types, Dispatcher
from create_bot import bot 
from aiogram.dispatcher.filters import Text
from keyboard.client_buttons import *
from states.create_states import *
from keyboard.client_inline_buttons import *
from db import alert_change_db_no, alert_change_db_yes, lists_event, give_week, give_week_today
from aiogram.dispatcher import FSMContext





async def main_inline(call: types.CallbackQuery):   
    
    
    if call.data == 'Timetable':
        await bot.edit_message_text(text='📔 <b>План на неделю</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=FullWeek)
       
    
    elif call.data == 'Event':
        await bot.edit_message_text(text="""📝 <b>Добавить напоминание</b>
                                                                                            
Напишите <b>название</b> напоминания""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoMain_frame)
        await AddEvent.text.set()
        
        
    elif call.data == 'Timetable_change':
        await bot.edit_message_text(text="""📔 <b>Изменить неделю</b>""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditFullWeek)
    
    
    elif call.data == 'Event_del':
        event = await lists_event(user_id=call.from_user.id)
        await bot.edit_message_text(text=f"""📝 <b>Удалить напоминание</b> 
                                                   
Напишите <b>текст и время</b> таким образом: Почистить зубы 7:00 

Ваши напоминания: 
{event}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoMain_frame)
        await DeleteEvent.time.set()
    
    
    elif call.data == 'Help':
        await bot.edit_message_text(text=
"""🆘 <b>Помощь</b>

Все контакты для обратной связи🧑‍💻:
Telegram - @SergeyManakhimov
Email - sergeymanakhimov@gmail.com
Instagram - @sergey_manakhimov""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoMain_frame)
    
    
    elif call.data == 'Today_timetable':
        now = datetime.now()
        weekday = str(datetime.weekday(now))
        list = await give_week_today(user_id=call.from_user.id, week=weekday)
        await bot.edit_message_text(text=f"""🗓️ <b>План на сегодня</b>
                                    
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoMain_frame)
    
    
    elif call.data == 'GoMain_menu':
         await bot.edit_message_text(text='✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b> ', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
    
    
    elif call.data == 'Alert_change':
        await bot.edit_message_text(text="""🔔 <b>Изменить уведомления</b>
                                    
По умолчанию: включено. При влключенном режиме, утром вам будет приходить ваш план на день.""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=Alert_yes_no)





async def alert_change(call: types.CallbackQuery):
    
    
    if call.data == 'Alert_yes':
        res = await alert_change_db_yes(user_id=call.from_user.id)
        if res == 1:
            await bot.edit_message_text(text="""✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b>

✅ Вы включили уведомления!""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
        else:
            await bot.edit_message_text(text="""✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b>

❌ У вас уже включены уведомления!""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
          
                
            
    elif call.data == 'Alert_no':
        res = await alert_change_db_no(user_id=call.from_user.id)
        if res == 1:
            await bot.edit_message_text(text="""✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b>

✅ Вы отключили уведомления!""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
        else:
            await bot.edit_message_text(text="""✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b>

❌ У вас уже были выключены уведомления!""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
        
        



async def fullweek_inline(call: types.CallbackQuery):
    
    
    if call.data == 'Monday':
        list = await give_week(user_id=call.from_user.id, week='monday')
        await bot.edit_message_text(text=f"""📔 <b>План на Понедельник</b>

{list}
""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoFullWeak_frame)
        
        
    elif call.data == 'Tuesday':
        list = await give_week(user_id=call.from_user.id, week='tuesday')
        await bot.edit_message_text(text=f"""📔 <b>План на Вторник</b>
 
{list}
""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoFullWeak_frame)
    
    
    elif call.data == 'Wednesday':
        list = await give_week(user_id=call.from_user.id, week='wednesday')
        await bot.edit_message_text(text=f"""📔 <b>План на Среду</b>

{list}
""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoFullWeak_frame)
    
    
    elif call.data == 'Thursday':
        list = await give_week(user_id=call.from_user.id, week='thursday')
        await bot.edit_message_text(text=f"""📔 <b>План на Четверг</b>

{list}
""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoFullWeak_frame) 
    
    
    elif call.data == 'Friday':
        list = await give_week(user_id=call.from_user.id, week='friday')
        await bot.edit_message_text(text=f"""📔 <b>План на Пятницу</b>

{list}
""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoFullWeak_frame)
    
    
    elif call.data == 'Saturday':
        list = await give_week(user_id=call.from_user.id, week='saturday')
        await bot.edit_message_text(text=f"""📔 <b>План на Субботу</b>

{list}
""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoFullWeak_frame)
    
    
    elif call.data == 'Sunday':
        list = await give_week(user_id=call.from_user.id, week='sunday')
        await bot.edit_message_text(text=f"""📔 <b>План на Воскресенье</b>

{list}
""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=GoFullWeak_frame)
    
    
    elif call.data == 'GoFullWeak__menu':
        await bot.edit_message_text(text='📔 <b>План на неделю</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=FullWeek)





async def editfullweek_inline(call: types.CallbackQuery):
    
    
    if call.data == 'EditMonday':
        await bot.edit_message_text(text='📔 <b>Изменить Понедельник</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditMonday_frame)
        
        
    elif call.data == 'EditTuesday':
        await bot.edit_message_text(text='📔 <b>Изменить Вторник</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditTuesday_frame)
    
    
    elif call.data == 'EditWednesday':
        await bot.edit_message_text(text='📔 <b>Изменить Среду</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditWednesday_frame)
    
    
    elif call.data == 'EditThursday':
        await bot.edit_message_text(text='📔 <b>Изменить Четверг</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditThursday_frame) 
    
    
    elif call.data == 'EditFriday':
        await bot.edit_message_text(text='📔 <b>Изменить Пятницу</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditFriday_frame)
    
    
    elif call.data == 'EditSaturday':
        await bot.edit_message_text(text='📔 <b>Изменить Субботу</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditSaturday_frame)
    
    
    elif call.data == 'EditSunday':
        await bot.edit_message_text(text='📔 <b>Изменить Воскресенье</b>', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditSunday_frame)
    
    
    elif call.data == 'GoEditFullWeak__menu':
        await bot.edit_message_text(text="""📔 <b>Изменить неделю</b>""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditFullWeek)





async def AddEditfullweek(call: types.CallbackQuery, state: FSMContext):
    
    
    if call.data == 'Add_monday':
        list = await give_week(user_id=call.from_user.id, week='monday')
        await bot.edit_message_text(text=f"""✏️ <b>Добавить планы на понедельник</b>   
                                                                   
Напишите <b>текст и время</b> для добавления, таким образом: 
Репетитор по математике 20:00

Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='monday')
        await Addweek.text.set()
    
    
    elif call.data == 'Change_monday':
        list = await give_week(user_id=call.from_user.id, week='monday')
        await state.update_data(week='monday')
        await bot.edit_message_text(text=f"""🔄 <b>Изменить планы на понедельник</b> 
                                                                     
Напишите <b>текст и время</b> для изменения таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Editweek.text.set()
    
    
    elif call.data == 'Delete_monday':
        list = await give_week(user_id=call.from_user.id, week='monday')
        await state.update_data(week='monday')
        await bot.edit_message_text(text=f"""✂️ <b>Удалить планы на понедельник</b>
                                    
Напишите <b>текст и время</b> для удаления таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Deleteweek.text.set()
        
    
    elif call.data == 'Add_tuesday':
        list = await give_week(user_id=call.from_user.id, week='tuesday')
        await bot.edit_message_text(text=f"""✏️ <b>Добавить планы на вторник</b>                             
                                                                   
Напишите <b>текст и время</b> для добавления, таким образом: 
Репетитор по математике 20:00

Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='tuesday')
        await Addweek.text.set()
    
    
    elif call.data == 'Change_tuesday':
        list = await give_week(user_id=call.from_user.id, week='tuesday')
        await state.update_data(week='tuesday')
        await bot.edit_message_text(text=f"""🔄 <b>Изменить планы на вторник</b>                                  
                                                                     
Напишите <b>текст и время</b> для изменения таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Editweek.text.set()
    
    
    elif call.data == 'Delete_tuesday':
        list = await give_week(user_id=call.from_user.id, week='tuesday')
        await state.update_data(week='tuesday')
        await bot.edit_message_text(text=f"""✂️ <b>Удалить планы на вторник</b>
                                    
Напишите <b>текст и время</b> для удаления таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Deleteweek.text.set()
    
    
    elif call.data == 'Add_wednesday':
        list = await give_week(user_id=call.from_user.id, week='wednesday')
        await bot.edit_message_text(text=f"""✏️ <b>Добавить планы на среду</b>                                    
                                                                   
Напишите <b>текст и время</b> для добавления, таким образом: 
Репетитор по математике 20:00

Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='wednesday')
        await Addweek.text.set()
    
    
    elif call.data == 'Change_wednesday':
        list = await give_week(user_id=call.from_user.id, week='wednesday')
        await state.update_data(week='wednesday')
        await bot.edit_message_text(text=f"""🔄 <b>Изменить планы на среду</b>
                                                                     
Напишите <b>текст и время</b> для изменения таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Editweek.text.set()
    
    
    elif call.data == 'Delete_wednesday':
        list = await give_week(user_id=call.from_user.id, week='wednesday')
        await state.update_data(week='wednesday')
        await bot.edit_message_text(text=f"""✂️ <b>Удалить планы на среду</b>
                                    
Напишите <b>текст и время</b> для удаления таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Deleteweek.text.set()

    
    elif call.data == 'Add_thursday':
        list = await give_week(user_id=call.from_user.id, week='thursday')
        await bot.edit_message_text(text=f"""✏️ <b>Добавить планы на четверг</b>                                    
                                                                   
Напишите <b>текст и время</b> для добавления, таким образом: 
Репетитор по математике 20:00

Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='thursday')
        await Addweek.text.set()
    
    
    elif call.data == 'Change_thursday':
        list = await give_week(user_id=call.from_user.id, week='thursday')
        await state.update_data(week='thursday')
        await bot.edit_message_text(text=f"""🔄 <b>Изменить планы на четверг</b>
                                                                     
Напишите <b>текст и время</b> для изменения таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Editweek.text.set()
    
    
    elif call.data == 'Delete_thursday':
        list = await give_week(user_id=call.from_user.id, week='thursday')
        await state.update_data(week='thursday')
        await bot.edit_message_text(text=f"""✂️ <b>Удалить планы на четверг</b>
                                    
Напишите <b>текст и время</b> для удаления таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Deleteweek.text.set()
    

    elif call.data == 'Add_friday':
        list = await give_week(user_id=call.from_user.id, week='friday')
        await bot.edit_message_text(text=f"""✏️ <b>Добавить планы на пятницу</b>                                    
                                                                   
Напишите <b>текст и время</b> для добавления, таким образом: 
Репетитор по математике 20:00

Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='friday')
        await Addweek.text.set()
    
    
    elif call.data == 'Change_friday':
        list = await give_week(user_id=call.from_user.id, week='friday')
        await state.update_data(week='friday')
        await bot.edit_message_text(text=f"""🔄 <b>Изменить планы на пятницу</b>
                                                                     
Напишите <b>текст и время</b> для изменения таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Editweek.text.set()

    
    elif call.data == 'Delete_friday':
        list = await give_week(user_id=call.from_user.id, week='friday')
        await state.update_data(week='friday')
        await bot.edit_message_text(text=f"""✂️ <b>Удалить планы на пятницу</b>
                                    
Напишите <b>текст и время</b> для удаления таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Deleteweek.text.set()

    
    elif call.data == 'Add_saturday':
        list = await give_week(user_id=call.from_user.id, week='saturday')
        await bot.edit_message_text(text=f"""✏️ <b>Добавить планы на субботу</b>        
                                                                   
Напишите <b>текст и время</b> для добавления, таким образом: 
Репетитор по математике 20:00

Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='saturday')
        await Addweek.text.set()

    
    elif call.data == 'Change_saturday':
        list = await give_week(user_id=call.from_user.id, week='saturday')
        await bot.edit_message_text(text=f"""🔄 <b>Изменить планы на субботу</b>
                                                                     
Напишите <b>текст и время</b> для изменения таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='saturday')
        await Editweek.text.set()
    
    
    elif call.data == 'Delete_saturday':
        list = await give_week(user_id=call.from_user.id, week='saturday')
        await state.update_data(week='saturday')
        await bot.edit_message_text(text=f"""✂️ <b>Удалить планы на субботу</b>
                                    
Напишите <b>текст и время</b> для удаления таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Deleteweek.text.set()


    elif call.data == 'Add_sunday':
        list = await give_week(user_id=call.from_user.id, week='sunday')
        await bot.edit_message_text(text=f"""✏️ <b>Добавить планы на воскресенье</b>                           
                                                                   
Напишите <b>текст и время</b> для добавления, таким образом: 
Репетитор по математике 20:00

Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='sunday')
        await Addweek.text.set()
    
    
    elif call.data == 'Change_sunday':
        list = await give_week(user_id=call.from_user.id, week='sunday')
        await state.update_data(week='sunday')
        await bot.edit_message_text(text=f"""🔄 <b>Изменить планы на воскресенье</b>
                                                                     
Напишите <b>текст и время</b> для изменения таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await state.update_data(week='sunday')
        await Editweek.text.set()
    
    
    elif call.data == 'Delete_sunday':
        list = await give_week(user_id=call.from_user.id, week='sunday')
        await state.update_data(week='sunday')
        await bot.edit_message_text(text=f"""✂️ <b>Удалить планы на воскресенье</b>
                                    
Напишите <b>текст и время</b> для удаления таким образом: 
Репетитор по математике 20:00
                                    
Ваши планы:
{list}""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=BackEditFullWeak_frame)
        await Deleteweek.text.set()



        

def register_call_handlers(dp: Dispatcher):
    
    dp.register_callback_query_handler(main_inline, Text(['Timetable', 'Event', 'Timetable_change', 'Event_del', 'Help', 'GoMain_menu', 'Today_timetable', 'Alert_change']))
    
    dp.register_callback_query_handler(fullweek_inline, Text(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'GoFullWeak__menu']))
    
    dp.register_callback_query_handler(editfullweek_inline, Text(['EditMonday', 'EditTuesday', 'EditWednesday', 'EditThursday', 'EditFriday', 'EditSaturday', 'EditSunday', 'GoEditFullWeak__menu']))
    
    dp.register_callback_query_handler(AddEditfullweek, Text(['Add_monday', 'Change_monday', 'Delete_monday', 'Add_tuesday', 'Change_tuesday', 'Delete_tuesday', 'Add_wednesday', 'Change_wednesday',\
                                                              'Delete_wednesday', 'Add_thursday', 'Change_thursday', 'Delete_thursday', 'Add_friday', \
                                                              'Change_friday', 'Delete_friday', 'Add_saturday', 'Change_saturday', 'Delete_saturday', 'Add_sunday', 'Change_sunday', 'Delete_sunday']), state=None)
    
    dp.register_callback_query_handler(alert_change, Text(['Alert_yes', 'Alert_no']))