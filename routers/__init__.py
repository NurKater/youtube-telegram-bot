from aiogram import Router
from routers.commands import commands_router

root_router = Router()
root_router.include_routers(
    commands_router,
)