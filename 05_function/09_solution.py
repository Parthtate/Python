# In Python, yield is used inside a function to create a generator. A generator allows you to pause and resume execution, making it memory-efficient compared to returning a large list.

def even_generator(number):
    for i in range(2, number+1, 2):
        yield i

for i in even_generator(10):
    print(i)
