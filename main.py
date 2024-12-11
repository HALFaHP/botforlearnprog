import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from keyboards import enterkb, rowspykb, python_moduls_kb, git_moduls_kb, cplusplus_moduls_kb, javascript_moduls_kb
from callbacks import router
from dotenv import load_dotenv

token = os.getenv('TOKEN')
bot = Bot(token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: Message):
    print(message)
    await message.answer(f'Hello {message.from_user.first_name}', reply_markup=enterkb)


@dp.callback_query(F.data ==  'Python_learning')
async def ptyhon_explanation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Выбирите технологию", reply_markup=python_moduls_kb)


@dp.callback_query(F.data ==  'Javascript_learning')
async def ptyhon_explanation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Выбирите технологию", reply_markup=javascript_moduls_kb)


@dp.callback_query(F.data ==  'C++_learning')
async def ptyhon_explanation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Выбирите технологию", reply_markup=cplusplus_moduls_kb)


@dp.callback_query(F.data ==  'Git_learning')
async def git_explanation(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Выбирите технологию", reply_markup=git_moduls_kb)




async def main():
    dp.include_router(router=router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())