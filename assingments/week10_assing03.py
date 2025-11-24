import time

def logger(func):
    """Decorator that logs function name and execution time."""
    def wrapper(*args, **kwargs):
        print(f"\nRunning {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Result: {result}")
        print(f"Finished {func.__name__} in {end - start:.4f}s")
        return result
    return wrapper


@logger
def slow_add(a, b):
    time.sleep(1)
    return a + b


@logger
def fast_multiply(a, b):
    return a * b

slow_add(5, 3)
fast_multiply(3, 4)