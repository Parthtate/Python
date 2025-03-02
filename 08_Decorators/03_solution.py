import time

def cache(func):
    values = {}
    print(values)
    def wrapper(*args):
        if args in values:
            return values[args]
        result = func(*args)
        
        # if not found args in dict, add it
        values[args] = result 
        return result
    return wrapper    

@cache
def calculation(a, b):
    time.sleep(4)
    return a + b

print(calculation(77, 100))
print(calculation(77, 100))
print(calculation(4, 9))
print(calculation(4, 4))
print(calculation(4, 5))
print(calculation(4, 23))
print(calculation(4, 9))
print(calculation(4, 44))
print(calculation(4, 33))
print(calculation(4, 78))

