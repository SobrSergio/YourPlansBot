from aiogram.dispatcher.filters.state import StatesGroup, State





class AddEvent(StatesGroup):
    text = State()
    time = State()





class DeleteEvent(StatesGroup):
    time = State()





class Addweek(StatesGroup):
    text = State()





class Editweek(StatesGroup):
    text = State()
    change = State()
    




class Deleteweek(StatesGroup):
    text = State()