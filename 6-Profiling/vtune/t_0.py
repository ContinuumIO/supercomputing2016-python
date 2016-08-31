import logging
import time

try:
    xrange
except NameError:
    # python3
    xrange = range

class BigObject:
    STR_VALUE = ''.join(str(x) for x in xrange(10000))
    def __str__(self):
        return self.STR_VALUE

def makeParams():
    objects = tuple(BigObject() for _ in xrange(50))
    template = ''.join('{%d}' % i for i in xrange(len(objects)))
    return template, objects

def doLog():
    template, objects = makeParams()
    for _ in xrange(1000):
        logging.info(template.format(*objects))

def main():
    logging.basicConfig()

    start = time.time()
    doLog()
    stop = time.time()
    print('run took: %.3f' % (stop - start))

if __name__ == '__main__':
    main()
