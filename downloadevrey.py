import telebot
import requests
from telebot import types

token = "6707171521:AAExFoeQEI2K4bc3IKZnX_JmCCBhdE350OQ"#token
bot = telebot.TeleBot(token)
channel= types.InlineKeyboardButton(text='قناتي', url = "https://t.me/SuPeRx1")
@bot.message_handler(commands=["start"])
def start(message):
	b = types.InlineKeyboardMarkup()
	b.add(channel)
	bot.reply_to(message,'اهلن بك في بوت تحميل صوت فيديو اليويتوب\n- ارسل الرابط Now\n[by](t.me/BRoK8)',disable_web_page_preview="true",parse_mode="markdown",reply_markup=b)

@bot.message_handler(func=lambda m:True)
def Url(message):
	try:
		msg = message.text
		req = requests.get(f'https://el-sherif.shop/Mahmoud/api/down.php?url={msg}').json()
		ti = req['title']
		im = req['img']
		u = req['url']
		tii = req['duration']
		bot.send_photo(message.chat.id,im, caption=f"{tii}")
		bot.send_voice(message.chat.id,u, caption=f"{ti}")
	except:bot.reply_to(message,'error')
	pass
print('run')
bot.infinity_polling()
