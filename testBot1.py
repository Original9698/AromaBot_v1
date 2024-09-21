import telebot
from telebot import types

bot = telebot.TeleBot('6996019691:AAGcNyYuHxaHMJna3Z0ZhBb9DeZbUcCuxEo')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Ахуеть, вот это фото')


@bot.message_handler(commands=['wedding'])
def website(message):
    mark = types.InlineKeyboardMarkup()
    mark.add(types.InlineKeyboardButton(text='Принцесса, угадай что там',
                                          url='https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0_(%D0%B3%D0%BE%D1%80%D0%B0)'))
    bot.send_message(message.chat.id,'Узнайте больше о принцессах', reply_markup= mark)


@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text.lower() == 'video':
        video = open('text/video/Пиу [720] [audiovk.com].mp4', 'rb')
        bot.send_video(message.chat.id, video)
    elif message.text.lower() == 'music':
        music = open('text/music/N-Sync - Bye Bye Bye.mp3', 'rb')
        bot.send_audio(message.chat.id, music)
    elif message.text.lower() == 'picture':
        pic = open('text/pic/images.jpg', 'rb')
        bot.send_photo(message.chat.id, pic)
    else:
        mess = 'Я тебя не понимаю, иди нахуй'
        bot.send_message(message.chat.id, mess)


bot.polling(non_stop=True)
