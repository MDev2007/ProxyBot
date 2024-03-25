# === [ run bot ] === #

import os,platform
from API.APIBOT import Api


# =================== #


def run_bot() :
    system = platform.system()
    # ===== #
    if system == "Windows" :
        os.system("cls")
    else :
        os.system("clear")
    # =========== #
    print("| BOT NOW ONLINE |")
    Api.infinity_polling()
    