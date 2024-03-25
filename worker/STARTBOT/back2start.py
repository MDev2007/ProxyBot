# === [ Back2 start ] === #

from API.APIBOT import Api
from API.database import users
from . import texts
from . import keyBords

# ================= #

def back_start(call) : 
    Api.edit_message_text(
        text = texts.startText.format(call.from_user.first_name) ,
        chat_id = call.message.chat.id ,
        message_id = call.message.id ,
        reply_markup = keyBords.startKey ,
    )