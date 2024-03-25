# === [ Database File ] === #

# ||||||||||||||||||||| #

from pymongo import MongoClient
# ----------- #
from dotenv import load_dotenv
# ----------- #
import os
# ----------- #
load_dotenv()
# ||||||||||||||||||||| #

client = MongoClient(os.getenv("db_url"))
dataBase = client["Pyro1"]
# ===================== #
users = dataBase["USERS"]
Modes = dataBase["MoDES"] 
admins = dataBase["ADMINS"]
proxis = dataBase["PROXIS"]
botData = dataBase["BotData"]
channels = dataBase["CHANNELS"]
# ||||||||||||||||||||||| #


data = {
    "_id" : "proxy" ,
    "proxyList" : [] ,
    "configList" : []
}

try : proxis.insert_one(data)
except : pass
owner_id = int(os.getenv("adminId"))
# ============= #
bot_Data = {
    "_id" : "bot" ,
    "owner" : owner_id ,
    "admins" : [] ,
    "channel" : None,
    "ejbariChannels" : None
}
try : botData.insert_one(bot_Data)
except : pass