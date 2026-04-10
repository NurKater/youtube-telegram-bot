import aiogram
from aiogram import Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("API_TOKEN")

bot = aiogram.Bot(token=token)
dp = Dispatcher(bot)

