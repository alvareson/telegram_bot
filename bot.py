""""
    Working version of Telegram bot with Proxy
"""


import config
import telebot
from telebot import apihelper

apihelper.proxy = {
    'http': 'socks5://proxy_active_ip_address_with_port',
    'https': 'socks5://proxy_active_ip_address_with_port',
}

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def main(message):
    bot.send_message(message.chat.id, "Привет это тестовый ответ")

if __name__ == "__main__":
    bot.polling(none_stop=True)
