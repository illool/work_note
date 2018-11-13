# -*- coding: UTF-8 -*-

from multiprocessing import Pool, Lock, Value
from ctypes import c_bool
import os

tests_count = 80

lock = Lock()

#counter = Value('i', 0)  # int type，相当于java里面的原子变量
counter = Value('i', 1)


def run(fn):
    global tests_count, lock, counter
    with lock:
        if counter is False:
            counter = True
        else:
            counter = False
            counter.value += 1

    print('NO. (%s/%d) test start. PID: %d ' % (counter, tests_count, os.getpid()))
    # do something below ...


if __name__ == "__main__":
    pool = Pool(10)
    # 80个任务，会运行run()80次，每次传入xrange数组一个元素
    pool.map(run, range(80))
    pool.close()
    pool.join()