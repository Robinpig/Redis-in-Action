import redis
import threading


locks=threading.local()
locks.redis={}

def key_for(user_id):
    return "account_{}".format(user_id)


