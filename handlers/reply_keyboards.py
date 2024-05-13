from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards import inline, reply
from creds import main
from states import forms
from auth import main as auth


dp = main.dp


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
        await message.answer("Ви в під меню -- Контакти --", reply_markup=reply.sub_contacts())
    elif content == "Назад":
        await message.answer("Ви в головному меню!", reply_markup=reply.main_menu())
    elif content == "План занять":
        await message.answer("Оберіть модуль курсу:", reply_markup=inline.plan_menu())
    elif content == "👨‍🎨Про проєкт":
        await message.answer(text="Test: https://www.youtube.com/watch?v=KM2o3OyTtVU",
                             disable_web_page_preview=True)
    elif content == "😉Надіслати відгук":
        await message.answer(text="Напишіть свій відгук!")
        await state.set_state(forms.RegistrationStates.wait_for_feedback)
    elif content == "Надіслати заявку":
        await message.answer("Введіть своє ім*я: ")
        await state.set_state(forms.RequestForm.wait_for_name)
    elif content == "Надіслати картинку":
        img = FSInputFile("assets/media/barbie.webp")
        await main.bot.send_photo(cid, img, caption="It's barbie",
                                  protect_content=True)
    elif content == "chatGPT":
        await message.answer("Впишіть, що ви б хотіли дізнатись в мене: ")
        await state.set_state(forms.SimplePromptGPT.wait_for_prompt)

    elif content == "Надіслати групу фото":
        media_group = MediaGroupBuilder(
            caption="It's media group!"
        )
        media_group.add(type="photo", media=FSInputFile("assets/media/barbie.webp"))
        media_group.add(type="photo", media=FSInputFile("assets/media/barbie.webp"))
        media_group.add(type="photo", media=FSInputFile("assets/media/barbie.webp"))

        await main.bot.send_media_group(cid, media=media_group.build(),
                                        protect_content=True)
    elif content == "Екзотика":
        await main.bot.send_sticker(cid, FSInputFile('assets/media/barbie.webp'))
        await main.bot.send_venue(
            cid,
            36.545,
            52.123,
            "Test Title",
            "test address"
        )
    # --- admins ---
    if content == "Додати адміністратора":
        if auth.is_admin(cid):
            await message.answer("Введіть ID адміністратора:")
            await state.set_state(forms.AddNewAdmin.wait_for_admin_id)
        else:
            await message.answer("У вас немає доступу до цієї функції! зверніться до аміністрації!",
                                 reply_markup=reply.main_menu())
    elif content == "Розсилка":
        if auth.is_admin(cid):
            await message.answer("Введіть текст розсилки:", reply_markup=reply.admin_mass_sending())
            await state.set_state(forms.MassSending.wait_for_content_msg)


        else:
            await message.answer("У вас немає доступу до цієї функції! зверніться до аміністрації!",
                                 reply_markup=reply.main_menu())
