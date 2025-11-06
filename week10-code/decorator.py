
# TODO: Create a decorator that prints:
# "Starting..." before the function,
# "Finished!" after the function.
def trace(func):
    def wrapper():
        print("Starting ....")
        func()
        print("Finished...")
    return wrapper
@trace
def greet():
    print("Hello students!")    
greet()
