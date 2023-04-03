from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

shaharlar = {
    'Andijon': 'andijon', 'Buxoro': 'bukhara', "Farg'ona": 'fargona', 
    'Jizzax':'jizzax','Xorazm':'urganch', 'Namangan': 'namangan',
    'Navoiy': 'navoiy', 'Qashqadaryo':'qashqadaryo', "Qoraqalpog'iston":'qoraqalpoq',
    'Samarqand':'samarqand', 'Sirdaryo':'sirdaryo', 'Surxondaryo':'termiz',
    'Toshkent': 'toshkent'
}


menubtn = InlineKeyboardMarkup(row_width=2)

for k, v in shaharlar.items():
    button = InlineKeyboardButton(text=k, callback_data=v)
    menubtn.insert(button)

backbtn = InlineKeyboardMarkup()
backbtn.add(InlineKeyboardButton(text='🔙ortga', callback_data='back'))