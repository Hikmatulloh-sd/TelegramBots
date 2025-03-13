from aiogram import Bot
from aiogram.types import Message


async def get_user_info(message: Message, bot: Bot) -> None:
    user_photos = await message.from_user.get_profile_photos()

    text = (
        f"{message.from_user.mention_html('USER_INFO')}\n\n"
        f"Ism-Familiya: {message.from_user.full_name}\n"
        f"ID: {message.from_user.id}\n"
    )

    if message.from_user.bio:
        text += f"Tarjimai holi: {message.from_user.bio}\n"
    if message.from_user.username:
        text += f"Username: @{message.from_user.username}"

    if user_photos.photos:
        await message.answer_photo(
            user_photos.photos[0][-1].file_id,
            caption=text,
            parse_mode="HTML",
        )
    else:
        await message.answer(text, parse_mode="HTML")
