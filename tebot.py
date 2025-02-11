from pyexpat.errors import messages

import telebot
from telebot import types
from telebot import apihelper

apihelper.API_URL = "https://tg.bimax.space/bot{0}/{1}"
bot_token = "7651357512:AAFLMYxjYuLpXDIJ05odan4dxY140NX3F8E"
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(" ایدی را وارد کنید", callback_data='button1')
    markup.add(button1)

    bot.send_message(message.chat.id, " لطفا دکمه را انتخاب کنید:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'button1':
        bot.answer_callback_query(call.id, "شما دکمه یک را انتخاب کردید. ")

        bot.send_message(call.message.chat.id, "این رباط هنوز بسیار مقدماتی است اما تا جای ممکن تلاش میکنیم به شما کمک کنیم.")

    elif call.data == 'button2':
        bot.answer_callback_query(call.id, "شما دکمه ۲ را انتخاب کردید.")

        bot.send_message(call.message.chat.id, "برای اطلاعات بیشتر راجب خودتان فقط کافیه درخواست کنی.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    user_id = message.from_user.id
    bot.reply_to(message,f"سلام {message.from_user.first_name}")
    bot.reply_to(message,f"ایدی شما  {user_id}")



bot.infinity_polling()
