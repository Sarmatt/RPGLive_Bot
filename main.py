import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

API_TOKEN = '8087096191:AAGpWlYrE0oXQJhHr4bpjLw9T7mVrSrd9Fo'
WEBAPP_URL = 'https://rpglive.xyz/'

# Нова структура ініціалізації Bot
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text="Грати!", web_app=WebAppInfo(url=WEBAPP_URL))]
        ]
    )
    await message.answer("Привіт! Натисни кнопку нижче, щоб почати гру 🎮", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
