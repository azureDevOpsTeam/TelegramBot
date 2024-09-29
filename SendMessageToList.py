import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# توکن ربات
bot_token = 'your_bot_token'  # توکن ربات تلگرام شما
bot = telebot.TeleBot(bot_token)

# لیستی از شناسه‌های کاربران
chat_ids = [123456789, 987654321, 1122334455]  # لیست آیدی کاربران

# متد برای ارسال پیام با دکمه شیشه‌ای
def send_message_with_button_to_list(chat_ids):
    message_text = "سلام! روی دکمه زیر کلیک کنید."

    # ایجاد دکمه شیشه‌ای
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("بازدید وب‌سایت", url="https://yourwebsite.com")
    markup.add(button)

    # ارسال پیام برای هر آیدی در لیست
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id, message_text, reply_markup=markup)
            print(f"پیام با موفقیت به {chat_id} ارسال شد.")
        except Exception as e:
            print(f"خطا در ارسال پیام به {chat_id}: {e}")

if __name__ == '__main__':
    send_message_with_button_to_list(chat_ids)
