# === { Bot File } === #

# ||||||||||||||||||||| #

from telebot import TeleBot
# ---------- #
from dotenv import load_dotenv
# ---------- #
import os
# ---------- #


load_dotenv()
# ---------- #

# ||||||||||||||||||||| #

Api = TeleBot(
    token = os.getenv("bot_token") ,
    parse_mode = 'html' ,
)