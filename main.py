from aiogram import Bot, Dispatcher,types
from aiogram import F
import keyboards
from states import  User_states
import aiogram.filters as fils
import asyncio
from aiogram.fsm import storage

from aiogram.fsm.context import FSMContext
import config
from aiogram.fsm import  state
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=config.TOKEN)
memory = MemoryStorage()
dp = Dispatcher(storage=memory)

@dp.message(fils.CommandStart())
async def start_cmd(message: types.Message, state: FSMContext):
    await message.answer("hello", reply_markup=keyboards.create_keyboard("Добавить пари", "Мои пари"))
    await state.set_state(User_states.BASE)


@dp.message(F.text == "Мои пари", fils.StateFilter(User_states.BASE))
async def create_pari(message: types.Message, state: FSMContext):
     pass

async def run_bot(bot):
    await dp.start_polling(bot)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run_bot(bot))