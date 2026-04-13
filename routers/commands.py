from aiogram import Router, types
from download import download_video
from aiogram.types import FSInputFile

commands_router = Router()


@commands_router.message()
async def track_message(message: types.Message):
    url = message.text
    download_video(url)
    video = FSInputFile("video.mp4")
    await message.reply_video(video=video)