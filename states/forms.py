import json

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from creds import main
from keyboards import reply

dp = main.dp


class RegistrationStates(StatesGroup):
    wait_for_feedback = State()


class RequestForm(StatesGroup):
    wait_for_name = State()
    wait_for_email = State()
    wait_for_comment = State()


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
    await msg.answer("Дякуємо! Ваша заявка на розгляді", reply_markup=reply.main_menu())
