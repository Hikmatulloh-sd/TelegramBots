import asyncio
from aiogram import Bot, Dispatcher, types
from .. import config

dp = Dispatcher()
bot = Bot(config.BOT_TOKEN)


async def echo(message: types.Message,bot: Bot):
    await message.copy_to(chat_id=message.chat.id)

    
async def main():
    dp.message.register(echo)

    await dp.start_polling(bot)


asyncio.run(main())