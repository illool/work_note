import threading
import time
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    print(thread.ident)
    _async_raise(thread.ident, SystemExit)


def test():
    while True:
        print('-------')
        time.sleep(0.5)


if __name__ == "__main__":
    threads = []
    t = threading.Thread(target=test)
    threads.append(t)
    t = threading.Thread(target=test)
    threads.append(t)
    t = threading.Thread(target=test)
    threads.append(t)
    t = threading.Thread(target=test)
    threads.append(t)
    t = threading.Thread(target=test)
    threads.append(t)
    t = threading.Thread(target=test)
    threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
    time.sleep(5.2)
    print("main thread sleep finish")
    for i in range(len(threads)):
        stop_thread(threads[i])

