import telebot
from telebot import types
from marketing_info import marketing, del_message
from product_info import pd_info

# import sqlite3

bot = telebot.TeleBot('6996019691:AAGcNyYuHxaHMJna3Z0ZhBb9DeZbUcCuxEo', parse_mode=None)

manage_text = ['Премиальная продукция',
               'Бонус "БЫСТРЫЙ СТАРТ"',
               'Бонус VIP клиентов',
               'Бонус "СИЛА ТРЕХ"',
               'Бонус "UNILEVER"',
               'Бонус "ИНФИНИТИ ПУЛ"',
               'Бонус "ДАЙМОНД ПУЛ"',
               'Бонус "ОСНОВАТЕЛЕЙ"',
               'Лидерская часть маркетинг плана']

product_text = ['Однокомпонентные масла',
                'Смеси эфирных масел',
                'Пищевые добавки',
                'Наборы',
                'Aксессуары',
                'Линейки продукции',
                'Литература',
                'Ароматерапия с doTERRA',
                'География эфирных масел',
                'Вернуться в главное меню']


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(text='Узнай о выгоде с doTERRA')
    btn2 = types.KeyboardButton(text='Расскажи мне о компании doTERRA')
    btn3 = types.KeyboardButton(text='Мне интересно узнать о бизнесе')
    btn4 = types.KeyboardButton(text='Мне интересна продукция компании')
    btn5 = types.KeyboardButton(text='Почему сегодня - doTERRA')
    markup.add(btn1, btn2, btn3, btn4, btn5, row_width=1)

    mess = '''👉Ты находишься в главном меню и отсюда, ты сможешь выбрать любое интересующее тебя направление, а я смогу предоставить всю необходимую информацию об этом направлении!

Сразу оставлю контакты моего владельца: 

Галина Валгаева (@Galizozh)'''
    pic = open('content/main_menu/logo.png', 'rb')
    bot.send_photo(message.chat.id, pic, caption=mess, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == 'Узнай о выгоде с doTERRA':
        markup1 = types.ReplyKeyboardMarkup()
        main_menu = types.KeyboardButton(text='Вернуться в главное меню')
        markup1.add(main_menu, row_width=1)
        video = open('content/video/profit.mp4', 'rb')
        bot.send_video(message.chat.id, video, reply_markup=markup1)


    elif message.text == 'Вернуться в главное меню':
        del_message(message)
        start(message)

    elif message.text == 'Расскажи мне о компании doTERRA' or message.text == 'Вернуться к информации о компании':
        if message.text == 'Вернуться к информации о компании':
            del_message(message)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Кто руководит компанией?')
        main_menu = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, main_menu, row_width=1)
        mess = """👉Компания doTERRA была основана в 2008 году с целью распространения эфирных масел терапевтического класса по всему миру.

        💧Испытав на себе целебное действие этих бесценных ресурсов, группа специалистов по медицине и бизнесу решила реализовать эту цель.

        Мы основали компанию и назвали ее doTERRA — от латинского «дар земли». Мы делимся нашей продукцией со всем миром: в Европе, Азии и странах СНГ сотни тысяч людей доверяют бренду doTERRA!"""
        photo = open('content/picture/photo_2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup, caption=mess)

    elif message.text == 'Кто руководит компанией?':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться к информации о компании')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        mess = """✅С удовольствием расскажу тебе о руководстве компании

        😃Только представьте, 12 лет назад полезные свойства масел были неизвестны большинству людей, а доступ к ним был ограничен. 

        🤩В то время, семь выдающихся личностей с горящим сердцем и ясным разумом объединились под предводительством Дэвида Стерлинга чтобы создать уникальную организацию - doTERRA. 

        😍doTERRA - признанный мировой лидер в индустрии эфирных масел, отрасли, оцениваемой в 8 миллиардов долларов США. 

        😎Благодаря Дэвиду, действующему руководителю doTERRA, и его врожденным лидерским качествам, компания продолжает расти, выходить на новые рынки, а также оказывать инициативную помощь поставщикам из неблагополучных районов Cō-Impact Sourcing, обеспечивая процветания всей семье doTERRA. 

        😇Первоочередная задача для Дэвида - это развитие и рост людей, для которых он является мудрым и добрым наставником. Он считает, что его величайшие достижения — это прекрасные друзья, захватывающие приключения и невероятные возможности по оказанию помощи, созданные для всей семьи doTERRA."""
        photo = open('content/picture/photo_2_1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, mess, reply_markup=markup)

    elif message.text == 'Мне интересно узнать о бизнесе' or message.text == 'Вернуться к информации о бизнесе':
        if message.text == 'Вернуться к информации о бизнесе':
            del_message(message)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Секреты бизнеса в doTERRA')
        btn2 = types.KeyboardButton(text='Узнать о системе продвижения в бизнесе')
        btn3 = types.KeyboardButton(text='Я новичок и хочу научиться')
        btn4 = types.KeyboardButton(text='У меня есть опыт, давай к маркетингу')
        btn5 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, row_width=1)
        mess = """😎Отличное решение!

😇Я помогу тебе узнать, как легко можно строить бизнес, будучи партнером компании dōTERRA!

🤩Давай только определимся сначала, что ты знаешь о бизнесе?!

🙃Ты новичок или уже был опыт в таком партнерстве?!"""
        bot.send_message(message.chat.id, mess, reply_markup=markup)

    elif message.text == 'Секреты бизнеса в doTERRA':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о бизнесе')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """✅Я расскажу тебе 10 секретов успешного бизнеса в компании dōTERRA!

😎Обычно про секреты говорят, что бы никому не говорили, но чем больше ты о них расскажешь людям - тем большего успеха ты добьешься!

➡️1. Продукт! Гениальные инновационные решения, качество и натуральность сырья! Сотни тысяч поклонников продукта! Сертификаты продукции ISO, GMP, FDA, НАССР
➡️2. Люди! Сюда приходят люди с осмысленным восприятием бизнеса!
➡️3. Наставники! Люди с богатейшим опытом в бизнесе делятся им с тобой!
➡️4. Маркетинг план! Он настолько сбалансирован и продуман, что сотни тысяч людей вполне успешно зарабатывают именно в партнерстве с dōTERRA
➡️5. Система! Современные и проверенные годами системы бизнеса позволяют из любого человека сделать предпринимателя! Если он того хочет сам!
➡️6. Популярность! Огромное количество знаменитостей, спортсменов, блоггеров - пользуются продукцией dōTERRA
➡️7. Стабильность! С 2008 года на отечественном рынке! 12 лет на международном! Это ли не стабильность? Она самая!  
➡️8. Динамика! Компания dōTERRA сегодня - это 65 открытых для бизнеса стран! И продолжает идти вперед!
➡️9. Потенциал! Прогрессивное производство. Оборудование мирового уровня
Современные технологические линии из Японии, Кореи, Китая, Европы и России, сертифицированные по международным стандартам качества.
➡️10. Вера в себя! Лучшее для людей - сегодня делаем мы!"""
        photo = open('content/picture/about_bisness.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, mess, reply_markup=markup)


    elif message.text == 'Мне интересно! Как зарегистрироваться':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, row_width=1)
        markup_inl = types.InlineKeyboardMarkup()
        btn_inl1 = types.InlineKeyboardButton(text='Регистрация',
                                              url='http://mydoterra.com/Galizozh')
        markup_inl.add(btn_inl1, row_width=1)
        mess = """😎Это легко!

😊Вот твоя ссылка для регистрации и добро пожаловать в команду: 

✍️После регистрации напиши моему владельцу, вот его телеграм

Галина Валгаева (@Galizozh)

🤝Что бы вы могли сразу начинать строить бизнес, он дал тебе инструменты и посвятил в курс дела!

😇Если я могу тебе еще чем-то помочь - переходи в главное меню - я полностью в твоем распоряжении!"""

        photo = open('content/picture/welcome.png', 'rb')
        bot.send_photo(message.chat.id, photo, reply_markup=markup)
        bot.send_message(message.chat.id, mess, reply_markup=markup_inl)


    elif message.text == 'Узнать о системе продвижения в бизнесе':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о бизнесе')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """Система построения бизнеса в компании dōTERRA очень многогранна, и постепенно ты узнаешь все тонкости грамотного развития своей структуры, через:

✅создание трафика
✅личного бренда
✅использования автоматизированных систем
✅навыков эффективного общения и коммуникации
✅навыки телефонных переговоров
✅использования мессенджеров и социальных сетей
и еще многое другое и все это доступно для тебя!

Всего я сейчас не смогу тебе рассказать - меня так запрограммировали, что информация - она только для партнеров компании)

