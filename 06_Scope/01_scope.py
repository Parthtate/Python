# In python scope also known as Namespaces
# Closure, global scope we study, like in every language

a = 22
def fun1():
    a = 44
    print(a)

# fun1()
# print(a)   
# same variable, but differ memoery allocation. 

x = 2
def fun2():
    # x = 10
    z = x ** 2
    return z

# result_fun2 = fun2()
# print(result_fun2)

# if x variable is not available, if finds from global scope, called (steping up)

# Closure scope: also known as factory function

def parent():
    x = 2
    def child():
        print(x)
    return child        

# print(parent()) # In parent() store child function reference, not execution. 

result_parent = parent()
result_parent() 
# In closure all the assoiated reference goes in the function