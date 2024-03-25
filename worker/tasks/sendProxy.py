# === [ proxy task ] === #

from API.database import proxis,botData
from API.APIBOT import Api
import requests,json,random
from . import texts

# "'''''''''''''''''''''''''" #

def send_proxy_channel() :
    data = botData.find_one({"_id":"bot"})
    channel = data["channel"] 
    if channel != None :
        # ============ [ proxies ] ========== #
        response = requests.get("http://api.codebazan.ir/mtproto/json/")
        data = json.loads(response.text)
        proxyData = proxis.find_one({"_id":"proxy"})
        added_proxes = [f"<a href='{proxy}'>اتصال</a>" for proxy in proxyData["proxyList"]]
        for i in data['Result']:
            secret = i['secret']
            server = i['server']
            port = i['port']
            proxy = f"<a href='https://t.me/proxy?server={server}&port={port}&secret={secret}'>اتصال</a>"
            added_proxes.append(proxy)
        # ================ #
        selected_proxies = [random.choice(added_proxes) for i in range(random.randint(3,10))]
        # ------------------- #
        bot = Api.get_me()
        bot_username = bot.username
        Api.send_message(
            chat_id = channel ,
            text = texts.proxy_text.format(" |".join(selected_proxies),bot_username)
            )
    else :
        pass
    
