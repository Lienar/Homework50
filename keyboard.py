from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

products = get_product_list()

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'Информация'),
         KeyboardButton(text = 'Рассчитать')],
        [KeyboardButton(text = 'Купить')]
    ],
    resize_keyboard = True
)

kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton (text = 'Формула расчёта', callback_data= 'formula'),
         InlineKeyboardButton (text = 'Рассчитать норму', callback_data= 'calories')]
    ],
    resize_keyboard = False
)

kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton (text = f'{products[0][1]}', callback_data= 'product_buying'),
         InlineKeyboardButton (text = f'{products[1][1]}', callback_data= 'product_buying')],
        [InlineKeyboardButton (text = f'{products[2][1]}', callback_data= 'product_buying'),
         InlineKeyboardButton (text = f'{products[3][1]}', callback_data= 'product_buying')],
        [InlineKeyboardButton (text = f'{products[4][1]}', callback_data= 'product_buying'),
         InlineKeyboardButton (text = f'{products[5][1]}', callback_data= 'product_buying')],
        [InlineKeyboardButton (text = f'{products[6][1]}', callback_data= 'product_buying'),
         InlineKeyboardButton (text = f'{products[7][1]}', callback_data= 'product_buying')],
        [InlineKeyboardButton (text = f'{products[8][1]}', callback_data= 'product_buying'),
         InlineKeyboardButton (text = f'{products[9][1]}', callback_data= 'product_buying')]
    ],
    resize_keyboard = False
)