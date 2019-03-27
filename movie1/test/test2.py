import threading
import time


def do(event):
    print('start')
    event.wait()  # 红灯，所有线程执行都这里都在等待
    print('end')


event_obj = threading.Event()  # 创建一个事件
for i in range(10):  # 创建10个线程
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

time.sleep(5)

event_obj.clear()  # 让灯变红，默认也是红的，阻塞所有线程运行
data = input('请输入要：')
if data == 'True':
    event_obj.set()  # 变绿灯