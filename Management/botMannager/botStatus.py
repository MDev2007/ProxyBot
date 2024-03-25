# === [ bot status ] === #

from API.APIBOT import Api
from API.database import (users,proxis,botData)
from telebot.types import (InlineKeyboardMarkup,InlineKeyboardButton)
from . import texts


# ============= #

def get_bot_status(call) :
    proxyData = proxis.find_one({"_id":"proxy"})
    configList = [config for config in proxyData["configList"]]
    proxyList = [proxy for proxy in proxyData["proxyList"]]
    # =============== #
    botData_ = botData.find_one({"_id":"bot"})
    channelID = botData_["channel"]
    # =============== #
    botUsers = users.find()
    botUsers = [user["_id"] for user in botUsers]
    # =============== #
    Api.edit_message_text(
        text = texts.bot_status_text.format(len(botUsers),len(proxyList),len(configList),channelID) ,
        chat_id = call.message.chat.id , 
        message_id = call.message.id ,
        reply_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("◄ برگشت",callback_data = "management")
            ]
        ])
    )


