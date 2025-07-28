from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
import asyncio

API_TOKEN = '7792258020:AAG3Sy9ht5_4Tgdz3pSXBE-dYjjrIJqf2xk'
WEBAPP_URL = 'https://rpglive.xyz/'

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = [
        [InlineKeyboardButton(text="Play", web_app=WebAppInfo(url=WEBAPP_URL))],
    ]

    await message.answer(
        "Press the button to start Play:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())