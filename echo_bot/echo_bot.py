import os
import asyncio

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('MY_CHAT_ID')

dp = Dispatcher()
bot = Bot(token=TOKEN)


async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=CHAT_ID, text="Bot ishga tushti!")


async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=CHAT_ID, text="Bot tohtadi!!!")


async def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)

    
async def main():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(echo)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())