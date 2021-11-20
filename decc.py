def logme(func):
    def wrapped(*args, **kwargs):
        print(f"call: {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)  
    return wrapped

print(1)