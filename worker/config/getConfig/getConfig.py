# === [ Get config file ] === #

from API.APIBOT import Api
from API.database import proxis
from . import texts
from telebot.types import (InlineKeyboardButton,InlineKeyboardMarkup)
import random

# =================== #

def get_config(call) :
    configData = proxis.find_one({"_id":"proxy"})
    configList = [f"<code>{config}</code>" for config in configData["configList"]]

    # ========================= #
    if len(configList) != 0 :
        configList_ = []
        for i in range(random.randint(2,4)) :
            config = random.choice(configList)
            if config not in configList_ :
                configList_.append(config)
            else : pass
        Api.edit_message_text(
            text = texts.config_text.format("\n------------\n".join(configList_)) ,
            chat_id = call.message.chat.id ,
            message_id = call.message.id ,
            reply_markup = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("🔄 تازه سازی ",callback_data="getConfig")
                ],
                [
                    InlineKeyboardButton("◄ برگشت",callback_data="back2start")
                ]
            ])
        )
    else :
        Api.answer_callback_query(call.id , "کانفیگی ثبت نشده !")
