import multiprocessing
import time


def wait_for_event(e):
    print("wait_for_event: starting")
    e.wait()
    print("wairt_for_event: e.is_set()->" + str(e.is_set()))


def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout:starting")
    e.wait(t)
    print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))


if __name__ == "__main__":
    print("event=threading.Event() #设置一个事件实例,\
            event.set() #设置标志位,\
            event.clear() #清空标志位,\
            event.wait()  #等待设置标志位")
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name="block",
            target=wait_for_event,
            args=(e,))

    w2 = multiprocessing.Process(name="non-block",
            target=wait_for_event_timeout,
            args=(e, 2))
    w1.start()
    w2.start()

    time.sleep(3)

    e.set()
    print("main: event is set")