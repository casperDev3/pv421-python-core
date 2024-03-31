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

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7192658163:AAEDRlxQ1qBVGwKEQz3O1O4Xk_FZe1dHfqY"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)


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


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML")
    await message.answer('Hello World! I am live!', reply_markup=r_main_menu())


# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


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


@dp.message()
async def special_commands(message: types.Message) -> None:
    cid = message.chat.id
    content = message.text


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
