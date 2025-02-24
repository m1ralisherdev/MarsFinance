import logging
from aiogram import Bot, Dispatcher, types, executor
import os
import django
import openpyxl



# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')

# Configure Django
django.setup()

# Now you can import your models
from MarsUsers.service import finance_service



logging.basicConfig(level=logging.INFO)
TOKEN = "5381016013:AAFrNaST9imOePGq9EotMhx4kghx1XgKHck"
bot = Bot(token=TOKEN,parse_mode="HTML")
dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Assalomu Aleykom Mars Finance botiga xush kelibsiz")

@dp.message_handler(commands=["finance"])
async def help_command(message: types.Message):
    data = await finance_service(message.from_user.id)
    await message.answer(data)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)