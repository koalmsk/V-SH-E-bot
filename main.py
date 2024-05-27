from aiogram import Bot, Dispatcher,types
from aiogram import F
import aiogram.filters as fils
import asyncio
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

@dp.message(fils.CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("hello")


@dp.message()
async def echo(message: types.Message):
    await message.reply(text=f"you said: {message.text}")


async def run_bot(bot):
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot(bot))