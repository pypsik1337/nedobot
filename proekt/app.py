import asyncio
import os
from aiogram import Bot, Dispatcher





from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.credit import credit_router
from handlers.common import common_router

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
dp.include_router(credit_router)
dp.include_router(common_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
asyncio.run(main())
