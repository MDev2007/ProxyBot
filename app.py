# === [ Main File ] === #
"""==> Pyro channel management bot 
   ==> LIB : TeleBot"""
# ----------------- #

# ||||||||||||||||||||||| #

"imports file : imported all used libs in the this file"
from imports import *
"'Files' file : imported all created files in the this file"
from files import *

# ================== #

def check_time(_) :
    while True :
        time = timezone("Asia/Tehran")
        cTime = jdatetime.datetime.now(time)
        cTime = str(cTime).split()
        cTime = cTime[1]
        cTime = cTime[:8]
        # ===================== #
        if cTime == "12:00:00" or cTime == "15:00:00" or cTime == "00:00:00" :
            clean_moades()
        threading.Event().wait(1)

# ||||||||||||||||| #

def send_proxy_chanel_s(_) :
    while True :
        send_proxy_channel()
        threading.Event().wait(1800)


@Api.message_handler(chat_types=["private"],commands=["start"])
def startBOT(Message) :
    startBot(Message)


# ||||||||||||||||| #

# @Api.channel_post_handler()
# def install_Bot(Message)  :
#     if Message.text == "/install" :
#         install_bot(Message)
#     # ============= #
#     elif Message.text == "تنظیم جوین اجباری" :
#         add_channel(Message)


# ===================== #
    
@Api.callback_query_handler(func=lambda call:True)
def callback(call) :
    # ============== #
    if call.data == "sendPost" :
        send_post(call)
    # ------------ #
    elif call.data == "getProxy" :
        get_proxy(call)
    # ------------- #
    elif call.data == "sendProxy" :
        save_proxy(call)
    # ------------- #
    elif call.data == "back2start" :
        back_start(call)
    # ------------- #
    elif call.data == "getConfig" :
        get_config(call)
    # ------------- #
    elif call.data == "sendConfig" :
        save_config(call)
    # ------------- #
    elif call.data == "management" :
        admin_page(call)
    # ------------- #
    elif call.data == "bot_page" :
        get_bot_status(call)

t = threading.Thread(target=check_time,args="_")
d = threading.Thread(target=send_proxy_chanel_s,args="_")
t.start()
d.start()
run_bot()