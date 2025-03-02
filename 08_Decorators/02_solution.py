def debug(func):
    def wrapper(*args, **kwargs):
        # return arguments passed in functions
        args_values = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{k}: {v}" for k, v in kwargs.items())
        print(f"function Name: {func.__name__} with arguments {args_values} and key_value {kwargs_values}")
        return func(*args, **kwargs)

    return wrapper    

@debug
def hello():
    print("what's up!")
@debug
def greeting(name, greet):
    print(f"{greet}, {name}")    

hello()
greeting("Sam", "Namaste")    