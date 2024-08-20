import aiogram
import keyboard
from crud_functions import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import asyncio






api = "7308792898:AAG29SEzQcPX10e0XCuDuvbuQbK_C19XYwc"
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

##Блок клавиатур



##Конец блока клавиатур

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def set_keyboard(message):
    await message.answer("Привет! Я бот помогающий вашему здоровью.", reply_markup = keyboard.kb)

@dp.message_handler(text='Рассчитать')
async def set_start(message):
    await message.answer("Выберите опцию", reply_markup = keyboard.kb2)

#Пользователь
@dp.callback_query_handler(text = 'formula')
async def set_formula(call):
    await call.message.answer("Формула для расчета:")
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()
    await call.message.answer("Выберите опцию", reply_markup=keyboard.kb2)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Начало рассчета")
    await call.message.answer("Введите ваш возраст")
    await call.answer()
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age_now = message.text)
    data = await state.get_data()
    await message.answer("Введите ваш рост в сантиметрах")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_now = message.text)
    data = await state.get_data()
    await message.answer("Введите ваш вес")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight_now = message.text)
    data = await state.get_data()
    answer = (10 * int(data['age_now'])) + (6.25 * float(data['growth_now'])) - (5 * int(data['age_now'])) + 5
    await message.answer(f"Ваша норма {answer} калорий")
    await state.finish()
#Конец блока пользователь

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_product_list()
    i = 1
    for product in products:
        info_text = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}"
        with open(f'files/{i}.png', "rb") as img:
            await message.answer_photo(img, info_text)
        i += 1
        #await message.answer(info_text)
    await message.answer("Выберите продукт для покупки:", reply_markup=keyboard.kb3)


@dp.callback_query_handler(text = 'product_buying')
async def set_formula(call):
    await call.message.answer("Вы успешно приобрели продукт!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)


