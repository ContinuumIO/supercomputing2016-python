import demo
import time

def slow_encode(input):
    return demo.Encoder(input).process_slow()

def fast_encode(input):
    return demo.Encoder(input).process_fast()

if __name__ == '__main__':
    input = 'a' * 10000000 # 10 millions of 'a'
    start = time.time()
    s1 = slow_encode(input)
    slow_stop = time.time()
    print('slow: %.2f sec' % (slow_stop - start))
    s2 = fast_encode(input)
    print('fast: %.2f sec' % (time.time() - slow_stop))
