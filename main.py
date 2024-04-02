import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7192658163:AAECXbCnH5sPWOh95FBp4HNVDbbrjfAUdQM"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)


# REPLY KEYBOARD
def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👨‍🎨Про проєкт")],
            [KeyboardButton(text="Реквізити"), KeyboardButton(text="План занять")],
            [KeyboardButton(text='Контакти')]
        ],
        resize_keyboard=True
    )
    return kb


def r_sub_contacts():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Соц. мережі"), KeyboardButton(text="Телефон")],
            [KeyboardButton(text='Назад')]
        ],
        resize_keyboard=True
    )


# INLINE KEYBOARD
def i_test_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Python Core", callback_data="plan_python_core")],
            [InlineKeyboardButton(text="HTML & CSS", callback_data="plan_html_css")],
            [InlineKeyboardButton(text="NEXT.js 14", callback_data="plan_next14")]
        ]
    )


@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    cid = callback_query.from_user.id
    print(f"DATA: {data}, CID: {cid}")


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML")
    await message.answer('Hello World! I am live!', reply_markup=r_main_menu())


@dp.message()
async def special_msg(message: types.Message) -> None:
    cid = message.chat.id
    content = message.text

    # commands
    if content == "/hide":
        await message.answer("You activated secret mode!", reply_markup=ReplyKeyboardRemove())

    # btn
    if content == "Реквізити":
        await message.answer("""
        <b>Найменування отримувача:</b> ФОП Лялюк Ігор Романович
<b>Код отримувача:</b> 3618507015
<b>Рахунок отримувача:</b> UA953052990000026005041024474
<b>Назва банку:</b> АТ КБ "ПРИВАТБАНК"
        """, parse_mode="HTML")
    elif content == "Контакти":
        await message.answer("Ви в під меню -- Контакти --", reply_markup=r_sub_contacts())
    elif content == "Назад":
        await message.answer("Ви в головному меню!", reply_markup=r_main_menu())
    elif content == "План занять":
        await message.answer("Оберіть модуль курсу:", reply_markup=i_test_menu())



async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
