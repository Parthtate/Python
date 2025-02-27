# file read 
f = open('chai.py')
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__()) 
# print(f.__next__()) 

# for line in open('chai.py'):
#     print(line, end='')

# while True:
#     line = f.readline()
#     if not line: break
#     print(line)

# list
myList = [1, 2, 3, 4]

I = iter(myList) # I variavle Hold's a memoery location
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I)) # on last index is exlcused, so automatically StopIteration



# Dictionary
D = {
    "a": 1,
    "b": 2,
    "c": 3
}
# I = iter(D) # Hold a memoery reference

# print(I.__next__())
# print(I.__next__())
# print(I.__next__()) # print the all values from dict

# range()

R = range(0, 5)
# print(iter(R)) # Hold a memoery reference

I = iter(R)
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I)) # last value in range is exlused, so it can't print StopIteration exception will raise