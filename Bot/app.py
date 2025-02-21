import logging
from aiogram import Bot, Dispatcher, types, executor


logging.basicConfig(level=logging.INFO)
TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Assalomu Aleykom Mars Finance botiga xush kelibsiz")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)