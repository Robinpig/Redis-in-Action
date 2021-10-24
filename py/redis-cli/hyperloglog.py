import init

def __hyper():
    client = init.__get_client()
    for i in range(100000):
        client.pfadd("codehole", "user%d" % i)
    print(100000, client.pfcount("codehole"))


if __name__ == '__main__':
    __hyper()
