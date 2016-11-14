from numba import jit

class MyInt(object):
    def __init__(self, x):
        self.x = x
        
@jit
def add_object(a, b):
    for i in range(100):
        c = i
        f = i + 7
        l = c + f
        
    return a.x + b.x

a = MyInt(5)
b = MyInt(6)

add_object(a, b)