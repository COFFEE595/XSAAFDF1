import requests
import telebot

def get(url):
    response = requests.get(url)
    return response.json()

def handle_message_text(text, chat_id):
    if text:
        api_data = get("https://hmsbots.aba.vg/api/Pintrest.php?url=" + text)
        if "UrlVideo" in api_data:
            bot_instance.send_video(chat_id, api_data["UrlVideo"])
        elif "UrlPhoto" in api_data:
            bot_instance.send_photo(chat_id, api_data["UrlPhoto"])

# يفترض أنك قد قمت بتهيئة كائن البوت بالفعل
# يمكنك استخدام الكائن الموجود في السياق الخاص بك
# والذي يبدو من رمز البوت الذي قمت بمشاركته في الكود الأول
# قمت بتغيير اسم الكائن في الشفرة الأساسية من "bot" إلى "bot_instance" لتوضيح الأمر
# ولكن قم بتغييره إلى اسم الكائن الفعلي للبوت الخاص بك
bot_instance = telebot.TeleBot("7069552302:AAHSdIuEa0sD0QLZ5IfumNnWPv5hxTXp_Qg")

@bot_instance.message_handler(func=lambda message: True)
def handle_message(message):
    handle_message_text(message.text, message.chat.id)

# بدء الاستماع للرسائل
bot_instance.polling()
