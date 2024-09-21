import telebot
from telebot import types

# import sqlite3

bot = telebot.TeleBot('6996019691:AAGcNyYuHxaHMJna3Z0ZhBb9DeZbUcCuxEo', parse_mode=None)

mess_id = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Узнай о выгоде с doTerra', callback_data='btn1')
    btn2 = types.InlineKeyboardButton(text='Расскажи мне о компании doTerra', callback_data='btn2')
    btn3 = types.InlineKeyboardButton(text='Расскажи мне о компании doTerra', callback_data='btn3')
    btn4 = types.InlineKeyboardButton(text='Мне интересно узнать о бизнесе', callback_data='btn4')
    btn5 = types.InlineKeyboardButton(text='Мне интересно узнать о бизнесе', callback_data='btn5')
    btn6 = types.InlineKeyboardButton(text='Мне интересно узнать о бизнесе', callback_data='btn6')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, row_width=1)

    mess = '''👉Ты находишься в главном меню и отсюда, ты сможешь выбрать любое интересующее тебя направление, а я смогу предоставить всю необходимую информацию об этом направлении!

Сразу оставлю контакты моего владельца: 

Галина Валгаева (@Galizozh)'''
    pic = open('content/main_menu/logo.png', 'rb')
    bot.send_photo(message.chat.id, pic, caption=mess, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'btn1':
        mess_id.clear()
        markup = types.InlineKeyboardMarkup()
        btn1_1 = types.InlineKeyboardButton(text='Главное меню', callback_data='btn1_1')
        markup.add(btn1_1, row_width=1)

        video = open('content/video/profit.mp4', 'rb')
        bot.send_video(callback.message.chat.id, video, reply_markup=markup)
        mess_id.append(callback.message.message_id)

        # bot.delete_message(callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'btn1_1':

        for i in range(len(mess_id)):
            try:
                bot.delete_message(callback.message.chat.id, callback.message.message_id - i)
            except Exception as e:
                print(f"Error deleting message: {e}")

        # bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        # bot.delete_message(callback.message.chat.id, callback.message.message_id - 2)
        # start(callback.message)
        # bot.edit_message_text('Edit text',callback.message.chat.id, callback.message.message_id)


    elif callback.data == 'btn2':
        mess_id.clear()
        markup = types.InlineKeyboardMarkup()
        btn2_1 = types.InlineKeyboardButton(text='Кто руководит компанией?', callback_data='btn2_1')
        btn1_1 = types.InlineKeyboardButton(text='Главное меню', callback_data='btn1_1')
        markup.add(btn2_1, btn1_1, row_width=1)
        mess = """👉Компания doTERRA была основана в 2008 году с целью распространения эфирных масел терапевтического класса по всему миру.

💧Испытав на себе целебное действие этих бесценных ресурсов, группа специалистов по медицине и бизнесу решила реализовать эту цель.

Мы основали компанию и назвали ее doTERRA — от латинского «дар земли». Мы делимся нашей продукцией со всем миром: в Европе, Азии и странах СНГ сотни тысяч людей доверяют бренду doTERRA!"""
        photo = open('content/picture/photo_2.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo, reply_markup=markup, caption=mess)
        mess_id.append(callback.message.message_id)


    elif callback.data == 'btn2_1':
        mess_id.clear()
        # bot.delete_message(callback.message.chat.id, callback.message.message_id)
        markup = types.InlineKeyboardMarkup()
        btn2_1_1 = types.InlineKeyboardButton(text='Шаг назад', callback_data='btn2_1_1')
        btn1_1 = types.InlineKeyboardButton(text='Главное меню', callback_data='btn1_1')
        markup.add(btn2_1_1, btn1_1, row_width=1)
        mess = """✅С удовольствием расскажу тебе о руководстве компании

😃Только представьте, 12 лет назад полезные свойства масел были неизвестны большинству людей, а доступ к ним был ограничен. 

🤩В то время, семь выдающихся личностей с горящим сердцем и ясным разумом объединились под предводительством Дэвида Стерлинга чтобы создать уникальную организацию - doTERRA. 

😍doTERRA - признанный мировой лидер в индустрии эфирных масел, отрасли, оцениваемой в 8 миллиардов долларов США. 

😎Благодаря Дэвиду, действующему руководителю doTERRA, и его врожденным лидерским качествам, компания продолжает расти, выходить на новые рынки, а также оказывать инициативную помощь поставщикам из неблагополучных районов Cō-Impact Sourcing, обеспечивая процветания всей семье doTERRA. 

😇Первоочередная задача для Дэвида - это развитие и рост людей, для которых он является мудрым и добрым наставником. Он считает, что его величайшие достижения — это прекрасные друзья, захватывающие приключения и невероятные возможности по оказанию помощи, созданные для всей семьи doTERRA."""
        photo = open('content/picture/photo_2_1.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo)
        mess_id.append(callback.message.message_id)
        bot.send_message(callback.message.chat.id, mess, reply_markup=markup)
        mess_id.append(callback.message.message_id)

    elif callback.data == 'btn2_1_1':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


bot.polling(non_stop=True)
