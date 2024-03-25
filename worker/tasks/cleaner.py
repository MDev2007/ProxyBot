# === [ Cleaner file ] === #

from API.database import proxis


def clean_moades() :
    # "clean added proxies" :
    proxis.update_one({'_id':'proxy'},{"$set":{"proxyList":[]}})
    # "clean added configs" :
    proxis.update_one({"_id":"proxy"},{"$set":{"configList":[]}})
    # ================== #