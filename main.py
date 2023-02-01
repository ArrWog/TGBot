import telebot
from telebot import types
import os


bot = bot(os.getenv('telebot.TeleBot'))


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler()
# def get_user_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'И тебе доброго времени суток', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'твой ID: {message.from_user.id}', parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('посетить GitHub', url='https://github.com/ArrWog?tab=overview&from=2022-12-01&to=2022-12-31'))
    bot.send_message(message.chat.id, "Перейдите на сайт", reply_markup=markup)


bot.polling(none_stop=True)
