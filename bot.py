import telebot

BOT_TOKEN = 8141642032:AAHvQtW0jk5atQWAy_m_YP6oA0oIZTyAu8c

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Saya adalah bot Telegram pertamamu 🎉")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Kamu bilang: {message.text}")

bot.polling()
