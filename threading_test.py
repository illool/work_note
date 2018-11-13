# coding:utf-8
import threading
import time


def fun(l, i):
    time.sleep(10.)
    l.append(i)


def fun_main():
    lsit_ = []
    threads = []
    for i in range(10):
        t = threading.Thread(target=fun, name='LoopThread' + ":" + str(i), args=(lsit_, i))
        threads.append(t)
    for i in range(10):
        threads[i].start()
    for i in range(10):
        threads[i].join()
    return lsit_


if __name__ == '__main__':
    start = time.time()
    l_ = fun_main()
    end = time.time()
    print(end - start)
    print(l_)
