from states.state_main import comment
from aiogram import types
from keyboards.inline.subscription import check_button
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from keyboards.default.first_keyboard import menu
from data.config import CHANNELS
from loader import dp, bot
from utils.misc import subscription


@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)
    await message.answer(f"Salom, {message.from_user.first_name}! Botimizga xush kelibsiz", reply_markup=menu)

@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f" ✅✅✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f" ❌❌❌ <b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)

@dp.message_handler(text='💬 Fikr bildirish 💬')
async def send_comment(message: types.Message):
    await message.answer(f"💬 Marhamat fikringizni bildirish mumkin")
    await comment.comment_one.set()


@dp.message_handler(state=comment.comment_one)
async def comment_def(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=-1001799251338, text=f'@{message.from_user.username} dan fikr keldi\n{message.text}')
    await message.answer(f"Sizning fikringiz muvaffaqiyatli saqlandi")
    await state.finish()
