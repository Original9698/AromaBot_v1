import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6996019691:AAGcNyYuHxaHMJna3Z0ZhBb9DeZbUcCuxEo', parse_mode=None)

name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('testSQL.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id,
                     f'Привет {message.from_user.first_name} {message.from_user.last_name}, сейчас тебя зарегистрирую! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()

    bot.send_message(message.chat.id, f'Введите пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('testSQL.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (name, password))
    conn.commit()
    cur.close()
    conn.close()
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, f'Пользователь зарегистрирован', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_1(callback):
    conn = sqlite3.connect('testSQL.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    info = ''
    for i in users:
        info += f'Имя: {i[1]}, пароль {i[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(callback.message.chat.id, info)


bot.polling(non_stop=True)
