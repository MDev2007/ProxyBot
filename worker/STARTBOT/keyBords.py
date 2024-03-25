# === ( bot start keyboards file ) === #

from telebot.types import (InlineKeyboardMarkup,InlineKeyboardButton)


startKey = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("✼ ارسال پست",callback_data="sendPost")
    ] ,
    [
        InlineKeyboardButton("✼ دریافت پروکسی ",callback_data="getProxy")
    ],
    [
        InlineKeyboardButton("✼ دریافت کانفیگ ",callback_data="getConfig")
    ] ,
    [
        InlineKeyboardButton("✼ ارسال کانفیگ",callback_data="sendConfig")
    ],
    [
        InlineKeyboardButton("✼ ارسال پروکسی ",callback_data="sendProxy")
    ],
        [
        InlineKeyboardButton("✼ مدیریت ",callback_data="management")
    ]
])
# =================== #