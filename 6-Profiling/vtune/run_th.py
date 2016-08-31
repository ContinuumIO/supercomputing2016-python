import demo
import time
import threading

def slow_encode(input):
    return demo.Encoder(input).process_slow()

def fast_encode(input):
    return demo.Encoder(input).process_fast()

if __name__ == '__main__':
    input = 'a' * 10000000 # 10 millions of 'a'
    th1 = threading.Thread(target=slow_encode, args=(input,))
    th2 = threading.Thread(target=fast_encode, args=(input,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
