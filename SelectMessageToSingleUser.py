import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توکن ربات و آیدی چت
bot_token = '7305923163:AAHu6Ka30ODUxv9IoO0hy0nnmbNnt8bs4Rs'  # توکن ربات خود را وارد کنید
chat_id = 5933914644  # آیدی چت کاربر را وارد کنید

bot = telebot.TeleBot(bot_token)

# متد برای ارسال پیام با دکمه شیشه‌ای
def send_message_with_button():
    message_text = "سلام! روی دکمه زیر کلیک کنید."

    # ایجاد دکمه شیشه‌ای
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("بازدید وب‌سایت", url="https://yourwebsite.com")
    button2 = InlineKeyboardButton("بازدید وب‌سایت", url="https://yourwebsite.com")
    markup.add(button1)
    markup.add(button2)
    # ارسال پیام با دکمه شیشه‌ای
    bot.send_message(chat_id, message_text, reply_markup=markup)

if __name__ == '__main__':
    send_message_with_button()
    print("پیام ارسال شد.")
