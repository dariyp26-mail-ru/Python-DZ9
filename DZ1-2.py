# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9
# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import random

global num
global count
count = 0
num = random.randint(1, 1000)

bot = telebot.TeleBot("5888185813:AAGLttnlk6bQYwGDbj2EfBBy4FrZrerj2U4")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет!")


@bot.message_handler(content_types=['text'])
def hello_user(message):

    def Calc(message):
        if '+' in message.text or '*' in message.text or '/' in message.text or '-' in message.text:
            do = str(eval(str(message.text)))
            bot.send_message(message.chat.id, f'{do}')
        else:
            bot.send_message(message.chat.id, 'Некорректный ввод')

    def Game(message):
        global num
        global count
        count += 1
        if int(message.text) > num:
            a = bot.send_message(message.chat.id, "Число должно быть меньше!")
            bot.register_next_step_handler(a, Game)
        elif int(message.text) < num:
            b = bot.send_message(message.chat.id, "Число должно быть больше!")
            bot.register_next_step_handler(b, Game)
        else:
            bot.send_message(
                message.chat.id, f"Вы угадали, это число = {num}, количество попыток {count}")

    if 'привет' in message.text.lower():
        bot.reply_to(message, "Hi, " + message.from_user.first_name)
    elif message.text.lower() == 'посчитай':
        r = bot.send_message(message.chat.id, 'Что будем считать?')
        bot.register_next_step_handler(r, Calc)
    elif message.text.lower() == 'играть':
        r = bot.send_message(
            message.chat.id, 'Я загадал число от 1 до 1000, угадывай')
        bot.register_next_step_handler(r, Game)


bot.infinity_polling()
