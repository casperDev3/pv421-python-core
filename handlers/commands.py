from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.markdown import hbold
from creds import main
from keyboards import reply
from auth import main as auth
import pandas as pd
import requests

dp = main.dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML")
    await message.answer('Hello World! I am live!', reply_markup=reply.main_menu())


@dp.message(Command("poll"))
async def poll(msg: types.Message):
    cid = msg.from_user.id
    await main.bot.send_poll(
        chat_id=cid,
        question="Test Question",
        options=["One", "Two"],
        type="regular",
        is_anonymous=False,
        allows_multiple_answers=True
    )


@dp.message(Command("admin"))
async def welcome_admin(msg: types.Message):
    if auth.is_admin(msg.from_user.id):
        await msg.answer("Вітає вам у режимі адміністратора", reply_markup=reply.admin_main())
    else:
        await msg.answer("You haven't access!", reply_markup=reply.main_menu())


@dp.message(Command("exel"))
async def generate_exel(msg: types.Message):
    products = requests.get("https://fakestoreapi.com/products")
    products = products.json()

    data = {
        'Title': [],
        'Price': [],
        'Description': [],
        'Category': [],
        'Image': []
    }

    for product in products:
        data["Title"].append(product["title"])
        data["Price"].append(product["price"])
        data["Description"].append(product["description"])
        data["Category"].append(product["category"])
        data["Image"].append(product["image"])


    df = pd.DataFrame(data)

    writer = pd.ExcelWriter('files/expl.xlsx', engine='openpyxl')

    df.to_excel(writer, sheet_name="Users", index=False)

    writer._save()

    await main.bot.send_document(chat_id=msg.from_user.id,
                                 document=FSInputFile("files/expl.xlsx"))
