import time
import threading


def f0():
    pass


def f1(a1, a2):
    time.sleep(5)
    f0()


'''下面代码是直接运行下去的，不会等待函数里面设定的sleep'''
t = threading.Thread(target=f1, args=(111, 112))  # 创建线程
t.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
t.start()  # 开启线程

t = threading.Thread(target=f1, args=(111, 112))
t.start()

t = threading.Thread(target=f1, args=(111, 112))
t.start()
# 默认情况下程序会等线程全部执行完毕才停止的，不过可以设置更改为后台线程，使主线程不等待子线程，主线程结束则全部结束