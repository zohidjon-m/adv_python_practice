class Countdown:
    """Iterator that counts down from n to 0 inclusive."""

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = self.n
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def countdown(n):
    """Generator version that yields n, n-1, …, 0."""
    while n >= 0:
        yield n
        n -= 1
        
print("[Assignment 1] Iterator output:")
for x in Countdown(3):
    print(x, end=" ")
print("\n[Assignment 1] Generator output:")
for x in countdown(3):
    print(x, end=" ")
print()