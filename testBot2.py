import telebot
from telebot import types

bot = telebot.TeleBot('6996019691:AAGcNyYuHxaHMJna3Z0ZhBb9DeZbUcCuxEo', parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/connect_site')
    btn2 = types.KeyboardButton('/del_photo')
    btn3 = types.KeyboardButton('/change_text')
    markup.row(btn1)
    markup.row(btn2, btn3)
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html',reply_markup=markup)
    pic = open('text/pic/images.jpg', 'rb')
    bot.send_photo(message.chat.id, pic)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, click)

@bot.message_handler(commands=['connect_site','del_photo','change_text'])
def click(message):
    if message.text == '/connect_site':
        bot.send_message(message.chat.id, 'Идем на сайт')
    elif message.text == '/del_photo':
        bot.send_message(message.chat.id, 'Удаляем фото')
    elif message.text == '/change_text':
        bot.send_message(message.chat.id, 'Редачим текст')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://pytba.readthedocs.io/ru/latest/types.html')
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data = 'delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text',callback.message.chat.id, callback.message.message_id)

bot.polling(non_stop=True)
