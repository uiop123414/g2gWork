import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command ,Message, CommandObject
import json
from funpay import get_funpay_pos , funpay_check
from g2g import g2g_create_offer
from db import get_active_offer , save_offer ,set_disactive


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6232994935:AAFYYNvIhwy8WTtJ26XyQWzgUkiQIy6JLZY",parse_mode='HTML')
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


@dp.message(Command("funpay_url"))
async def create_offer(
        message: Message,
        command: CommandObject
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу
    try:
        url,game,tp,*other = command.args.split(" ")

    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n"
            "/settimer <url> "
        )
        return
    
    save_offer(url)


    data = get_funpay_pos(url)

    data['koef']=1.0
    result_dict = {}
    for item in other:
        key, value = item.split('=')
        result_dict[key] = value.rstrip().replace("_"," ")
        data[key] = value.rstrip().replace("_"," ")

    
    
    game = game.replace("_"," ")

    data['price'] *= float(data.get('koef',1.0))# multiply koef price

    await message.answer(
        "Funpay запарсен!\n"
        f"<b>Игра</b>: {game}\n"
        f"<b>Тип</b>: {tp}\n"
        f"<b>Новая цена</b>: {data['price']}\n"
        f"<b>Название</b>: {data['desc']}\n"
        f"<b>Описание</b>: {data['full_desc']}\n"
        f"Другие характеристики: {result_dict}"
    )

    data['game'] = game
    data['type'] = tp

    await g2g_create_offer(data)

async def check(bot):
    #NOT TESTED
    offers = get_active_offer()
    
    if offers != []:
        for offer in offers:
            if(await funpay_check(offer[0])):
                with open("data.json", "r") as f:
                    users = json.loads(f.read())
                for user in users:
                    await bot.send_message(user, "Внимание !!!\n"+offer[0]+"\nБольше не действителен , нужно удалить оффер с G2G!!!")
                set_disactive(offer[0])

if __name__ == "__main__":
    asyncio.run(start_bot())


