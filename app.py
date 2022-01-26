from aiogram import executor

from data.db import create_tables, create_db
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Создаем базу данных
    try:
        create_db()
    except:
        print("БД уже создана")

    # Создаем таблицы в базе данных
    try:
        create_tables()
    except:
        print("Таблица уже создана")

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
