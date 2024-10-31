import telebot
import random
from telebot import types
from habit import WaterHabit

# Создаем экземпляр бота
bot = telebot.TeleBot('8190594044:AAElwSVlkg12C-Erw3hwdaPu7fcgDyEC-J4')

# Список для хранения привычек
habits = []

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем 4 кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Создание привычки")
        item2=types.KeyboardButton("Список привычек")
        item3=types.KeyboardButton("Удаление привычки")
        item4=types.KeyboardButton("Выполнение привычки")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(m.chat.id, 'Нажми:' 
                         '\nСоздание привычки - для создания новой привычки'
                         '\nСписок привычек - для просмотра существующих привычек' 
                         '\nУдаление привычки - для удаления ненужной привычки'
                         '\nВыполнение привычки - для успешного выполнения той или иной привычки',  
                         reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, создаем новую привычку
    if message.text.strip() == 'Создание привычки' :
            bot.send_message(message.chat.id, 'Здесь будет создание привычки')
    # Если юзер прислал 2, выдаем список привычек
    elif message.text.strip() == 'Список привычек':
            bot.send_message(message.chat.id, 'Здесь будет список привычек')
    elif message.text.strip() == 'Удаление привычки':
            bot.send_message(message.chat.id, 'Будем удалять привычку')
    elif message.text.strip() == 'Выполнение привычки':
            bot.send_message(message.chat.id, 'Здесь будем выполнять действие по привычке')
    # # Отсылаем юзеру сообщение в его чат
    # bot.send_message(message.chat.id, answer)

# Запускаем бота
bot.polling(none_stop=True, interval=0)