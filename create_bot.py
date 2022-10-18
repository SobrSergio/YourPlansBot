from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config_reader import config





bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot, storage=MemoryStorage())