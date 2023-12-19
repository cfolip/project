import telebot
from telebot import types
TOKEN = '6943988498:AAHYVMFmqMeAyIelnoBhhgRKIuPL8dnCjJ4'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Что такое утилита top')
    item2 = types.KeyboardButton('Запуск команды top')
    item5 = types.KeyboardButton('Интерфейс')
    item3 = types.KeyboardButton('Сортировка списка процессов')
    item4 = types.KeyboardButton('Вопросы из зачёта о команде top и ответы на них')
    markup.add(item1, item2, item5, item3, item4)
    file = open('./topnachalo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}. Здесь вы сможете узнать всё об утилите top в Linux. Это поможет ответить на вопросы при зачёте'.format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Интерфейс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            a = types.KeyboardButton('Верхняя рабочая зона')
            b = types.KeyboardButton('Основная рабочая зона')
            back = types.KeyboardButton('Назад')
            markup.add(a, b, back)
            bot.send_message(message.chat.id, 'Выберите рабочую зону, о которой хотите узнать информацию', reply_markup=markup)
        elif message.text == 'Верхняя рабочая зона':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            a = types.KeyboardButton('1 строка top')
            b = types.KeyboardButton('2 строка Tasks')
            c = types.KeyboardButton('3 строка %Cpu(S)')
            d = types.KeyboardButton('4 и 5 строка KiB Mem, KiB Swap')
            back3 = types.KeyboardButton('Вернуться к выбору рабочей зоны')
            markup.add(a, b, c, d,  back3)
            file = open('./verzona.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.chat.id,
                             'Верхняя рабочая зона содержит сведения о времени работы сервера, свободных и занятых ресурсах, пользователях;',
                             reply_markup=markup)
            bot.send_message(message.chat.id, 'Выберите нужую вам строку', reply_markup=markup)
        elif message.text == 'Основная рабочая зона':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            a = types.KeyboardButton('PID')
            b = types.KeyboardButton('USER')
            m = types.KeyboardButton('PR')
            d = types.KeyboardButton('NI')
            e = types.KeyboardButton('VIRT')
            f = types.KeyboardButton('RES')
            g = types.KeyboardButton('SHR')
            h = types.KeyboardButton('S')
            i = types.KeyboardButton('%CPU')
            j = types.KeyboardButton('%MEM')
            k = types.KeyboardButton('TIME+')
            l = types.KeyboardButton('COMMAND')
            back3 = types.KeyboardButton('Вернуться к выбору рабочей зоны')
            markup.add(a, b, m, d, e, f, g, h, i, j, k, l, back3)
            file = open('./osnzona.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.chat.id,
                             'Основная рабочая зона - это динамически обновляемая таблица, содержащая сведения о процессах.',
                             reply_markup=markup)
            bot.send_message(message.chat.id, 'Так выглядит "основная рабочая зона". Чтобы узнать значение каждого столбца - выберите нужный вам столбец, о котором хотите узнать', reply_markup=markup)
            bot.send_message(message.chat.id, 'Выберите нужный вам столбец', reply_markup=markup)
        elif message.text == 'Вернуться к выбору рабочей зоны':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Верхняя рабочая зона')
            item2 = types.KeyboardButton('Основная рабочая зона')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выберите рабочую зону заново', reply_markup=markup)

        elif message.text == '1 строка top':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Вернуться к выбору строки')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id, 'В верхнем левом углу экрана отображено текущее время, за которым следует время безотказной работы системы. Далее в строке идет количество активных сеансов пользователя.Далее Load average', reply_markup=markup)
        elif message.text == 'Вернуться к выбору строки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            a = types.KeyboardButton('1 строка top')
            b = types.KeyboardButton('2 строка Tasks')
            c = types.KeyboardButton('3 строка %Cpu(S)')
            d = types.KeyboardButton('4 и 5 строка KiB Mem, KiB Swap')

            back3 = types.KeyboardButton('Вернуться к выбору рабочей зоны')
            markup.add(a, b, c, d, back3)
            bot.send_message(message.chat.id, 'Выберите заново рабочую зону', reply_markup=markup)
        elif message.text == '2 строка Tasks':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            final = types.KeyboardButton('Вернуться к началу')
            back4 = types.KeyboardButton('Вернуться к выбору строки')
            markup.add(back4, final)
            bot.send_message(message.chat.id, 'В разделе Tasks отображается статистика процессов, выполняемых в вашей системе. Далее перечислено общее количество процессов, активные, спящие, остановленные и процессы-зомби.', reply_markup=markup)
        elif message.text == '3 строка %Cpu(S)':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Вернуться к выбору строки')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4,final)
            bot.send_message(message.chat.id, ' Раздел использования CPU показывает процентное время процессорного времени, затрачиваемого на различные задачи.', reply_markup=markup)
        elif message.text == '4 и 5 строка KiB Mem, KiB Swap':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Вернуться к выбору строки')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id, ' Они указывают общее, использованное и свободное количество памяти',reply_markup=markup)
        elif message.text == 'PID':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id, 'идентификатор процесса', reply_markup=markup)
        elif message.text == 'USER':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id, 'Это эффективное имя пользователя (соответствующее идентификатору пользователя) пользователя, который запустил этот процесс. Linux назначает реальный идентификатор пользователя и эффективный идентификатор пользователя для процессов; последний позволяет процессу действовать от имени другого пользователя. Например, пользователь, не являющийся пользователем root, может с правами root установить пакет.', reply_markup=markup)
        elif message.text == 'PR':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,'текущий приоритет процесса',reply_markup=markup)
        elif message.text == 'NI':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'Поле показывает nice-значение процесса. Значение nice - это десятичное представление приоритета процесса в системном планировщике заданий. Чем больше число, тем ниже приоритет. Ноль означает, что процесс необходимо запустить с базовым приоритетом планирования.',
                             reply_markup=markup)
        elif message.text == 'VIRT':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'полный объем виртуальной памяти, которую занимает процесс.',
                             reply_markup=markup)
        elif message.text == 'RES':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             ' текущее использование оперативной памяти',
                             reply_markup=markup)
        elif message.text == 'SHR':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'Объем памяти, совместно используемый другими процессами.',
                             reply_markup=markup)
        elif message.text == 'S':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'В этом поле отображается состояние процесса в однобуквенной форме(R - Runnable, D - Interruptible sleep, S - Uninterruptible sleep, T - Stopped, Z - Zombie).',
                             reply_markup=markup)
        elif message.text == '%CPU':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'Параметр выражает объем в процентах от общей доступной оперативной памяти ОЗУ. Показывает процент загрузки ядра',
                             reply_markup=markup)
        elif message.text == '%MEM':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'RES в процентах от общего количества памяти;',
                             reply_markup=markup)
        elif message.text == 'TIME+':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'Общее время процессора, используемое процессом с момента его начала, с точностью до сотых долей секунды.',
                             reply_markup=markup)
        elif message.text == 'COMMAND':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back4 = types.KeyboardButton('Выбрать столбец заново ')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back4, final)
            bot.send_message(message.chat.id,
                             'показывает с помощью какой команды запустили процесс.',
                             reply_markup=markup)
        elif message.text == 'Выбрать столбец заново':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            a = types.KeyboardButton('PID')
            b = types.KeyboardButton('USER')
            m = types.KeyboardButton('PR')
            d = types.KeyboardButton('NI')
            e = types.KeyboardButton('VIRT')
            f = types.KeyboardButton('RES')
            g = types.KeyboardButton('SHR')
            h = types.KeyboardButton('S')
            i = types.KeyboardButton('%CPU')
            j = types.KeyboardButton('%MEM')
            k = types.KeyboardButton('TIME+')
            l = types.KeyboardButton('COMMAND')

            back3 = types.KeyboardButton('Вернуться к выбору рабочей зоны')
            markup.add(a, b, m, d, e, f, g, h, i, j, k, l, back3)
            bot.send_message(message.chat.id, 'Выберите столбец заново', reply_markup=markup)

        elif message.text == 'Что такое утилита top':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'top – одна из наиболее распространённых и удобных в своей линейке утилит, предназначенная для мониторинга состояния сервера. Программа top динамически выводит в режиме реального времени информации о работающей системе, т.е. о фактической активности процессов. По умолчанию она выдает задачи, наиболее загружающие процессор сервера, и обновляет список каждые две секунды.', reply_markup=markup)

        elif message.text == 'Сортировка списка процессов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            a = types.KeyboardButton('сортировка по памяти')
            b = types.KeyboardButton('сортировка по использованию CPU')
            c = types.KeyboardButton('сортировка по идентификатору процесса')
            d = types.KeyboardButton('сортировка по времени работы')
            back = types.KeyboardButton('Назад')
            markup.add(a, b, c,d,  back)
            bot.send_message(message.chat.id, 'Одной из наиболее частых причин использования такого инструмента top является выяснение того, какой процесс потребляет большинство ресурсов. Вы можете нажать следующие клавиши, чтобы отсортировать список:', reply_markup=markup)
            bot.send_message(message.chat.id, 'Нажмите как вы хотите отсортировать процесс и бот выдаст вам клавишу, которую надо нажать', reply_markup=markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Что такое утилита top')
            item5 = types.KeyboardButton('Запуск команды top')
            item2 = types.KeyboardButton('Интерфейс')
            item3 = types.KeyboardButton('Сортировка списка процессов')
            item4 = types.KeyboardButton('Вопросы из зачёта о команде top и ответы на них')
            markup.add(item1, item5, item2, item3, item4)
            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)
        elif message.text == 'сортировка по памяти':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back2 = types.KeyboardButton('Заново выбрать, как хотите отсортировать')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back2,final)
            bot.send_message(message.chat.id, 'для этого нажмите клавишу "M"', reply_markup=markup)
        elif message.text == 'сортировка по использованию CPU':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back2 = types.KeyboardButton('Заново выбрать, как хотите отсортировать')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back2,final)
            bot.send_message(message.chat.id, 'для этого нажмите клавишу "P"', reply_markup=markup)
        elif message.text == 'сортировка по идентификатору процесса':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back2 = types.KeyboardButton('Заново выбрать, как хотите отсортировать')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back2,final)
            bot.send_message(message.chat.id, 'для этого нажмите клавишу "N"', reply_markup=markup)
        elif message.text == 'сортировка по времени работы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back2 = types.KeyboardButton('Заново выбрать, как хотите отсортировать')
            final = types.KeyboardButton('Вернуться к началу')
            markup.add(back2,final)
            bot.send_message(message.chat.id, 'для этого нажмите клавишу "N"', reply_markup=markup)
        elif message.text == 'Заново выбрать, как хотите отсортировать':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('сортировка по памяти')
            item2 = types.KeyboardButton('сортировка по использованию CPU')
            item3 = types.KeyboardButton('сортировка по идентификатору процесса')
            item4 = types.KeyboardButton('сортировка по времени работы')
            back5 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back5)
            bot.send_message(message.chat.id, 'Выберите заново, как хотите отсортировать', reply_markup=markup)
        elif message.text == 'Запуск команды top':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(message.chat.id,'Утилита не всегда установлена по умолчанию, для её установки в Ubuntu используйте команду: sudo apt install top',reply_markup=markup)
            file = open('./sudo.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.chat.id,
                             'Затем для запуска просто выполните в терминале: top',
                             reply_markup=markup)
            file = open('./sudotop.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
        elif message.text == 'Вопросы из зачёта о команде top и ответы на них':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            f = types.KeyboardButton('Нагрузка на каждое ядро')
            item3 = types.KeyboardButton('Какой командой был запущен процесс')
            item4 = types.KeyboardButton(' Что означает каждая запись в выводе?')
            back = types.KeyboardButton('Назад')
            markup.add(f, item3, item4, back)
            bot.send_message(message.chat.id, 'Выберите вопрос', reply_markup=markup)
        elif message.text =='Нагрузка на каждое ядро':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            file = open('./cpu.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.chat.id, 'для этого найдите столбец %CPU и снизу будет написано какой командой был запущен процесс. Это можно было изучить в боте, посмотрев интерфейс данной утилиты', reply_markup=markup)
        elif message.text =='Какой командой был запущен процесс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            file = open('./command.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.chat.id, 'для этого найдите столбец COMMAND и снизу будет написано какой командой был запущен процесс. Это можно было изучить в боте, посмотрев интерфейс данной утилиты', reply_markup=markup)
        elif message.text =='Что означает каждая запись в выводе?':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, ' Для этого изучите команду интерфейс в боте!', reply_markup=markup)
        elif message.text == 'Вернуться к началу':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Что такое утилита top')
            item5 = types.KeyboardButton('Запуск комнады top')
            item2 = types.KeyboardButton('Интерфейс')
            item3 = types.KeyboardButton('Сортировка списка процессов')
            item4 = types.KeyboardButton('Вопросы из зачёта о команде top и ответы на них')
            markup.add(item1, item5, item2, item3, item4)
            bot.send_message(message.chat.id, 'Начало', reply_markup=markup)



bot.polling(none_stop=True)











