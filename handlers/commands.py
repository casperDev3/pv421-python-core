import pdfkit
from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.markdown import hbold
from creds import main
from keyboards import reply
from auth import main as auth
import pandas as pd
import requests
import qrcode

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


@dp.message(Command("pdf"))
async def generate_pdf(msg: types.Message):
    html_content = """
    <!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<style>
h1{
color: #f00;
}
</style>
<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
</body>
</html>
    """
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    output_file = 'files/tpl.pdf'
    pdfkit.from_string(html_content, output_file, configuration=config)

    await main.bot.send_document(chat_id=msg.from_user.id,
                                 document=FSInputFile(output_file))


@dp.message(Command("qr"))
async def generate_qr(msg: types.Message):
    # Create a QR code object with a larger size and higher error correction
    qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Define the data to be encoded in the QR code
    data = "https://www.youtube.com/watch?v=xgQSGD7ok7s"

    # Add the data to the QR code object
    qr.add_data(data)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code with a black fill color and white background
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save("files/qr_code.png")

    await main.bot.send_photo(chat_id=msg.from_user.id,
                              photo=FSInputFile('files/qr_code.png'))
