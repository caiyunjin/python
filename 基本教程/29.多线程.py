import time
import threading


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 创建一个唱歌线程
    sing_thread = threading.Thread(target=sing, args=('我要唱歌',))
    # 创建一个跳舞线程
    dance_thread = threading.Thread(target=dance, kwargs={'msg': '我在跳舞'})
    # 启动唱歌线程
    sing_thread.start()
    # 启动跳舞线程
    dance_thread.start()
