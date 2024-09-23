import telebot
from bs4 import BeautifulSoup
import requests

# Токен бота, полученный от BotFather
TOKEN = 'токен'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = f"Приветствую Вас, {message.from_user.first_name}! Я могу пробить данные по кадастровому " \
                      f"номеру. Нажмите кнопку ниже, чтобы начать.\n\nP.S Я беру данные, которые нахожу в сети! 😉 "
    markup = telebot.types.InlineKeyboardMarkup()
    button_start = telebot.types.InlineKeyboardButton("🟡Начать", callback_data='start')
    markup.add(button_start)
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'start')
def handle_start(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, "🤖: Пожалуйста, введите кадастровый номер!")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.startswith(' ') or not message.text.replace('-', '').replace(':', '').isdigit():
        bot.reply_to(message, "⚠️ Введите корректный кадастровый номер (например, 69:45:0080243:2).")
        return

    kad_number = message.text.strip().replace(':', '-')

    url = f"https://nca.by/services/resources-services/publichnaya-kadastrovaya-karta/{kad_number}"

    try:

        response = requests.get(url)

        if response.status_code == 200:

            property_info = parse_property_info(response.content)

            if property_info:
                bot.reply_to(message, format_property_info(property_info), parse_mode='HTML')
            else:
                bot.reply_to(message, "⚠️ Не удалось найти информацию о недвижимости.")
        else:
            bot.reply_to(message, "⚠️ Не удалось получить доступ к информации о недвижимости.")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Произошла ошибка: {str(e)}")

    markup = telebot.types.InlineKeyboardMarkup()
    button_developer = telebot.types.InlineKeyboardButton("Разработчик бота", url="https://t.me/pizzaway")
    markup.add(button_developer)
    bot.send_message(message.chat.id, "👨‍💻 Связаться с разработчиком", reply_markup=markup)


def parse_property_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    property_info = {}
    property_sections = soup.find_all('div', class_='object__table-tr')
    for section in property_sections:
        key_element = section.find('div', class_='object__table-td')
        value_element = section.find('div', class_='object__table-td').find_next('div')
        if key_element and value_element:
            key = key_element.text.strip()
            value = value_element.text.strip()
            property_info[key] = value
    return property_info


def format_property_info(property_info):
    formatted_info = "<b>Сведения по объекту:</b>\n\n"
    for key, value in property_info.items():
        if key != 'Арест и ограничения:' and key != 'Наличие залога в банке:' and key != 'Особые отметки:':
            formatted_info += f"<b>{key}:</b> {value}\n\n"
    return formatted_info


bot.polling()
