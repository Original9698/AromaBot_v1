import telebot
from telebot import types

bot = telebot.TeleBot('6996019691:AAGcNyYuHxaHMJna3Z0ZhBb9DeZbUcCuxEo', parse_mode=None)


def del_message(message):
    for i in range(100):
        try:
            bot.delete_message(message.chat.id, message.message_id - i)
        except Exception as e:
            print(f"Error deleting message: {e}")
            break


@bot.message_handler(content_types=['text'])
def marketing(message):
    if message.text == 'Расскажи про маркетинг' or message.text == 'Вернуться к информации о маркетинге':
        if message.text == 'Вернуться к информации о маркетинге':
            del_message(message)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Премиальная продукция')
        btn2 = types.KeyboardButton(text='Бонус "БЫСТРЫЙ СТАРТ"')
        btn3 = types.KeyboardButton(text='Бонус VIP клиентов')
        btn4 = types.KeyboardButton(text='Бонус "СИЛА ТРЕХ"')
        btn5 = types.KeyboardButton(text='Бонус "UNILEVER"')
        btn6 = types.KeyboardButton(text='Бонус "ИНФИНИТИ ПУЛ"')
        btn7 = types.KeyboardButton(text='Бонус "ДАЙМОНД ПУЛ"')
        btn8 = types.KeyboardButton(text='Бонус "ОСНОВАТЕЛЕЙ"')
        btn9 = types.KeyboardButton(text='Лидерская часть маркетинг плана')
        btn10 = types.KeyboardButton(text='Вернуться к сути бизнес партнерства')
        btn11 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, row_width=1)
        mess = """🤝Здесь я тебе подробно расскажу обо всех ступеньках в маркетинге и какие премии выплачиваются при их достижении!
    
    😇Ниже я расположил ступени по мере возрастания товарооборота в твоей структуре и в каждом есть описание всех бонусов и премий!!
    
    😎Посмотри какой рост может быть уже в первый месяц, два, три в твоем бизнесе!"""
        photo = open('content/picture/marketing.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)

    elif message.text == 'Премиальная продукция':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😇Этот бонус начисляется тому, кто покупает продукцию doTERRA на 100 PV ежемесячно. 

😎А выдается премиальной продукцией. 

🤗Ее стоимость измеряется в процентах от набранных баллов. 

🤩Например, если 2–3 месяца подряд покупать продукцию «doterra» на 100 PV и больше, есть шанс получить премиальные товары на 10 % от PV. То есть на 10 PV или больше. 
😍Если продолжать в том же духе в течение 4–6 месяцев подряд, процент увеличится до 15 %. 

✅Максимальная премия положена тому, кто будет заказывать на 100 PV в течение 13 месяцев. Она составит 30 % от PV. 

⚠️Но если пропустить хотя бы один месяц, все придется начинать заново."""
        photo = open('content/picture/premium_prod.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)

    elif message.text == 'Бонус "БЫСТРЫЙ СТАРТ"':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😎Бонус «Быстрый старт» еженедельно выплачивается Инициаторам за Заказы, по которым начисляется комиссионные, сделанные в первые 60 (шестьдесят) дней их новыми Независимыми консультантами по продукции или Оптовыми клиентами. 

😍Такой бонус за нового Независимого консультанта по продукции выплачивается Инициаторам первого, второго и третьего уровней. 
✅Инициатор первого уровня получает 20 (двадцать) процентов, 
✅Инициатор второго уровня — 10 (десять) процентов, 
✅Инициатор третьего уровня — 5 (пять) процентов.

⚠️Чтобы претендовать на Бонус «Быстрый старт», каждый Инициатор должен заполнить бланк заказа по Программе вознаграждений за лояльность (LRP), заказав продукцию не менее, чем на 100 баллов PV за месяц, и оформить Квалифицированный заказ в рамках LRP."""
        photo = open('content/picture/fast_start.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)

    elif message.text == 'Бонус VIP клиентов':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """✅Стимулирует привлечение клиентов в компанию - розничная разница за клиентов, которых обслуживает компания Возврат за личные закупки свыше 100 PV = удешевление продукции для личного пользования."""
        photo = open('content/picture/vip_bonus.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)

    elif message.text == 'Бонус "СИЛА ТРЕХ"':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess1 = """😍Это возможность получать деньги за развитие своей команды. Данный бонус состоит из трех уровней квалификации.

🤗Как пройти 1-ю квалификацию?

✅Чтобы претендовать на бонус в размере 50 долларов США, Независимый консультант по продукции должен сделать Квалифицированный заказ в рамках LRP. 

😃Независимый консультант по продукции должен также иметь трех лично спонсируемых Независимых консультантов по продукции или трех лично привлеченных Оптовых клиентов с Квалифицированными заказами в рамках LRP и Командным объемом продаж (TV) не менее 600 баллов."""
        mess2 = """Как пройти 2-ю квалификацию?

Чтобы претендовать на бонус в размере 250 долларов США, Независимый консультант по продукции должен сначала получить бонус в размере 50 долларов США. Те трое лично спонсируемых Независимых консультантов по продукции или трое лично привлеченных Оптовых клиентов, которые помогли ему в получении Бонуса в размере 50 долларов США, должны также получить этот бонус в размере 50 долларов США."""
        mess3 = """Как пройти 3-ю квалификацию?

Чтобы претендовать на бонус в размере 1 500 долларов США, Независимый консультант по продукции должен сначала получить Бонус в размере 250 долларов США. Те трое лично спонсируемых Независимых консультантов по продукции или трое лично привлеченных Оптовых клиентов, которые помогли ему в получении Бонуса в размере 250 долларов США, должны также получить этот Бонус в размере 250 долларов США."""
        mess4 = """Преимущества бонуса "СИЛА ТРЕХ"
Данный бонус, ежемесячный, для Спонсоров в размере, эквивалентном 50, 250 или 1 500 долларов США."""
        photo1 = open('content/picture/three_forse/three_forse1.jpg', 'rb')
        photo2 = open('content/picture/three_forse/three_forse2.jpg', 'rb')
        photo3 = open('content/picture/three_forse/three_forse3.jpg', 'rb')
        photo4 = open('content/picture/three_forse/three_forse4.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1, caption=mess1, reply_markup=markup)
        bot.send_photo(message.chat.id, photo2, caption=mess2, reply_markup=markup)
        bot.send_photo(message.chat.id, photo3, caption=mess3, reply_markup=markup)
        bot.send_photo(message.chat.id, photo4, caption=mess4, reply_markup=markup)

    elif message.text == 'Бонус "UNILEVER"':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😃Бонус "UNILEVEL", позволяет получать от 2 % до 7 % с 1-й по 7-ю линии структуры в зависимости от ранга спонсора. 

Всего в карьерной лестнице «DOTERRA» 12 ступеней — от «Консультанта» до «Президентского Бриллианта». 
«Консультант» получает 2 % от 1-го уровня своей структуры. 
А «Президентскому Бриллианту» достается:
👉2 % от L1.
👉3 % от L2.
👉5 % от L3 и L4.
👉6 % от L5 и L6.
👉7 % от L7.
⚠️Но для этого ему нужно иметь 6 «ног». 
✅Причем в каждой из них должны быть лично рекрутированные представители уровня Platinum (это 9-я ступень карьерной лестницы).

⚠️Чтобы получать бонус «UNILEVEL», нужно выполнить еще два условия. А именно:

✅покупать продукцию doTERRA на 100 PV в течение 12 месяцев;
✅каждый квартал приводить нового человека.
Личное спонсорство позволяет Велнес Консультантам зарабатывать процент от заказов, размещенных участниками в их нижестоящих структурах."""
        photo = open('content/picture/unilever.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,mess,reply_markup=markup)


    elif message.text == 'Бонус "ИНФИНИТИ ПУЛ"':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😃Бонус «ИНФИНИТИ ПУЛ» Правила квалификации
👉Быть квалифицированным на соответствующий ранг в расчетном месяце
👉При изменении ранга в течение месяца дистрибьютор получает количество долей, соответствующее окончательному рангу"""
        photo = open('content/picture/infinity.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)

    elif message.text == 'Бонус "ДАЙМОНД ПУЛ"':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """😎Преимущества бонуса:
✅Все лидеры компании заинтересованы в успехе фирмы в целом. 
😃Высокие выплаты – 6% от 1 млрд в год!!!! 

👉Величина зависит от успеха всей лидерской команды компании, а не только от твоей организации. 
😍Распределение доходов - не только от того рынка, где ты работаешь, а от всех открытых рынков. 
😇Нет маргинального объема – распределяется полностью."""
        photo = open('content/picture/diamond.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)

    elif message.text == 'Бонус "ОСНОВАТЕЛЕЙ"':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess = """Бонус «ОСНОВАТЕЛЕЙ» 

Кто не рискует, тот не пьет шампанское! (народная мудрость)"""
        photo = open('content/picture/founders.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)

    elif message.text == 'Лидерская часть маркетинг плана':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(text='Мне интересно! Как зарегистрироваться')
        btn2 = types.KeyboardButton(text='Вернуться к информации о маркетинге')
        btn3 = types.KeyboardButton(text='Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, row_width=1)
        mess1 = """😎Это вторая часть маркетинг плана!

Лидерские бонусы, являются частью компенсационного плана doTERRA, который вознаграждает лидеров за командный успех всех Велнес Консультантов.

😎Виды Фондов Лидерства
😇Лидерский поощрительный фонд Бриллиантовый
🤝Суммарно ежемесячные выплаты по Фондам Лидерства составляют 7% от глобального объема компании doTERRA.
😍Объем компании — это суммарный объем Личного Объема (PV), реализованный через Велнес Консультантов doTERRA по всему миру."""
        mess2 = '''👉Лидерский Поощрительный Фонд — 4% выплат:
✅ • 1,25 % - Бонус Возможностей
✅ • 2% - Лидерский Поощрительный Фонд
✅ • 1% - Бриллиантовый Поощрительный Фонд

👉Бриллиантовый Фонд — 3% выплат:
✅1% - Бриллиантовый Фонд
✅1% - Голубой Бриллиантовый Фонд
✅1% - Президентский Бриллиантовый Фонд

Доли
✅Каждый месяц общий объем каждого Фонда Лидерства делится на равные доли.
✅Одна доля — это часть от общего объема опеделенного Фонда, сформированного от обьема Компании. Количество долей, которые может получить Велнес Консультант, зависит от достигнутого Статуса.
✅Чтобы заработать дополнительные доли в в Лидерском поощрительном и Бриллиантовом фондах, лично зарегистрированный нижестоящий Консультант должен впервые достичь определенного Статуса в текущем месяце. Требования к Статусу варьируются в зависимости от фонда.'''
        photo = open('content/picture/lead_manage.jpg', 'rb')
        bot.send_message(message.chat.id, mess1)
        bot.send_photo(message.chat.id, photo, caption=mess2, reply_markup=markup)
