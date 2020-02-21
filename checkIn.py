# 针对机器人签到群组实现自动化
from GetSetMessages import *
from time import sleep


def check():
    url = "https://t.me/"
    text = "abracadabra"
    send(url, text)
    sleep(1)
    receive(url, 10)




if __name__ == '__main__':
    check()
