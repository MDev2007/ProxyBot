# === [ sendProxy file ] === #

from API.APIBOT import Api
from API.database import proxis
from . import texts
from telebot.types import (InlineKeyboardButton,InlineKeyboardMarkup)


# ==================== #


def save_config(call) :
    Api.edit_message_text(
        text = texts.save_config_text ,
        chat_id = call.message.chat.id ,
        message_id = call.message.id 
    )
    Api.register_next_step_handler(call.message,get_config)

def get_config(message) :
    if message.text != "/cancel" :
        config_ = str(message.text).split()
        data = proxis.find_one({"_id":"proxy"})
        configList = [config for config in data["configList"]]
        # ====================== #
        configList_ = [config for config in config_ if config.startswith("vless") or config.startswith("vmess") and config not in configList]

        if len(configList_) != 0:
            # ||||||||||||||||||||||||| #
            finally_ = []
            for config_ in configList :
                finally_.append(config_)
            "end 1"
            for config_ in configList_ :
                finally_.append(config_)
            "end 2"
            proxis.update_one({"_id":"proxy"},{"$set":{"configList":finally_}})
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
            Api.send_message(chat_id = message.chat.id , text = "❗️ کانفیگ ارسالی شما نامعتبر است یا از قبل در لیست موجود هست \n لطفا کانفیگ معتبر یا جدیدی ارسال کنید :\n\n/cancel")
            Api.register_next_step_handler(message,get_config)
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