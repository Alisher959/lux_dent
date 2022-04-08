from aiogram import types
from states.state_main import comment
from aiogram.dispatcher import FSMContext

from loader import dp, bot

@dp.message_handler(text='/users')
async def admin_users(message: types.Message):
    f = open('chat_id.txt', 'r')
    text = f.read()
    txt = text.split(',')
    f.close()    
    await message.answer(f"Bot statistikasi quyidagicha: \nBot lichkasidan foydalanayotganlar soni : {len(txt)-1} ta  ✅")

@dp.message_handler(text='/allusers')
async def admin_users(message: types.Message):
    f = open('users.txt', 'r')
    msg=''
    text1 = f.read()
    txt1 = text1.split(',')
    for i in range(0, len(txt1)-1):
        msg+=(f'{i+1}-foydalanuvchi @{txt1[i]}\n')
    f.close()    
    await message.answer(f"Bot statistikasi quyidagicha: \nBot lichkasidan foydalanayotganlar soni : {len(txt1)-1} ta  ✅\n{msg}")


@dp.message_handler(text='/reklama')
async def reklama(message: types.Message):
    f = open('chat_id.txt', 'r')
    text = f.read()
    txt = text.split(',')
    for i in range(0, len(txt)-1):
        chd = int(txt[i])
        k = open('reklama.txt', 'r')
        text = k.read()
        await bot.send_message(chat_id=chd, text=f"{text}")
        k.close()   
    f.close()       
    await  message.answer('reklama jo`natildi.')

@dp.message_handler(text='/reklama_edit')
async def reklama(message: types.Message):
    f = open('reklama.txt', 'r')
    text = f.read()
        
    f.close()       
    await  message.answer(f'Reklama texti \n{text}')
    await  message.answer('Reklama textini jo`nating!')
    await comment.reklama_edit_text.set()

@dp.message_handler(state=comment.reklama_edit_text)
async def reklama(message: types.Message, state: FSMContext):
    f = open('reklama.txt', 'w')
    f.write(message.text)
            
    await  message.answer('Reklama texti muvaffaqiyatli o`zgartirildi.')
    await state.finish()
    f.close()       