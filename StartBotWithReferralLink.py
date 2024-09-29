from telebot import TeleBot
from telebot.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo)

bot = TeleBot('7305923163:AAHu6Ka30ODUxv9IoO0hy0nnmbNnt8bs4Rs')

@bot.message_handler(commands=['start'])
def start(message: Message):
    # Parse the incoming message to extract the referral code
    if message.text.startswith('/start'):
        query_string = message.text.split(' ', 1)[-1]  # Get everything after /start
        referral_code = query_string if query_string else 'default_code'  # Use a default code if none provided

        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Hello! Welcome To My App', web_app=WebAppInfo(f'https://bot.draton.io?referral={referral_code}'))]
        ])

        bot.send_message(chat_id=message.chat.id, text='Start Game...', reply_markup=markup)

if __name__ == '__main__':
    bot.polling(skip_pending=True)
