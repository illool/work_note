# encoding=utf8

from multiprocessing import Process, Queue
from time import sleep


def get(q):
    print("get start...")
    while True:
        while not q.empty():
            info = q.get()
            print('get %s' % info)
            print('is running')
        print('队列已经空了', info)
        sleep(1)


def put(q):
    while True:
        if q.empty():
            print("q.empty()")
            for i in range(5):
                q.put(str(i))
            q.put(None)
            print('put is done')
        else:
            info = q.get()
            print("put", info)
        sleep(2)


def main():
    print
    'main task start'
    q = Queue()
    #p1 = Process(target=put, args=(q,))
    p2 = Process(target=get, args=(q,))

    #p1.start()
    p2.start()
    put(q)
    #p1.join()
    #p2.join()

    print('main task done')


if __name__ == '__main__':
    main()

