import asyncio
import json
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
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7192658163:AAGVzkWMbNrY35qfw8jo0PZZ-ql28xvb5A0"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)


class RegistrationStates(StatesGroup):
    wait_for_feedback = State()


class RequestForm(StatesGroup):
    wait_for_name = State()
    wait_for_email = State()
    wait_for_comment = State()


# REPLY KEYBOARD
def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👨‍🎨Про проєкт")],
            [KeyboardButton(text="Реквізити"), KeyboardButton(text="План занять")],
            [KeyboardButton(text='Контакти')],
            [KeyboardButton(text='😉Надіслати відгук'), KeyboardButton(text='Надіслати заявку')]
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
def i_plan_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Python Core", callback_data="plan_python_core")],
            [InlineKeyboardButton(text="HTML & CSS", callback_data="plan_html_css")],
            [InlineKeyboardButton(text="NEXT.js 14", callback_data="plan_next14"),
             InlineKeyboardButton(text="Контакти", callback_data="plan_contacts")]
        ]
    )


@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    cid = callback_query.from_user.id
    msg_id = callback_query.message.message_id
    if data == "plan_python_core":
        # await bot.send_message(cid, "Program Python: ")
        await bot.edit_message_text(
            text="Program Python: https://drohobych.itstep.org/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_html_css":
        await bot.edit_message_text(
            text="HTML Program: https://drohobych.itstep.org/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_next14":
        await bot.edit_message_text(
            text="NEXT.js 14 Program: https://drohobych.itstep.org/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_contacts":
        await bot.delete_message(chat_id=cid, message_id=msg_id)
        await bot.send_message(cid, "Ви відкрили підменю контакти", reply_markup=r_sub_contacts())


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML")
    await message.answer('Hello World! I am live!', reply_markup=r_main_menu())


@dp.message(RegistrationStates.wait_for_feedback)
async def get_user_feedback(msg: types.Message, state: FSMContext):
    print("Requests", msg.text)
    await state.clear()


@dp.message(RequestForm.wait_for_name)
async def get_name_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Введіть вашу пошту: ")
    await state.set_state(RequestForm.wait_for_email)


@dp.message(RequestForm.wait_for_email)
async def get_email_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(email=msg.text)
    await msg.answer("Введіть ваш коментар: ")
    await state.set_state(RequestForm.wait_for_comment)


@dp.message(RequestForm.wait_for_comment)
async def get_comment_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(comment=msg.text)
    with open("data/requests.json", "r", encoding="utf-8") as file:
        all_req = json.load(file)
        req_data = await state.get_data()
        all_req.append(req_data)
    with open("data/requests.json", "w", encoding="utf-8") as f:
        json.dump(all_req, f)

    await state.clear()
    await msg.answer("Дякуємо! Ваша заявка на розгляді", reply_markup=r_main_menu())


@dp.message()
async def special_msg(message: types.Message, state: FSMContext) -> None:
    cid = message.chat.id
    content = message.text

    # commands
    if content == "/hide":
        await message.answer("You activated secret mode!", reply_markup=ReplyKeyboardRemove())
    elif content == "/spam":
        while True:
            await message.answer("This spam")

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
        await message.answer("Оберіть модуль курсу:", reply_markup=i_plan_menu())
    elif content == "👨‍🎨Про проєкт":
        await message.answer(text="Test: https://www.youtube.com/watch?v=KM2o3OyTtVU",
                             disable_web_page_preview=True)
    elif content == "😉Надіслати відгук":
        await message.answer(text="Напишіть свій відгук!")
        await state.set_state(RegistrationStates.wait_for_feedback)
    elif content == "Надіслати заявку":
        await message.answer("Введіть своє ім*я: ")
        await state.set_state(RequestForm.wait_for_name)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
