import time 
import math

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = timer(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran at {end-start}")
        return result
    return wrapper

@timer
def sample(n):
    time.sleep(n)

sample(2)