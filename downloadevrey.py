#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@onlyibrahim
# Coded by Ibrahima
# ---------------------

#lib

import os,io,re



try:
    import telebot
    from telebot import types
except ImportError:
    os.system('pip install pytelegrambotapi')
    os.system('pip install telebot')
try:
    from TikTok import TikTok_dl as TK
except ImportError:
    os.system('pip install TikTok-dl')
try:
    import requests
except ImportError:
    os.system('pip install requests')
#vars

os.system('clear')

token = input("5872831544:AAFLrtuOSBtCKMb6Teno1wguBBeLLau9Yas")

chatid = ''

text = ''

messageid = ''

vd_status = ""

wm_status = ""

ad_status = ""

bot = telebot.TeleBot(token)


#func
@bot.message_handler(commands='start')
def start(message):

    bot.send_message(message.chat.id,'مرحبا بك في بوت تحميل من التيك توك ارسل رابط الفيديو للتحميل')

@bot.message_handler(func=(lambda message:True))
def dow(message):

    if message.text:
        try:
            global text,chatid,messageid,vd_status,wm_status,ad_status

            if re.search(r'https://vm.tiktok.com/(.*?)/?k=1',message.text) or re.search(r'',message.text):
                text = message.text

                chatid = message.chat.id

                messageid = message.message_id

                vd_status = 'تحميل باعلئ دقه'

                wm_status = 'تحميل بعلامه مائيه'

                ad_status = 'تحميل كملف صوتي'

                img = io.BytesIO(requests.get(TK(message.text).image).content)

                keyboar = [
                    [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                    [types.InlineKeyboardButton(ad_status,callback_data='ad')]
                ]

                mark = types.InlineKeyboardMarkup(keyboard=keyboar)
                
                bot.send_photo(chatid,img,reply_markup=mark)
        except:pass
@bot.callback_query_handler(func=(lambda call:True))
def call(call):
    global ad_status,vd_status,wm_status
    if call.data == 'vd':
        try:

            bot.send_video(chatid,TK(text).nowatermark)
            
            vd_status = "تم التحميل"

            keyboar = [
                [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                
                [types.InlineKeyboardButton(ad_status,callback_data='ad')]
            ]
            
            mark = types.InlineKeyboardMarkup(keyboard=keyboar)

            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=mark)
        except:pass
    if call.data == 'ad':
        try:
            bot.send_audio(chatid,TK(text).audio)

            ad_status = "تم التحميل"

            keyboar = [
                [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                
                [types.InlineKeyboardButton(ad_status,callback_data='ad')]
            ]

            mark = types.InlineKeyboardMarkup(keyboard=keyboar)

            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=mark)
        except:pass
    if call.data == 'wm':
        try:
            bot.send_video(chatid,TK(text).watermark)

            wm_status = "تم التحميل"

            keyboar = [
                [types.InlineKeyboardButton(vd_status,callback_data='vd'),types.InlineKeyboardButton(wm_status,callback_data='wm')],
                
                [types.InlineKeyboardButton(ad_status,callback_data='ad')]
            ]

            mark = types.InlineKeyboardMarkup(keyboard=keyboar)

            bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=mark)
        except:pass
bot.infinity_polling()
