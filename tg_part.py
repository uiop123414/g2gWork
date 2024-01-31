import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import json


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6232994935:AAFYYNvIhwy8WTtJ26XyQWzgUkiQIy6JLZY")
# Диспетчер
dp = Dispatcher()
users = []
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        with open("data.json", "r") as f:
            users = set(json.loads(f.read()))
    except json.decoder.JSONDecodeError:
        print('No Users')
        users = {}
    await message.answer("Hello!")
    
    users.append(message.from_user.id)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(list(users), f, ensure_ascii=False, indent=4)

async def echo_message(bot,text):
    with open("data.json", "r") as f:
        users = json.loads(f.read())
    for user in users:
        await bot.send_message(user, text)

# Запуск процесса поллинга новых апдейтов
async def start_bot():
    await dp.start_polling(bot)
    return dp,bot

if __name__ == "__main__":
    asyncio.run(start_bot())