from __future__ import print_function

import sys
if sys.version_info < (3,0,0):
    from thread import get_ident
else:
    from threading import get_ident
import threading
import time

class WaitClass:
    def __init__(self, time):
        self.time = time

    def __call__(self):
        ident = get_ident()
        print('START task_noop_waiter: %s\n' % ident, end='')
        time.sleep(self.time)
        print('STOP task_noop_waiter: %s\n' % ident, end='')


def do_work(self):
    ident = get_ident()
    print('START1 task_cpu_eater: %s\n' % ident, end='')
    stop = time.time() + self.time
    while time.time() < stop:
       pass
    print('STOP1 task_cpu_eater: %s\n' % ident, end='')

class SpinClass:
    def __init__(self, time):
        self.time = time

    def __call__(self):
        do_work(self);

def main():
    ident = get_ident()
    print('START main: %s\n' % ident, end='')
    wc = WaitClass(9)
    sc = SpinClass(7)
    t1 = threading.Thread(target=wc)
    t2 = threading.Thread(target=sc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('STOP main: %s\n' % ident, end='')

if __name__ == '__main__':
    main()
