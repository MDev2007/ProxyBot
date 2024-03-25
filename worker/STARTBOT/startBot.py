# === ( bot start file ) === #

from API.APIBOT import Api
from API.database import users,botData
from . import texts
from . import keyBords
from telebot.types import (InlineKeyboardMarkup,InlineKeyboardButton)

# ================= #

def startBot(message) : 
    data = botData.find_one({"_id":"bot"})
    # =============== #
    if data["ejbariChannels"] != None :
        user = Api.get_chat_member(data["ejbariChannels"],message.from_user.id) 
        if user.status != "left" :
            try :
                data = {
                    "_id" : message.from_user.id ,
                    "firstName" : message.from_user.first_name ,
                    "step" : ""
                }
                users.insert_one(data)
            except :
                pass
            # ================= #

            Api.send_message(
                chat_id = message.chat.id ,
                text = texts.startText.format(message.from_user.first_name) ,
                reply_markup = keyBords.startKey ,
                reply_to_message_id = message.id
            )
        else :
            bot = Api.get_me()
            Api.send_message(
                chat_id = message.chat.id ,
                text = "❗️ برای استفاده از ربات داخل چنل زیر جوین شوید ",
                reply_markup = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(f"{Api.get_chat(data['ejbariChannels']).title}",url=f"{Api.get_chat(data['ejbariChannels']).invite_link}")
                    ],
                    [
                        InlineKeyboardButton("start",url=f"https://t.me/{bot.username}?start=joined")
                    ]
                ])
            )
    else :
        try :
            data = {
                "_id" : message.from_user.id ,
                "firstName" : message.from_user.first_name ,
                "step" : ""
            }
            users.insert_one(data)
        except :
            pass
        # ================= #

        Api.send_message(
            chat_id = message.chat.id ,
            text = texts.startText.format(message.from_user.first_name) ,
            reply_markup = keyBords.startKey ,
            reply_to_message_id = message.id
        )