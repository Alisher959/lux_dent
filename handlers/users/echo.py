from aiogram import types
from keyboards.default.first_keyboard import menu
from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer('Uzur bunday buyruq topilmadi.\nPastdagi tugmalardan birini tanlang.', reply_markup=menu)
