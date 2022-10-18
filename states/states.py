from aiogram import types, Dispatcher
from keyboard.client_inline_buttons import GoMain_frame
from states.create_states import *
from aiogram.dispatcher import FSMContext
from create_bot import bot
from aiogram.dispatcher.filters import Text
from keyboard.client_inline_buttons import main_frame, EditFullWeek, BackEditFullWeak_frame
from db import add_week, change_week, check_week, create_event, delete_event, check_event, delete_week





async def set_addevent_textinline(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'GoMain_menu':
        await bot.edit_message_text(text='✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b> ', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
        await state.finish()



async def set_addevent_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("""🕖 <b>Напишите время напоминания</b>  
                                                                     
Пример: 18:20""", parse_mode='HTML', reply_markup=GoMain_frame)
    await AddEvent.next()
    
    
    
    
    
async def set_addevent_timeinline(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'GoMain_menu':
        await bot.edit_message_text(text='✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b> ', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
        await state.finish()
        
    
        
async def set_addevent_time(message: types.Message, state: FSMContext):
    while not ((':' in message.text) and (len(message.text) == 5 or len(message.text) == 4) and (len(message.text.split(':')[0]) == 2 or len(message.text.split(':')[0]) == 1)):
        await message.answer("""❌ <b>Не правильный формат!</b>""",  parse_mode='HTML', reply_markup=GoMain_frame)
        break
    else:
        if len(message.text) == 4:
            message.text = '0' + message.text
        await state.update_data(time=message.text)
        await message.answer("""✅ <b>Напоминание добавлено!</b>""",  parse_mode='HTML', reply_markup=main_frame)
        data = await state.get_data()
        await create_event(user_id=message.from_user.id, text=data['text'], time=data['time'])
        await state.finish()
        
        
        
        
        
async def set_deleteevent_timeinline(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'GoMain_menu':
        await bot.edit_message_text(text='✍️ <b>𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧𝐬</b> ', chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode='HTML', reply_markup=main_frame)
        await state.finish()
        
  
             
async def set_deleteevent_time(message: types.Message, state: FSMContext):
    if len(message.text.rsplit(' ', 1)) > 1:
        text = message.text.rsplit(' ', 1)[0]
        time = message.text.rsplit(' ', 1)[1]
        event = await check_event(user_id=message.from_user.id, text=text, time=time)
        while not event:
            await message.answer("""❌ <b>Напоминание не найдено!</b>""",  parse_mode='HTML', reply_markup=GoMain_frame)
            break
        else:
            await message.answer("""✅ <b>Напоминание удалено!</b>""",  parse_mode='HTML', reply_markup=main_frame)
            await delete_event(user_id=message.from_user.id, text=text, time=time)
            await state.finish()
    else:
        await message.answer("""❌ <b>Напоминание не найдено!</b>""",  parse_mode='HTML', reply_markup=GoMain_frame)
        
        
        
        
               
async def set_addweekinline(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'BackEditFullWeak_menu':
        await bot.edit_message_text(text="""📔 <b>Изменить неделю</b>""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditFullWeek)
        await state.finish()
        
  
           
async def set_addweek(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await add_week(user_id=message.from_user.id, week=data['week'], text=message.text)
    await message.answer("""✅ <b>План добавлен!</b> 
                         
Пишите дальше или нажмите на кнопку закончить""", parse_mode='HTML', reply_markup=BackEditFullWeak_frame)





async def set_editweekinline_change(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'BackEditFullWeak_menu':
        await bot.edit_message_text(text="""📔 <b>Изменить неделю</b>""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditFullWeek)
        await state.finish()



async def set_editweek_change(message: types.Message, state: FSMContext):
    data = await state.get_data()
    res = await change_week(user_id=message.from_user.id, week=data['week'], plan=data['plan'], text=message.text)
    while not res == 1:
        await message.answer(text=res,  parse_mode='HTML', reply_markup=BackEditFullWeak_frame)
        break
    else:
        await message.answer("""📔 <b>Изменить неделю</b>
                                    
✅ Вы успешно изменили планы!""", parse_mode='HTML', reply_markup=EditFullWeek)
        await state.finish()





async def set_editweekinline(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'BackEditFullWeak_menu':
        await bot.edit_message_text(text="""📔 <b>Изменить неделю</b>""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditFullWeek)
        await state.finish()
        
        
        
async def set_editweek(message: types.Message, state: FSMContext):
    data = await state.get_data()
    proverka = await check_week(user_id=message.from_user.id, week=data['week'], text=message.text)
    if proverka:
        await state.update_data(plan=message.text)
        await message.answer(f"""Вы выбрали для измения: <b>{message.text}</b>
                             
Напишите, как он теперь должен выглядеть!""", parse_mode='HTML', reply_markup=BackEditFullWeak_frame)
        await Editweek.next()
    else:
        await message.answer("""❌ <b>План не найден!</b>""",  parse_mode='HTML', reply_markup=BackEditFullWeak_frame)
       




async def set_deleteweekinline(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'BackEditFullWeak_menu':
        await bot.edit_message_text(text="""📔 <b>Изменить неделю</b>""", chat_id=call.from_user.id, message_id=call.message.message_id, parse_mode="HTML", reply_markup=EditFullWeek)
        await state.finish()



async def set_deleteweek(message: types.Message, state: FSMContext):
    data = await state.get_data()
    res = await delete_week(user_id=message.from_user.id, week=data['week'], text=message.text)
    while not res == '✅ План был удален':
        await message.answer("""❌ <b>План не найден!</b>""",  parse_mode='HTML', reply_markup=BackEditFullWeak_frame)
        break
    else:
        await message.answer("""✅ <b>План был удален!</b> 
                             
Пишите дальше или нажмите на кнопку закончить""", parse_mode='HTML', reply_markup=BackEditFullWeak_frame)










def register_states_client(dp: Dispatcher):
    
    
    dp.register_callback_query_handler(set_addevent_textinline, Text('GoMain_menu'), state=AddEvent.text)
    dp.register_message_handler(set_addevent_text, state=AddEvent.text)
    
    
    dp.register_callback_query_handler(set_addevent_timeinline, Text('GoMain_menu'), state=AddEvent.time)
    dp.register_message_handler(set_addevent_time, state=AddEvent.time)
    
    
    dp.register_callback_query_handler(set_deleteevent_timeinline, Text('GoMain_menu'), state=DeleteEvent.time)
    dp.register_message_handler(set_deleteevent_time, state=DeleteEvent.time)
    
    
    dp.register_callback_query_handler(set_addweekinline, Text('BackEditFullWeak_menu'), state=Addweek.text)
    dp.register_message_handler(set_addweek, state=Addweek.text)
    
    
    dp.register_callback_query_handler(set_editweekinline, Text('BackEditFullWeak_menu'), state=Editweek.text)
    dp.register_message_handler(set_editweek, state=Editweek.text)
    
    
    dp.register_callback_query_handler(set_editweekinline_change, Text('BackEditFullWeak_menu'), state=Editweek.change)
    dp.register_message_handler(set_editweek_change, state=Editweek.change)
    
    
    dp.register_callback_query_handler(set_deleteweekinline, Text('BackEditFullWeak_menu'), state=Deleteweek.text)
    dp.register_message_handler(set_deleteweek, state=Deleteweek.text)
    
    