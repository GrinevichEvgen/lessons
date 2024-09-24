# 🔣 Телеграм бот с двумя страницами

# 🔧 Технологии:
# - 💻 Python

# 💻 Пример использования: Бот имеет две страницы, которые можно переключать с помощью кнопок на клавиатуре. Вы
# можете указать нужную информацию там, например ссылку на свой канал.
import telebot
from telebot import types

# Указываем токен бота
TOKEN = "YOUR_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Информация')
    markup.add(itembtn1)

    bot.send_message(message.chat.id, "Привет! Я бот с двумя страницами. Выбери, что тебе интересно:",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_info(message):
    if message.text == 'Информация':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('Назад')
        markup.add(itembtn1)

        bot.send_message(message.chat.id, "Это пример текста со страницы информации.", reply_markup=markup)

    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('Информация')
        markup.add(itembtn1)

        bot.send_message(message.chat.id, "Возвращаемся на главную страницу.", reply_markup=markup)


# Запуск бота
bot.polling()
