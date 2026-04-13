import aiogram
from dotenv import load_dotenv
from routers import root_router
import os

load_dotenv()

token = os.getenv("API_TOKEN")

bot = aiogram.Bot(token='8706204215:AAGjfPt1fzi5khao_dufcXfdlo4-Mc9Io0E')
dp = aiogram.Dispatcher()

dp.include_router(root_router)