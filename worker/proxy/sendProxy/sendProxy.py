# === [ sendProxy file ] === #

from API.APIBOT import Api
from API.database import proxis
from . import texts
from telebot.types import (InlineKeyboardButton,InlineKeyboardMarkup)


# ==================== #


def save_proxy(call) :
    Api.edit_message_text(
        text = texts.save_proxy_text ,
        chat_id = call.message.chat.id ,
        message_id = call.message.id 
    )
    Api.register_next_step_handler(call.message,get_proxy)

def get_proxy(message) :
    if message.text != "/cancel" :
        proxis_ = str(message.text).split()


        data = proxis.find_one({"_id":"proxy"})


        proxyList = [proxys for proxys in data["proxyList"]]


        proxy = [proxy for proxy in proxis_ if proxy.startswith("http") and "server" in proxy and "secret" in proxy and "port" in proxy and "proxy" in proxy and proxy not in proxyList]
        if len(proxy) != 0 :
             # ||||||||||||||||||||||||| #
            finally_ = []
            for proxy_ in proxy :
                finally_.append(proxy_)
            "end 1"
            for proxy_ in proxyList :
                finally_.append(proxy_)
            "end 2"
            proxis.update_one({"_id":"proxy"},{"$set":{"proxyList":finally_}})
            # ==================== #
            Api.send_message(
                chat_id = message.chat.id ,
                text =  "✅ با موفقیت به لیست اضافه شد " ,
                reply_to_message_id = message.id ,
                reply_markup = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton("◄ برگشت",callback_data="back2start")
                    ]
                ])
            )
        else :
            Api.send_message(chat_id = message.chat.id , text = "❗️ پروکسی ارسالی شما نامعتبر است یا از قبل در لیست موجود هست \n لطفا پروکسی معتبر یا جدیدی ارسال کنید :\n\n/cancel")
            Api.register_next_step_handler(message,get_proxy)
    else :
        Api.send_message(
            chat_id = message.chat.id ,
            text = "عملیات لغو شد",
            reply_to_message_id = message.id ,
            reply_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("◄ برگشت",callback_data="back2start")
            ]
        ])
        )