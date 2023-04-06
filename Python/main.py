from Settings       import TOKEN
from UserOperation  import *
from User           import User
import telebot
import sys

# Кодировка UTF-8
sys.stdout.reconfigure(encoding='utf-8')

bot = telebot.TeleBot(TOKEN)
database = Users()

@bot.message_handler(commands=['start'])
def send_sticker(message):

    # Image send
    with open("Image/hello.webp", "rb") as file:
        bot.send_sticker(message.chat.id, file)

    database.add(User(message.chat.id, message.from_user.first_name))

    bot.send_message(message.chat.id, "Добро пожаловать! Напишите ваш класс")
    bot.register_next_step_handler(message, ask_class)


# class number
def ask_class(message):
    try:
        ClassNumber = int(message.text)
        bot.send_message(message.chat.id, f"Вы учитесь в {ClassNumber} классе.")
    except ValueError:
        bot.send_message(message.chat.id, "Увы, но вы написали его некореткно. Сейчас стоит класс: 1, но в настройках его можно изменить😭")
    

@bot.message_handler(commands=['info'])
def message_info(message):
    database.print()
    bot.send_message(message.chat.id, "Загруженно")

@bot.message_handler(content_types=['text'])
def printConsole(message):
    print(str(message.chat.id) + ": " + message.text)

if __name__ == '__main__':
    bot.infinity_polling()