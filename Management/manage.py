# === ( admins File ) === #

from API.APIBOT import Api
from API.database import (botData,users,proxis)
from . import texts
from . import keyboards


# ========================= #

def admin_page(call) :
    data = botData.find_one({"_id":"bot"})
    if data["channel"] != None :
        channelAdmins = [admin.user.id for admin in Api.get_chat_administrators(data["channel"])]
        if call.from_user.id in channelAdmins :
            Api.edit_message_text(
                text = "به بخش مدیریت خوش مدید :" ,
                chat_id = call.message.chat.id ,
                message_id = call.message.id ,
                reply_markup = keyboards.keyBoard_1
            )
        else :
            Api.answer_callback_query(call.id,"شما ادمین کانال نمیباشید !")
    else :
        Api.answer_callback_query(call.id , "کانالی ثبت نشده است !")
