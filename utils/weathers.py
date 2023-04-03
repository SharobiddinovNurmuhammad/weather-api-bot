import requests
import datetime

from data.config import API_KEY

async def weatherbot(text):
    iconka_kodlari = {
		"Clear": "Quyoshli havo \U00002600",
		"Clouds": "Bulutli havo \U00002601",
		"Rain": "Yomg'irli havo \U00002614",
		"Drizzle": "Yomg'irli havo \U00002614",
		"Thunderstorm": "Chaqmoq \U000026A1",
		"Snow": "Qor \U0001F328",
		"Mist": "Tuman \U0001F32B"
	}

    url = f'https://api.openweathermap.org/data/2.5/weather?q={text}&appid={API_KEY}&units=metric'
    data = requests.get(url).json()
    
    shahar = data['name']
    harorat = data['main']['temp']
    iconka = data['weather'][0]['main']
    if iconka in iconka_kodlari:
        icon = iconka_kodlari[iconka]
    else:
        icon = "Aniqlab bo'lmadi :)"

    namlik = data['main']['humidity']
    bosim = data['main']['pressure']
    shamol = data['wind']['speed']
    quyosh_chiqishi = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    quyosh_botishi = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    kunning_uzunligi = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

    text = f"Xozirgi Vaqt Bo'yicha ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})\n\n"\
		   f"{shahar} Shahar ob-havosi!\nHarorat: {harorat}°C {icon}\n"\
		   f"Namlik: {namlik}%\nBosim: {bosim} mm.sim.ust\nShamol: {shamol} m/s\n"\
		   f"Quyosh Chiqishi: {quyosh_chiqishi}\nQuyosh Botishi: {quyosh_botishi}\nKunning Uzunligi: {kunning_uzunligi}\n"
    return text

