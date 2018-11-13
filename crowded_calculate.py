import requests
import time
from threading import Thread
from multiprocessing import Process
import os,sys


_head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}
url = "http://www.tieba.com"

def count(x, y):
    # 使程序完成150万计算
    c = 0
    while c < 500000:
        c += 1
        x += 1
        y += 1


def write():
    dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dir,'test.txt')
    with open(filepath, 'w') as f:
        for x in range(5000000):
            f.write("testwrite\n")


def read():
    dir = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dir, 'test.txt')
    with open(filepath, 'r') as f:
        lines = f.readline()


def http_request():
    try:
        webpage = requests.get(url, headers = _head)
        html = webpage.text
        return {"context":html}
    except Exception as e:
        return {"error":e}


def io():
    write()
    read()


# single_Thread
def single_Thread_cpu():
    t = time.time()
    for x in range(10):
        count(1,1)
    print("single cpu", time.time()-t)


def single_Thread_io():
    t = time.time()
    for x in range(10):
        write()
        read()
    print("single io", time.time()-t)


def single_Thread_http():
    t = time.time()
    for x in range(10):
        http_request()
    print("single http", time.time()-t)


# mul__Thread
def mul_Thread_cpu():
    counts = []
    t = time.time()
    for x in range(10):
        thread = Thread(target=count,args=(1,1))
        counts.append(thread)
        thread.start()
    e = counts.__len__()
    while True:
        for th in counts:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("mul cpu",time.time() - t)


def mul_Thread_io():
    ios = []
    t = time.time()
    for x in range(10):
        thread = Thread(target=io)
        ios.append(thread)
        thread.start()
    e = ios.__len__()
    while True:
        for th in ios:
            if not th.is_alive():
                e -= 1
        if e < 0:
            break
    print("mul io",time.time() - t)


def mul_Thread_http():
    https = []
    t = time.time()
    for x in range(10):
        thread = Thread(target=http_request)
        https.append(thread)
        thread.start()
    e = https.__len__()
    while True:
        for th in https:
            if not th.is_alive():
                e -=1
        if e <= 0:
            break
    print("mul http",time.time() - t)


# mul_process
def mul_process_cpu():
    counts = []
    t = time.time()
    for x in range(10):
        p = Process(target=count, args=(1, 1))
        counts.append(p)
        p.start()
    e = counts.__len__()
    while True:
        for th in counts:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("Multiprocess cpu", time.time() - t)


def mul_process_io():
    t = time.time()
    ios = []
    t = time.time()
    for x in range(10):
        p = Process(target=io)
        ios.append(p)
        p.start()
    e = ios.__len__()
    while True:
        for th in ios:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("Multiprocess IO", time.time() - t)


def mul_process_http():
    t = time.time()
    httprs = []
    t = time.time()
    for x in range(10):
        p = Process(target=http_request)
        httprs.append(p)
        p.start()
    e = httprs.__len__()
    while True:
        for th in httprs:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("Multiprocess Http Request", time.time() - t)


if __name__ == '__main__':
    # single_Thread
    single_Thread_cpu()
    single_Thread_io()
    single_Thread_http()
    # mul__Thread
    mul_Thread_cpu()
    mul_Thread_io()
    mul_Thread_http()
    # mul_process
    mul_process_cpu()
    mul_process_io()
    mul_process_http()

    print("__file__=%s" % __file__)
    print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
    print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
    print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])
    print("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))
    print("os.getcwd()=%s" % os.getcwd())
    print("sys.path[0]=%s" % sys.path[0])
    print("sys.argv[0]=%s" % sys.argv[0])
