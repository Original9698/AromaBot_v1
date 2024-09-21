import telebot
from telebot import types

bot = telebot.TeleBot('6996019691:AAGcNyYuHxaHMJna3Z0ZhBb9DeZbUcCuxEo', parse_mode=None)


def del_message(message):
    for i in range(20):
        try:
            bot.delete_message(message.chat.id, message.message_id - i)
        except Exception as e:
            print(f"Error deleting message: {e}")
            break


@bot.message_handler(content_types=['text'])
def pd_info(message):
    if message.text == 'Мне интересна продукция компании' or message.text == 'Вернуться к информации о продукции':
        if message.text == 'Вернуться к информации о продукции':
            del_message(message)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Однокомпонентные масла')
        btn2 = types.KeyboardButton(text='Смеси эфирных масел')
        btn3 = types.KeyboardButton(text='Пищевые добавки')
        btn4 = types.KeyboardButton(text='Наборы')
        btn5 = types.KeyboardButton(text='Aксессуары')
        btn6 = types.KeyboardButton(text='Линейки продукции')
        btn7 = types.KeyboardButton(text='Литература')
        btn8 = types.KeyboardButton(text='Ароматерапия с doTERRA')
        btn9 = types.KeyboardButton(text='География эфирных масел')
        btn10 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9,btn10, row_width=1)
        mess = """💧Эфирные масла doTERRA - это сертифицированные масла терапевтического
класса

✅В продукции doTERRA отсутствуют наполнители, синтетические масла,
загрязняющие вещества и токсины (химические удобрения, пестициды,
тяжелые металлы, промышленные выбросы, примеси).

✅Масла изготавливаются из растительного сырья, собранного в местах
естественного произрастания (регион, почва, влажность, высота над
уровнем моря) с соблюдением необходимых условий сбора (периодичность сбора, сезон, время суток).

✅Процесс изготовления соответствует технологии (оптимальная температура,
циркуляция пара и давления на протяжении всего процесса) и находится под тщательным контролем специалистов.

✅Готовые масла протестированы по составу в том числе в независимых научных лабораториях 8 аналитическими методами.

✅ Образцы каждой партии хранятся 5 лет для проверки в случае претензий.

➡️Я тебе сейчас тебе покажу основные направления продукции компании, и по каждому из них ты сможешь получить информацию!

"""
        photo = open('content/picture/pd_info0.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, mess, reply_markup=markup)

    elif message.text == 'Однокомпонентные масла':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Однокомпонентные масла',
                                              url='https://www.doterra.com/RU/ru_RU/pl/single-oils')
        markup_inl.add(btn_inl1,row_width=1)
        mess = """Однокомпонентные масла - это эфирные масла, полученные из одного растения или источника. Они могут быть использованы для различных целей, таких как ароматерапия, уход за кожей и волосами, а также для поддержания общего здоровья и благополучия.

На сайте компании doTERRA представлены различные однокомпонентные масла, каждое из которых имеет свои уникальные свойства и преимущества. Например:

 <b>•Лаванда:</b> известна своими успокаивающими и расслабляющими свойствами, часто используется для улучшения сна и снятия стресса.
 <b>•Чайное дерево:</b> имеет антибактериальные и противовоспалительные свойства, часто используется для лечения кожных проблем и поддержания здоровья волос.
 <b>•Эвкалипт:</b> известен своими очищающими и дезинфицирующими свойствами, часто используется для поддержания здоровья дыхательных путей и снятия симптомов простуды.
 <b>•Бергамот:</b> имеет антидепрессивные и анксиолитические свойства, часто используется для улучшения настроения и снятия стресса.
 <b>•Грейпфрут:</b> известен своими очищающими и тонизирующими свойствами, часто используется для поддержания здоровья кожи и волос.
 
Эти однокомпонентные масла можно использовать отдельно или в комбинации с другими маслами для достижения желаемого эффекта. На сайте doTERRA вы можете найти подробную информацию о каждом масле, включая его свойства, применение и противопоказания."""
        photo = open('content/picture/one_c.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl,parse_mode='html')


    elif message.text == 'Смеси эфирных масел':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Смеси эфирных масел',
                                              url='https://www.doterra.com/RU/ru_RU/pl/proprietary-blends')
        markup_inl.add(btn_inl1,row_width=1)
        mess = """Смеси эфирных масел - это уникальные комбинации однокомпонентных масел, созданные для достижения конкретных целей и результатов. Они могут быть использованы для ароматерапии, ухода за кожей и волосами, а также для поддержания общего здоровья и благополучия.

На сайте компании doTERRA представлены различные смеси эфирных масел, каждая из которых имеет свои уникальные свойства и преимущества. Например:

 <b>•On Guard:</b> смесь масел, которая помогает поддерживать здоровье иммунной системы и защитить организм от внешних факторов.
 <b>•Deep Blue:</b> смесь масел, которая помогает снимать мышечную и суставную боль, а также уменьшать воспаление.
 <b>•Breathe:</b> смесь масел, которая помогает поддерживать здоровье дыхательных путей и снимать симптомы простуды.
 <b>•DigestZen:</b> смесь масел, которая помогает поддерживать здоровье пищеварительной системы и уменьшать симптомы дискомфорта.
 <b>•Serenity:</b> смесь масел, которая помогает снимать стресс и тревогу, а также улучшать качество сна.
 
Эти смеси эфирных масел могут быть использованы в различных формах, таких как масла для ароматерапии, добавки к ванне, кремы и лосьоны для кожи. Они могут быть также использованы в сочетании с другими продуктами doTERRA для достижения максимального эффекта.

На сайте doTERRA вы можете найти подробную информацию о каждой смеси, включая ее свойства, применение и противопоказания. Кроме того, вы можете ознакомиться с отзывами наших клиентов, которые уже испытали на себе эффективность наших смесей эфирных масел.
"""
        photo = open('content/picture/one_c.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl,parse_mode='html')


    elif message.text == 'Пищевые добавки':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Пищевые добавки',
                                              url='https://www.doterra.com/RU/ru_RU/c/supplements')
        markup_inl.add(btn_inl1)
        mess = """
        Укрепите свое здоровье с пищевыми добавками doTERRA

В doTERRA мы разработали линейку пищевых добавок для поддержки общего благополучия. Наши добавки обеспечивают организм необходимыми питательными веществами, витаминами и минералами.

<b>Поддержка систем организма</b>
 <b>•Сердечно-сосудистая система:</b> поддержка здоровья сердца
 <b>•Иммунная система:</b> укрепление иммунитета
 <b>•Здоровье пищеварительной системы:</b> поддержка здоровой пищеварения
 <b>•Когнитивная функция:</b> поддержка здоровья мозга
Натуральные ингредиенты, непревзойденное качество
В doTERRA мы используем только ингредиенты высочайшего качества, свободные от искусственных наполнителей и консервантов.

Начните свой путь к оптимальному здоровью сегодня
        """
        photo = open('content/picture/one_c.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl,parse_mode='html')


    elif message.text == 'Наборы':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Наборы',
                                              url='https://www.doterra.com/RU/ru_RU/c/kits-and-collections')
        markup_inl.add(btn_inl1)
        mess = """
        <b>Сэкономьте время и деньги с наборами doTERRA</b>

В doTERRA мы понимаем, что каждый человек уникален, и у каждого свои цели и потребности в здоровье. Поэтому мы разработали линейку наборов, которые помогут вам достичь ваших целей быстрее и эффективнее.

<b>Выберите свой путь к здоровью</b>
Наше наборы категоризированы по целям и потребностям, чтобы помочь вам найти идеальный вариант для вашего тела. От наборов для поддержки иммунной системы до наборов для здоровья сердца, и от наборов для когнитивной функции до наборов для здоровья кожи, у нас есть вариант, который подходит вам.

<b>•Наборы для начинающих:</b> идеальный способ начать свой путь к здоровью с doTERRA
<b>•Наборы для здоровья:</b> поддержка общего благополучия и здоровья
<b>•Наборы для специфических целей:</b> поддержка иммунной системы, здоровья сердца, когнитивной функции и здоровья кожи

<b>Начните свой путь к здоровью сегодня</b>

Просмотрите наш ассортимент наборов и узнайте, как doTERRA может помочь вам достичь ваших целей здоровья и благополучия.
        """
        photo = open('content/picture/one_c.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl,parse_mode='html')


    elif message.text == 'Aксессуары':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Aксессуары',
                                              url='https://www.doterra.com/RU/ru_RU/pl/accessories')
        markup_inl.add(btn_inl1)
        mess = """
        <b>Удобство и стиль с аксессуарами doTERRA</b>

В doTERRA мы понимаем, что удобство и стиль играют важную роль в вашем пути к здоровью. Мы разработали аксессуары, упрощающие использование наших продуктов и делающие его более удобным.

<b>Удобство в использовании</b>
 •Контейнеры и сумки для хранения и транспортировки
 •Устройства для применения для эффективного использования
 •Дополнительные аксессуары для упрощения использования
 
<b>Стиль и качество</b>
Мы используем материалы высокого качества для долговечности и комфорта.

<b>Удобство и стиль в одном</b>

Просмотрите наш ассортимент аксессуаров и узнайте, как doTERRA может помочь вам.
        """
        photo = open('content/picture/one_c.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl,parse_mode='html')


    elif message.text == 'Линейки продукции':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Линейки продукции',
                                              url='https://www.doterra.com/RU/ru_RU/c/doterra-product-lines')
        markup_inl.add(btn_inl1)
        mess = """
        <b>Линейки продукции</b>
В doTERRA мы предлагаем различные линейки продукции, разработанные для удовлетворения ваших потребностей в эфирных маслах и продуктах для здоровья.

<b>Единичные масла</b>
•Натуральные, высококачественные масла для различных целей
•Используйте их по отдельности или в сочетании для достижения желаемого эффекта

<b>Смешанные масла</b>
•Уникальные сочетания масел для решения конкретных задач
•Используйте их для поддержки здоровья и благополучия

<b>Пищевые добавки</b>
•Натуральные добавки для поддержки здоровья и благополучия
•Используйте их для укрепления иммунитета, улучшения пищеварения и других целей

<b>Личная гигиена</b>
•Натуральные продукты для личной гигиены, разработанные для ухода за кожей и волосами
•Используйте их для поддержки здоровья и красоты
        """
        photo = open('content/picture/one_c.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl,parse_mode='html')

    elif message.text == 'Литература':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Литература',
                                              url='https://www.doterra.com/RU/ru_RU/pl/literature')
        markup_inl.add(btn_inl1)
        mess = """
        <b>Литература</b>
В этом разделе мы собрали различные публикации, которые помогут вам лучше понять преимущества эфирных масел и как они могут помочь вам в вашем пути к здоровью и благополучию.

<b>Научные исследования</b>
•Узнайте о последних научных открытиях и исследованиях в области эфирных масел
•Ознакомьтесь с результатами клинических испытаний и лабораторных исследований

<b>Практические советы</b>
•Получите полезные советы и рекомендации по использованию эфирных масел в повседневной жизни
•Узнайте, как эфирные масла могут помочь вам в различных ситуациях

<b>Книги и брошюры</b>
•Ознакомьтесь с нашими книгами и брошюрами, посвященными эфирным маслам и здоровью
•Узнайте о различных способах использования эфирных масел и их преимуществах
        """
        photo = open('content/picture/one_c.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl,parse_mode='html')

    elif message.text == 'Ароматерапия с doTERRA':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        mess = """
        <b>Ароматерапия с doTERRA</b>
Ароматерапия - это естественный способ улучшить свое физическое и эмоциональное благополучие. Используя высококачественные эфирные масла doTERRA, вы можете:

<b>Уменьшить стресс и напряжение</b>
•Используйте масла лаванды и бергамота для релаксации и уменьшения стресса
<b>Улучшить сон</b>
•Используйте масла ромашки и сандалового дерева для улучшения качества сна
<b>Укрепить иммунитет</b>
•Используйте масла чайного дерева и эвкалипта для укрепления иммунитета и защиты от болезней
<b>Улучшить настроение</b>
•Используйте масла лимона и грейпфрута для улучшения настроения и энергии

Мы предлагаем широкий спектр эфирных масел и продуктов для ароматерапии, чтобы помочь вам достичь своих целей в области здоровья и благополучия.
        """
        photo = open('content/picture/Aromatherapy.jpg', 'rb')
        bot.send_photo(message.chat.id, photo,caption=mess,reply_markup=markup,parse_mode='html')

    elif message.text == 'География эфирных масел':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о продукции')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)

        mess = """
        <b>География эфирных масел</b>
doTERRA является лидером в индустрии эфирных масел, и наша география охватывает более 40 стран мира. Мы сотрудничаем с местными фермерами и производителями, чтобы обеспечить высококачественные масла, выращенные в идеальных условиях.

<b>Африка</b>
•Кения: известная своими высококачественными маслами герани и лемонграсса
•Мадагаскар: родина уникальных масел, таких как масляное дерево и ваниль
<b>Европа</b>
•Франция: известная своими высококачественными маслами лаванды и розы
•Италия: родина масел лимона и апельсина
<b>Азия и Австралия</b>
•Индия: известная своими маслами сандалового дерева и пачули
•Австралия: родина масел чайного дерева и эвкалипта

Мы тщательно выбираем наши партнеров, чтобы обеспечить высококачественные масла, выращенные в соответствии с нашими строгими стандартами качества.
        """
        photo = open('content/picture/geography.jpg', 'rb')
        bot.send_photo(message.chat.id, photo,caption=mess, reply_markup=markup,parse_mode='html')



