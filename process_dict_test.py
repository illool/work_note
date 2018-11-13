import multiprocessing
import time


def worker(d, key, value):
    #d[(key*1., key+1.)] = {(key*1., key+1.) : value}
    if 's' not in list(d.keys()):
        d['s'] = []
        d['s'].append(key)
    else:
        d['s'].append(key)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(d, i, i*2))
             for i in range(10)
             ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Results:')
    #for key, value in enumerate(dict(d)):
    #    print("%s=%s" % (key, value))
    for key in list(d.keys()):
        print(key, d[key])
