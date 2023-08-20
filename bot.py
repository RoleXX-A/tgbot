import telebot

from random import choice

SECRET_KEY = ""

bot = telebot.TeleBot(SECRET_KEY)


@bot.message_handler(commands=['start'])
def start(message):
  keyboard = telebot.types.ReplyKeyboardMarkup()
  red_button = telebot.types.KeyboardButton('🟥')
  black_button = telebot.types.KeyboardButton('⬛️')

  keyboard.row(red_button)
  keyboard.row(black_button)

  bot.send_message(message.chat.id,
                   "Угадай цвет масти карты: 🟥 или ⬛️",
                   reply_markup=keyboard)
  bot.register_next_step_handler(message, answer_card)


def answer_card(message):
  suit, number = generate_random_card()
  random_card = number + ' ' + suit

  if message.text == '🟥' and suit in ["Ч", "Б"]:
    bot.send_message(message.chat.id,
                     "Ответ верный! Выбранная карта: " + random_card)

  elif message.text == '⬛️' and suit in ["Т", "П"]:
    bot.send_message(message.chat.id,
                     "Ответ верный! Выбранная карта: " + random_card)

  else:
    bot.send_message(message.chat.id,
                     "Неверный ответ! Выбранная карта: " + random_card)

  start(message)


def generate_random_card():
  card_number = [
      "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
  ]
  card_suit = ["Ч", "Б", "Т", "П"]

  random_card_suit = choice(card_suit)
  random_card_number = choice(card_number)

  return random_card_suit, random_card_number


bot.infinity_polling()
