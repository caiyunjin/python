#装饰器 创建一个闭包函数，在调用闭包函数内调用目标函数，可以达到不改动目标函数的同时增加额外的功能
def outer(func):
    def inner():
        print('睡觉了')
        func()
        print('起床了')

    return inner


@outer
def sleep():
    import random
    import time

    print('睡眠中...')
    time.sleep(random.randint(1, 5))


sleep()
