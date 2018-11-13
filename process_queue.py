import multiprocessing


def writer_proc(q):
    try:
        l = list(range(100000))
        q.put(l, block=True)
    except:
        pass


def reader_proc(q):
    try:
        print(q.get(block=True))
    except:
        pass


if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    reader.join()
    writer.join()