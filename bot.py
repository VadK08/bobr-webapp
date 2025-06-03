import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

API_TOKEN = "7747183387:AAHCTKaj905Q9-Qvygui7h503jzpkbjb7Sg"

# Инициализация бота и диспетчера
bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Обработка команды /start
@router.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🚀 Запустить Bobr.dev",
                web_app=WebAppInfo(url="https://empty-cats-matter.loca.lt")  # твой URL
            )]
        ]
    )
    await message.answer(
        "🦫 Привет! Жми на кнопку, чтобы начать эволюцию бобра!",
        reply_markup=keyboard
    )

# Точка входа
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
