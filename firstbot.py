import requests
import telebot
from telebot import apihelper 

apihelper.API_URL = "https://tg.bimax.space/bot{0}/{1}"
bot_token = "7651357512:AAFLMYxjYuLpXDIJ05odan4dxY140NX3F8E"

bot = telebot.TeleBot(token=bot_token, parse_mode='markdown')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"ایدی را وارد کنید")
    #bot.reply_to(f"{user_data},{text:str}")

def get_user_info(user_id):
    url = f"https://api.maxpool.site/wallet"

    try:
        response = requests.get(f"{url}/{user_id}/", headers={
            "x-service-key": "xgDJ-wj5iSebCCtKUQdiRkUb5Jy5qpyTZ_DWs5Z9Vuzgwn-QyAVhaJxmYeXig5-DF"})
        response.raise_for_status()
        user_data = response.json()

        # print((f"{user_data}"))
        print ( "Total wallet info.",user_data['message'])


    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    bot.infinity_polling()