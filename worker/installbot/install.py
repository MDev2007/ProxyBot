# === [ install bot ] === #

from API.APIBOT import Api
from API.database import botData,channels
from . import texts

# ================ #

def install_bot(message) :
    # =============== #
    data = botData.find_one({"_id":"bot"})
    # --------------- #
    if data["channel"] == None :
        botData.update_one({"_id":"bot"},{"$set":{"channel":message.chat.id}})
    
    else : 
        Api.send_message(
            chat_id = message.chat.id ,
            text = f"❗️ چنلی از قبل نصب  شده است ."
        )