Ну, в качестве одного из примеров - посмотри на меня)

Я могу и рассказать, и показать, и зарегистрировать и помочь по всем вопросам бизнеса, продукта, маркетинга, в то время пока мой владелец работает с командой или отдыхает с семьей)"""
        photo = open('content/picture/sistem_prod_bis.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)


    elif message.text == 'Я новичок и хочу научиться' or message.text == 'Вернуться к информации для новичков':
        if message.text == 'Вернуться к информации для новичков':
            del_message(message)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='В чем суть бизнес партнерства?')
        btn2 = types.KeyboardButton(text='За что платит компания?')
        btn3 = types.KeyboardButton(text='Как правильно начать бизнес?')
        btn4 = types.KeyboardButton(text='Вернуться к информации о бизнесе')
        btn5 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, row_width=1)
        mess = """😇Все когда-то были в чем-то новички! 

🙃И поверь, это лучшее что могло с тобой сейчас произойти!

😍Есть такая мысль о том, что человека проще научить чему то, чем переобучить!

🤩Давай начнем по порядку!"""

        bot.send_message(message.chat.id, mess, reply_markup=markup)

    elif message.text == 'В чем суть бизнес партнерства?' or message.text == 'Вернуться к сути бизнес партнерства':
        if message.text == 'Вернуться к сути бизнес партнерства':
            del_message(message)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Расскажи про маркетинг')
        btn2 = types.KeyboardButton(text='Вернуться к информации для новичков')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😎Это самый частый вопрос)

✅Компания заинтересована в своем развитии и выбирая между традиционным (привычным многим предпринимателям) путем развития - она выбрала именно сетевой способ!

➡️Чем он лучше? Все просто!

✨Представь, что у тебя есть товар или продукт!

Что бы его реализовать тебе надо:
⭕️- сделать магазин (а это аренда, коммуналка, все разрешения санэпидем, противопожарные комиссии, налоговая отчетность, бухгалтерия и т.д.) - это стоит больших денег!💰💰💰
⭕️- нанять продавцов, платить им зарплату, пенсионные и страховые отчисления (это тоже стоит денег) 💰💰💰
⭕️- организовать логистику (это дорого)  💰💰💰
⭕️- реклама (это еще дороже чем все выше перечисленное) 💰💰💰
❌- Выжить хотя бы первый год в таких условиях крайне трудно!

По статистике 90% бизнесов разваливается в первый год!

А в сетевом?

Все легко - компания платит ЛЮДЯМ все вышеперечисленные деньги - за фактическую реализацию товара!

За рекламу, за продвижение, за логистику и если ты посмотришь маркетинг, то тебе платят 💰💰💰💰💰💰💰💰💰💰💰💰 - все то, что традиционный предприниматель платил бы налево-направо!"""

        bot.send_message(message.chat.id, mess, reply_markup=markup)

    elif message.text == 'За что платит компания?':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Расскажи про маркетинг')
        btn2 = types.KeyboardButton(text='Вернуться к информации для новичков')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😎Этот вопрос тоже интересен!

