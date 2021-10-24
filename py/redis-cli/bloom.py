import init


def __bloom():
    client = init.__get_client()
    for i in range(100000):
        client.execute_command("bf.add", "codeBloom", "user%d" % i)
        ret = client.execute_command("bf.exists", "codeBloom", "user%d" % i)
        if ret == 0:
            print(i)
            break

if __name__ == '__main__':
    __bloom()