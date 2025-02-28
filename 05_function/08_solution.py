# **kwargs is similar to *args, but it take multiple parm from arguments as a multiple key, value pairs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:}: {value:}")

print_kwargs(name="Iron_man", power="fly", enemey="aliens")
print_kwargs(name="shaktiman", power="lazer")

