import math
cdef class SlowpokeCore:
    cdef public object N
    cdef public int divisor
    def __init__(self, N):
        self.N = N
        self.divisor = 1

    cdef double doWork(self, int N) except *:
        cdef int i, j, k
        cdef double res
        res = 1
        for j in range(N / self.divisor):
            k = 1
            for i in range(N):
                k += 1
            res += k
        return math.log(res)

    def __str__(self):
        return 'SlowpokeCore: %f' % self.doWork(self.N)
