import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import random
import time
import os

TOKEN = '1200805567:AAEY0_cfflnR-9DlIi7viDs0G4riOdowey4'

logging.basicConfig(level=logging.INFO)

a = 0

class TS(Helper):
    mode = HelperMode.snake_case
    T_S1 = ListItem()
    T_S2 = ListItem()

bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

admi =['898287979']
com_text = ['p','i','p','l','p','i','p','l']

@dp.message_handler(commands=['start'])
async def star(msg: types.message):
    await msg.answer('Бот семейства Game of Thrones')


@dp.message_handler(commands=['empire'])
async def empire(msg: types.message):
    await msg.answer(com_text[0])

@dp.message_handler(commands=['nickname'])
async def nick(msg: types.message):
    await msg.answer(com_text[1])
    await msg.answer_photo('')
    await msg.answer_photo('')
    await msg.answer_photo('')
    await msg.answer(com_text[2])
@dp.message_handler(commands=['history'])
async def his(msg: types.message):
    await msg.answer(com_text[3])

@dp.message_handler(commands=['game'])
async def game(msg: types.message):
    await msg.answer(com_text[4])
    await msg.answer(com_text[5])
    await msg.answer(com_text[6])

@dp.message_handler(commands=['got'])
async def got(msg: types.message):
    await msg.answer(com_text[7])


@dp.message_handler(state='*',commands=['izm'])
async def iz(msg: types.message):
    if str(msg.from_user.id) in admi:
        state = dp.current_state(user=msg.from_user.id)
        await state.set_state(TS.all()[0])
        await msg.answer('Введите номер текста')
    else:
        await msg.answer('Вы не являетесь админом бота!')

@dp.message_handler(state=TS.T_S1)
async def nomber(msg: types.message):
    state = dp.current_state(user=msg.from_user.id)
    global a
    a = msg.text
    try:
     if (int(a)>=0) and (int(a)<=7):
         await state.set_state(TS.all()[1])
         await msg.answer('Отправте текст одним сообщением')
         @dp.message_handler(state=TS.T_S2)
         async def men(msg):
              global com_text
              global a
              com_text[int(a)] = msg.text
              await state.reset_state()
              await msg.answer('Готово!')

     else:
         await msg.answer('Нeверный номер текста! Попробуйте ещё раз!')
         await state.reset_state()
         await state.set_state(TS.T_S1)
    except:
        await msg.answer('Сообщение не является цифрой! Попробуйте ещё раз!')
        await state.reset_state()
        await state.set_state(TS.T_S1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)