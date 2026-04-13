from bot import bot, dp
from routers import root_router
import asyncio



async def main():
    await dp.start_polling(bot)


asyncio.run(main())