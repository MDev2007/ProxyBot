# === [ admin page keyboards ] === #

from telebot.types import (InlineKeyboardMarkup,InlineKeyboardButton)

# -------------------------------- #

keyBoard_1 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("مدیریت ربات",callback_data="bot_page")
    ],
    [
        InlineKeyboardButton("مدیریت کانال",callback_data="channel_page")
    ] ,
    [
        InlineKeyboardButton("◄ برگشت",callback_data="back2start")
    ]
])