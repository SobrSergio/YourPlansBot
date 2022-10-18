from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup





Help = InlineKeyboardButton(text='🆘 Связь с создателем', callback_data='Help')
GoMain_menu = InlineKeyboardButton(text="🏠 Главное меню", callback_data= "GoMain_menu")
Alert_change = InlineKeyboardButton(text="🔔 Изменить уведомления", callback_data="Alert_change")
GoFullWeak__menu = InlineKeyboardButton(text="🔙 Назад", callback_data= "GoFullWeak__menu")
GoEditFullWeak__menu = InlineKeyboardButton(text="🔙 Назад", callback_data= "GoEditFullWeak__menu")
BackEditFullWeak_menu = InlineKeyboardButton(text="🔙 Закончить", callback_data= "BackEditFullWeak_menu")





Timetable = InlineKeyboardButton(text= "📔 План на неделю", callback_data= "Timetable")
Timetable_change = InlineKeyboardButton(text= "📔 Изменить неделю", callback_data= "Timetable_change")
Event = InlineKeyboardButton(text= "📝 Добав. напомин.", callback_data= "Event")
Event_del = InlineKeyboardButton(text= "📝 Удал. напомин.", callback_data= "Event_del")
Today_timetable = InlineKeyboardButton(text='🗓️ План на сегодня', callback_data= "Today_timetable")



Alert_yes = InlineKeyboardButton(text="✅ Включить", callback_data="Alert_yes")
Alert_no = InlineKeyboardButton(text="❌ Отключить", callback_data="Alert_no")


Alert_yes_no = InlineKeyboardMarkup(row_width=2).add(Alert_yes, Alert_no).add(GoMain_menu)



Monday = InlineKeyboardButton(text="Понедельник", callback_data="Monday")
Tuesday = InlineKeyboardButton(text="Вторник", callback_data="Tuesday")
Wednesday = InlineKeyboardButton(text="Среда", callback_data="Wednesday")
Thursday = InlineKeyboardButton(text="Четверг", callback_data="Thursday")
Friday = InlineKeyboardButton(text="Пятница", callback_data="Friday")
Saturday = InlineKeyboardButton(text="Суббота", callback_data="Saturday")
Sunday = InlineKeyboardButton(text="Воскресенье", callback_data="Sunday")





EditMonday = InlineKeyboardButton(text="Понедельник", callback_data="EditMonday")
EditTuesday = InlineKeyboardButton(text="Вторник", callback_data="EditTuesday")
EditWednesday = InlineKeyboardButton(text="Среда", callback_data="EditWednesday")
EditThursday = InlineKeyboardButton(text="Четверг", callback_data="EditThursday")
EditFriday = InlineKeyboardButton(text="Пятница", callback_data="EditFriday")
EditSaturday = InlineKeyboardButton(text="Суббота", callback_data="EditSaturday")
EditSunday = InlineKeyboardButton(text="Воскресенье", callback_data="EditSunday")





FullWeek = InlineKeyboardMarkup(row_width=3).add(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).add(GoMain_menu)

EditFullWeek = InlineKeyboardMarkup(row_width=3).add(EditMonday, EditTuesday, EditWednesday, EditThursday, EditFriday, EditSaturday, EditSunday).add(GoMain_menu)

main_frame = InlineKeyboardMarkup(row_width=1).add(Today_timetable).row(Timetable, Timetable_change).row(Event, Event_del).add(Alert_change).add(Help)

GoMain_frame = InlineKeyboardMarkup(row_width=1).add(GoMain_menu)

GoFullWeak_frame = InlineKeyboardMarkup(row_width=1).add(GoFullWeak__menu)

BackEditFullWeak_frame = InlineKeyboardMarkup(row_width=1).add(BackEditFullWeak_menu)





Add_monday = InlineKeyboardButton(text="✏️ Добав. планы", callback_data="Add_monday")
Change_monday = InlineKeyboardButton(text="🔄 Измен. планы", callback_data="Change_monday")
Delete_monday = InlineKeyboardButton(text="✂️ Удалить планы", callback_data="Delete_monday")

EditMonday_frame = InlineKeyboardMarkup(row_width=1).add(Add_monday).row(Change_monday, Delete_monday).add(GoEditFullWeak__menu)



Add_tuesday = InlineKeyboardButton(text="✏️ Добав. планы", callback_data="Add_tuesday")
Change_tuesday = InlineKeyboardButton(text="🔄 Измен. планы", callback_data="Change_tuesday")
Delete_tuesday = InlineKeyboardButton(text="✂️ Удалить планы", callback_data="Delete_tuesday")

EditTuesday_frame = InlineKeyboardMarkup(row_width=1).add(Add_tuesday).row(Change_tuesday, Delete_tuesday).add(GoEditFullWeak__menu)



Add_wednesday = InlineKeyboardButton(text="✏️ Добав. планы", callback_data="Add_wednesday")
Change_wednesday = InlineKeyboardButton(text="🔄 Измен. планы", callback_data="Change_wednesday")
Delete_wednesday = InlineKeyboardButton(text="✂️ Удалить планы", callback_data="Delete_wednesday")

EditWednesday_frame = InlineKeyboardMarkup(row_width=1).add(Add_wednesday).row(Change_wednesday, Delete_wednesday).add(GoEditFullWeak__menu)



Add_thursday = InlineKeyboardButton(text="✏️ Добав. планы", callback_data="Add_thursday")
Change_thursday = InlineKeyboardButton(text="🔄 Измен. планы", callback_data="Change_thursday")
Delete_thursday = InlineKeyboardButton(text="✂️ Удалить планы", callback_data="Delete_thursday")

EditThursday_frame = InlineKeyboardMarkup(row_width=1).add(Add_thursday).row(Change_thursday, Delete_thursday).add(GoEditFullWeak__menu)


Add_friday = InlineKeyboardButton(text="✏️ Добав. планы", callback_data="Add_friday")
Change_friday = InlineKeyboardButton(text="🔄 Измен. планы", callback_data="Change_friday")
Delete_friday = InlineKeyboardButton(text="✂️ Удалить планы", callback_data="Delete_friday")

EditFriday_frame = InlineKeyboardMarkup(row_width=1).add(Add_friday).row(Change_friday, Delete_friday).add(GoEditFullWeak__menu)



Add_saturday = InlineKeyboardButton(text="✏️ Добав. планы", callback_data="Add_saturday")
Change_saturday = InlineKeyboardButton(text="🔄 Измен. планы", callback_data="Change_saturday")
Delete_saturday = InlineKeyboardButton(text="✂️ Удалить планы", callback_data="Delete_saturday")

EditSaturday_frame = InlineKeyboardMarkup(row_width=1).add(Add_saturday).row(Change_saturday, Delete_saturday).add(GoEditFullWeak__menu)



Add_sunday = InlineKeyboardButton(text="✏️ Добав. планы", callback_data="Add_sunday")
Change_sunday = InlineKeyboardButton(text="🔄 Измен. планы", callback_data="Change_sunday")
Delete_sunday = InlineKeyboardButton(text="✂️ Удалить планы", callback_data="Delete_sunday")

EditSunday_frame = InlineKeyboardMarkup(row_width=1).add(Add_sunday).row(Change_sunday, Delete_sunday).add(GoEditFullWeak__menu)