✅Часто люди считают что в сетевом бизнесе платят за то, что ты продавец продукта какой-то компании!

➡️И это в корне не правильно!

✨На самом деле, в компании dōTERRA платят практически за каждый твой шаг в бизнесе)

🤝Порекомендовал(-а) продукт - и его кто-то заказал - получи прибыль!💰

🤝Рассказал(-а) кому-то о возможностях бизнеса - получи прибыль!💰

🤝Построил(-а) команду - получи прибыль!💰

Суть простая - рассказывать и показывать)

И именно за это компания тебе готова платить большие деньги!

😇За то что ты рассказываешь о ее продукте и бизнесе!"""

        bot.send_message(message.chat.id, mess, reply_markup=markup)

    elif message.text == 'Как правильно начать бизнес?':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Расскажи про маркетинг')
        btn2 = types.KeyboardButton(text='Вернуться к информации для новичков')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😇У тебя будет целая школа по этому направлению, во главе с твоим наставником - моим владельцем!

😃Мы будем с тобой планомерно и поэтапно осваивать все тонкости этого бизнеса и шаг за шагом придем вместе к результату!"""

        bot.send_message(message.chat.id, mess, reply_markup=markup)

    elif message.text == 'Расскажи про маркетинг' or message.text == 'Вернуться к информации о маркетинге' or message.text in manage_text:
        marketing(message)


    elif message.text == 'У меня есть опыт, давай к маркетингу' or message.text == 'Вернуться маркетингу':
        if message.text == 'Вернуться маркетингу':
            del_message(message)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Можно посмотреть видео!')
        btn2 = types.KeyboardButton(text='Расскажи про маркетинг')
        btn3 = types.KeyboardButton(text='Вернуться к информации о бизнесе')
        btn4 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, row_width=1)
        mess = """✅Отлично!

😎Давай знакомиться с маркетингом!

😇Как тебе будет удобнее, что бы я рассказал тебе все сам или небольшое видео с разбором маркетинга?"""

        photo = open('content/picture/marketing2.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)


    elif message.text == 'Можно посмотреть видео!':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться маркетингу')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😇В этом небольшом видео - ты узнаешь все о маркетинге компании!

😎Кто-то скажет что "Ой, это долго", "У меня нет времени"
🙃Долго, это 5 лет учиться в институте, что бы потом зарабатывать по 30-40 тысяч в месяц... Вот это ДОЛГО!

😃А потратить несколько минут, что бы понять, как зарабатывать 50 и более тысяч уже через пару месяцев - это не долго!
Это маленький миг!

😇Приятного просмотра!"""
        video = open('content/video/Marketing_plan_doTERRA_for_15_min.mp4', 'rb')
        bot.send_video(message.chat.id, video, caption=mess, reply_markup=markup)


    elif message.text == 'Мне интересна продукция компании' or message.text == 'Вернуться к информации о продукции' or message.text in product_text:
        pd_info(message)

    elif message.text == 'Почему сегодня - doTERRA':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, row_width=1)
        mess = """Когда меня, как бота создавали - нашлось столько информации о компании! Но, что бы вместить ее всю - понадобилось бы тома и библиотеки читать которые было скучно!

Столько плюсов нет ни у одной компании на современном рынке!

➡️Это и собственное производство
➡️И контракты с Российским Олимпийским комитетом
➡️И многонациональность рынка и продукта dōTERRA
➡️И мы решили сделать всего лишь один короткий ролик!

Увидев который ты поймешь раз и навсегда почему сегодня именно  dōTERRA
"""
        video = open('content/video/10_years_dōTERRA.mp4', 'rb')
        bot.send_video(message.chat.id, video, caption=mess, reply_markup=markup)


bot.polling(non_stop=True)
