# === [ send post ] === #

# ||||||||||||||||||||| #

from API.APIBOT import Api
from API.database import botData
from . import texts
from telebot.types import (InlineKeyboardButton,InlineKeyboardMarkup)

def send_post(call) :
    data = botData.find_one({"_id":"bot"})
    channel = data["channel"]
    # =================== #
    if channel == None :
        Api.answer_callback_query(call.id , "❗️ چنلی برای این ربات تنظیم نشده است .",show_alert=True)
    else :
        keyboards = [[InlineKeyboardButton(f'{Api.get_chat(channel).title}',callback_data=f"channel{channel}")]]
        keyboards.append([InlineKeyboardButton("◄ برگشت",callback_data="back2start")])
        # ==================== #
        Api.edit_message_text(
            text = texts.step_1_text ,
            chat_id = call.message.chat.id ,
            message_id = call.message.id ,
            reply_markup = InlineKeyboardMarkup(keyboards)
        )
