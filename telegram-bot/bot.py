import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

# --- НАСТРОЙКИ ---
BOT_TOKEN = "8947311324:AAFMDStT8MrWktrWQENTKl5Lb-yh1CLbGLM"  # Замени на свой токен!
ADMIN_ID = 8733257796  # Твой Telegram ID (узнай через @userinfobot)
# -----------------

# Список рабочих ключей (можешь добавлять свои)
VALID_KEYS = [
    "BR-2026-HACK-001",
    "FREE-KEY-2026",
    "MY-SUPER-KEY-12"
]

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("👋 Привет! Отправь мне свой ключ для активации лаунчера.\n\nИспользуй команду /check KEY")

# Команда проверки ключа (через бота)
@dp.message(Command("check"))
async def check_key(message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("❌ Ошибка: Напиши /check ТВОЙ_КЛЮЧ")
        return
    
    user_key = args[1]
    
    if user_key in VALID_KEYS:
        await message.answer("✅ Ключ активирован! Лаунчер разблокирован.")
        # (Здесь можно отправить запрос лаунчеру, если нужно)
    else:
        await message.answer("❌ Неверный ключ или ключ истек.")

# --- ЕСЛИ ЛАУНЧЕР СТУЧИТСЯ НА БОТА (Webhook или API) ---
# Ниже функция для HTTP-сервера, если лаунчер делает GET/POST запросы на бота, а не просто пишет в чат.
# Если тебе нужно, чтобы лаунчер отправлял HTTP-запрос, раскомментируй импорт FastAPI и этот код.

# from fastapi import FastAPI
# import uvicorn
# app = FastAPI()
#
# @app.post("/api/check")
# async def check_launcher_key(key: str):
#     if key in VALID_KEYS:
#         return {"status": "success", "license": "active"}
#     return {"status": "error", "message": "invalid key"}

# --- Запуск бота (если используешь только чат) ---
async def main():
    print("🚀 Бот запущен и ждет ключи...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
