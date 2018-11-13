# coding=utf-8
import threading
from time import sleep, ctime


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(self.args)


def super_play(time, *files_):
    for file in files_:
        print('Start playing： %s! %s' % (file, ctime()))
        sleep(time)


list = {'爱情买卖.mp3': 3, '阿凡达.mp4': 5}

# 创建线程
threads = []
files = range(len(list))

for k, v in list.items():
    t = MyThread(super_play, (v, k), super_play.__name__)
    threads.append(t)


if __name__ == '__main__':
    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

# 主线程
print('end:%s' % ctime())