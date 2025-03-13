import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from functions import get_user_info

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("MY_CHAT_ID")

dp = Dispatcher()
bot = Bot(token=TOKEN)


async def startup_await(event):
    await bot.send_message(chat_id=CHAT_ID, text="Bot ishga tushdi!")


async def shutdown_await(event):
    await bot.send_message(chat_id=CHAT_ID, text="Bot ishdan toxtadi!")


async def main() -> None:
    dp.startup.register(startup_await)
    dp.shutdown.register(shutdown_await)

    dp.message.register(get_user_info)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
