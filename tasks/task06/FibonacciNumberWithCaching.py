from functools import lru_cache
import time

class measure_elapsed_time(object):
    def __init__(self, f):
        self.f = f
        self.active = False

    def __call__(self, *args):
        if self.active:
            return self.f(*args)
        start = time.time()
        self.active = True
        res = self.f(*args)
        end = time.time()
        self.active = False
        print(f"Time = {end - start}")
        return res
    

@lru_cache(maxsize = 128)
@measure_elapsed_time
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

@measure_elapsed_time
def my_fn1(arg1, arg2):
   time.sleep(0.5)
   return arg1 + arg2


print(fibo(100))
print(my_fn1(100,100))