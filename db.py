import asyncio
import sqlite3 as sq
import datetime





async def db_start():
    global db, cur
    
    db = sq.connect('database.db') #подключение к баззе данных
    cur = db.cursor() #для выполнений действий с баззой данных
    
    cur.execute("CREATE TABLE IF NOT EXISTS user(user_id TEXT PRIMARY KEY, monday TEXT, tuesday TEXT, wednesday TEXT, thursday TEXT, friday TEXT, saturday TEXT, sunday TEXT, alert TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS event(user_id TEXT, text TEXT, time TEXT)")
    db.commit()






async def create_profile(user_id):
    user = cur.execute("SELECT 1 FROM user WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, '', '', '', '', '', '', '', 1))
        db.commit()
        

async def check_user(user_id):
    user = cur.execute("SELECT * FROM user WHERE user_id == '{}' ".format(user_id)).fetchone()
    if user:
        return 1
    else:
        return 0


async def create_event(user_id, text, time):
    cur.execute("INSERT INTO event VALUES(?, ?, ?)", (user_id, text, time))
    db.commit()





async def delete_event(user_id, text, time):
    cur.execute("DELETE FROM event WHERE user_id == '{}' AND text == '{}' AND time == '{}' ".format(user_id, text, time)).fetchone()
    db.commit()





async def check_event(user_id, text, time):
    event = cur.execute("SELECT * FROM event WHERE user_id == '{}' AND text == '{}' AND time == '{}' ".format(user_id, text, time)).fetchone()
    if event:
        return 1
    else:
        return 0





async def lists_event(user_id):
    events = cur.execute("SELECT * FROM event WHERE user_id == '{}' ".format(user_id)).fetchall()
    l = []
    for i in events:
        event = i[1] + ' ' + i[2]
        l.append(event)
    event = '\n'.join(l)
    if event == '':
        event = 'У вас нет напоминаний'
    return event





async def add_week(user_id, week, text):
    
    week_db = cur.execute("SELECT {} FROM user WHERE user_id == '{}' ".format(week, user_id)).fetchone()
    if week_db == ('',):
        cur.execute("UPDATE user SET {} == '{}' WHERE user_id == '{}'".format(week, text, user_id))
    else:
        list_weeks = ' '.join(map(str, week_db)) + ';' + text
        cur.execute("UPDATE user SET {} == '{}' WHERE user_id == '{}'".format(week, list_weeks, user_id))
    db.commit()





async def delete_week(user_id, week, text):
    week_db = cur.execute("SELECT {} FROM user WHERE user_id == '{}' ".format(week, user_id)).fetchone()
    for i in week_db:
        week_list = i.split(';')
    for i in week_list:
        if i == text:
            week_list.remove(text)
            week_list = ';'.join(map(str, week_list))
            cur.execute("UPDATE user SET {} == '{}' WHERE user_id == '{}'".format(week, week_list, user_id))
            db.commit()
            return '✅ План был удален'
    return '❌ <b>Мы не смогли удалить план</b>'





async def check_week(user_id, week, text):
    week_db = cur.execute("SELECT {} FROM user WHERE user_id == '{}'".format(week, user_id)).fetchone()
    for i in week_db:
        week_list = i.split(';')
    for i in week_list:
        if i == text:
            return 1
    return 0



  
    
async def change_week(user_id, plan, week, text):
    week_db = cur.execute("SELECT {} FROM user WHERE user_id == '{}'".format(week, user_id)).fetchone()
    for i in week_db:
        week_list = i.split(';')
    for i in range(len(week_list)):
        if week_list[i] == plan:
            week_list[i] = text
            week_list = ';'.join(map(str, week_list))
            cur.execute("UPDATE user SET {} == '{}' WHERE user_id == '{}'".format(week, week_list, user_id))
            db.commit()
            return 1
    return 0





async def give_week(user_id, week):
    
    week_list = cur.execute("SELECT {} FROM user WHERE user_id == '{}' ".format(week, user_id)).fetchone()
    l = []
    for i in week_list:
        l.append(i)
    list = '\n'.join(l).split(';')
    list = '\n\n'.join(list)
    if list == '':
        list = 'У вас нет напоминаний на этот день'
        
    return list
    




async def give_week_today(user_id, week):
    if week == '0':
        week = 'monday'
    elif week == '1':
        week = 'tuesday'
    elif week == '2':
        week = 'wednesday'
    elif week == '3':
        week = 'thursday'
    elif week == '4':
        week = 'friday'
    elif week == '5':
        week = 'saturday'
    elif week == '6':
        week = 'sunday'   
    week_list = cur.execute("SELECT {} FROM user WHERE user_id == '{}'".format(week, user_id)).fetchone()
    l = []
    for i in week_list:
        l.append(i)
    list = '\n'.join(l).split(';')
    list = '\n\n'.join(list)
    if list == '':
        list = 'У вас нет планов на сегодня'
        
    return list





from handlers.client import send_message, answer_mesage

async def check_time_function(): #фукнция просмотра времени в напоминаниях
    while True:
        time_now = str(datetime.datetime.now().time())[:5]
        check_time = cur.execute("SELECT * FROM event WHERE time == '{}'".format(time_now)).fetchall()
        if check_time:
            for i in range(len(check_time)):
                await send_message(user_id=check_time[i][0], text_message=check_time[i][1], time=check_time[i][2])
                cur.execute("DELETE FROM event WHERE time == '{}' and text == '{}'".format(time_now, check_time[i][1])).fetchone()
                db.commit()
        await asyncio.sleep(50)





async def all_users():
    users = cur.execute("SELECT user_id FROM user WHERE alert == 1").fetchall()
    if users:
        for i in range(len(users)):
            await answer_mesage(user_id=users[i][0])





async def every_day_week():
    while True: 
        time_now = str(datetime.datetime.now().time())[:5]
        if time_now == "07:00":
            await all_users()
        await asyncio.sleep(3600)
        


async def alert_change_db_yes(user_id):
    user = cur.execute("SELECT * FROM user WHERE user_id == '{}' ".format(user_id)).fetchone()
    if user[-1] == '0':
        cur.execute("UPDATE user SET alert == 1 WHERE user_id == '{}'".format(user_id))
        db.commit()
        return 1
    else:
        return 0



async def alert_change_db_no(user_id):
    user = cur.execute("SELECT * FROM user WHERE user_id == '{}' ".format(user_id)).fetchone()
    if user[-1] == '1':
        cur.execute("UPDATE user SET alert == 0 WHERE user_id == '{}'".format(user_id))
        db.commit()
        return 1
    else:
        return 0
        