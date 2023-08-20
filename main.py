import telebot

secret_key = '6652756332:AAFuzhaFCwTis93M6uaOtZsfj6Q1kh369_k'

bot = telebot.TeleBot(secret_key)

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Hello Player' )

bot.infinity_polling()
