from bot import bot, dp
import asyncio

async def main():
    await dp.start_polling(bot)

asyncio.run(main())