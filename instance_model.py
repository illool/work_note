# coding: utf-8

import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton, "_instance"):
                # Singleton._instance = Singleton(*args, **kwargs)
                Singleton._instance = Singleton()
        return Singleton._instance


def task(arg):
    print(arg)
    obj_ = Singleton.instance()
    print(obj_)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()
    time.sleep(20)
    obj = Singleton.instance()
    print(obj)
