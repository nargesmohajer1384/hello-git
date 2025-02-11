import requests
import telebot
from telebot import apihelper

apihelper.API_URL = "https://tg.bimax.space/bot{0}/{1}"
bot_token = "7651357512:AAFLMYxjYuLpXDIJ05odan4dxY140NX3F8E"

bot = telebot.TeleBot(token=bot_token, parse_mode='markdown')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "لطفاً آیدی کاربر را وارد کنید:")
    bot.register_next_step_handler(message, get_user_info)


def get_user_info(message):
    user_id = message.text
    url = f"https://api.maxpool.site/wallet"

    try:
        response = requests.get(f"{url}/{user_id}/", headers={
            "x-service-key": "xgDJ-wj5iSebCCtKUQdiRkUb5Jy5qpyTZ_DWs5Z9Vuzgwn-QyAVhaJxmYeXig5-DF"})
        response.raise_for_status()
        user_data = response.json()

        bot.reply_to(message, f"اطلاعات کیف پول: {user_data['message']}")
        print(f"Total wallet info: {user_data}")

    except requests.exceptions.HTTPError as err:
        bot.reply_to(message, f"خطا در درخواست: {err}")
    except Exception as e:
        bot.reply_to(message, f"یک خطا رخ داد: {e}")

if __name__ == "__main__":
    bot.infinity_polling()
