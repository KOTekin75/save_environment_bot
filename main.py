import telebot
import random
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, """\
    Привет! Я бот, который поможет тебе заботиться о природе. Используй /advice для получения советов. 
    Я так же могу предоставить информацию о некоторых материалах из моей базы данных. По команде /materials
    можно узнать какие из материалов доступны.\
    """)

# Список советов по охране окружающей среды
advice_list = [
    "Сократите использование пластика. Используйте многоразовые сумки.",
    "Собирайте и перерабатывайте отходы. Разделяйте мусор на перерабатываемый и неперерабатываемый.",
    "Используйте общественный транспорт, чтобы уменьшить выбросы углекислого газа.",
    "Выключайте свет и электронику, когда они не нужны.",
    "Сажайте деревья и ухаживайте за растительностью.",
    "Используйте экологически чистые моющие средства и продукты.",
    "Экономьте воду, закрывайте кран, пока чистите зубы.",
    "Старайтесь покупать продукты местных производителей.",
]

# Список материалов и их вреда для окружающей среды
materials_info = {
    'пластик': {
        'harm': 'Пластик выделяет вредные химические вещества, которые могут попадать в окружающую среду.',
        'decomposition_time': 'От 100 до 1000 лет.'
    },
    'стекло': {
         'harm': 'При разложении стекло может выделять токсичные вещества.',
        'decomposition_time': 'От 1000 до 4000 лет.'
    },
    'бумага': {
        'harm': 'При разложении бумага потребляет кислород и может способствовать образованию метана.',
        'decomposition_time': 'От 2 до 6 месяцев.'
    },
}

@bot.message_handler(commands=['advice'])
def send_advice(message):
    advice = random.choice(advice_list)
    bot.send_message(message.chat.id, advice)

@bot.message_handler(commands=['materials'])
def list_materials(message):
  materials_list = ', '.join(materials_info.keys())
  response = f"Доступные материалы: {materials_list}"
  bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['info'])
def send_info(message):
    try:
        material_name = message.text.split(' ', 1)[1].lower() # Получаем название материала
        info = materials_info[material_name]
    
        response = f"**Материал:** {material_name.title()}\n"
        response += f"**Вред:** {info['harm']}\n"
        response += f"**Время разложения:** {info['decomposition_time']}"
    
        bot.send_message(message.chat.id, response, parse_mode='Markdown')
    except (IndexError, KeyError):
        bot.send_message(message.chat.id, "Пожалуйста, укажите действительное название материала.")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)