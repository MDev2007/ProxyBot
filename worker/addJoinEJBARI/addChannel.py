# === [ Add channel ] === #

from API.APIBOT import Api
from API.database import botData
import asyncio

# --------------- #

def add_channel(message) :
    botData.update_one({"_id":"bot"},{"$set":{"ejbariChannels":message.chat.id}}) 
    # ---------- #
    Api.delete_message(message.chat.id , message.id)
    # ============== #
    msg = Api.send_message(
        chat_id = message.chat.id ,
        text = "✅ جنل با موفقیت برای جوین اجباری تنظیم شد"
    )