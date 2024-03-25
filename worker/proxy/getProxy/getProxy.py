# === [ Get proxy  ] === #

from API.APIBOT import Api
from API.database import proxis
import requests,json,random
from . import texts
from telebot.types import (InlineKeyboardMarkup,InlineKeyboardButton)

# ====================== #

def get_proxy(call) :
    response = requests.get("http://api.codebazan.ir/mtproto/json/")
    data = json.loads(response.text)
    proxyData = proxis.find_one({"_id":"proxy"})
    added_proxes = [proxy for proxy in proxyData["proxyList"]]
    for i in data['Result']:
        secret = i['secret']
        server = i['server']
        port = i['port']
        proxy = f"https://t.me/proxy?server={server}&port={port}&secret={secret}"
        added_proxes.append(proxy)
    # ======================== #
    keyboards = [[InlineKeyboardButton("◄ اتصال",url=f"{random.choice(added_proxes)}")] for i in range(random.randint(5,10))]
    # =============== #
    keyboards.append([InlineKeyboardButton("🔄 تازه سازی ",callback_data="getProxy")])
    keyboards.append([InlineKeyboardButton("◄ برگشت",callback_data="back2start")])
    # -------------------- #
    Api.edit_message_text(
        text = texts.proxy_text ,
        chat_id = call.message.chat.id ,
        message_id = call.message.id ,
        reply_markup = InlineKeyboardMarkup(keyboards)
    )