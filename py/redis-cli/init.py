from redis import StrictRedis

def __get_client():
    return StrictRedis("47.97.123.133", 6379, 0)