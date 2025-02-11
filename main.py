import telebot
from telebot import apihelper

apihelper.API_URL = "https://tg.bimax.space/bot{0}/{1}"
bot_token = "7651357512:AAFLMYxjYuLpXDIJ05odan4dxY140NX3F8E"
chat_id = "7651357512"

bot = telebot.TeleBot(token=bot_token, parse_mode='markdown')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.from_user.id == message.from_user.id:
        bot.reply_to(f"{user_data}")

bot.infinity_polling()