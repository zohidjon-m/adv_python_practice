# def greet(name, message="Hello"):
#     print(message, name)

# greet("Alice")          # Hello Alice
# greet("Alice", "Hi")    # Hi Alice

##########Important Rule: parameters with defaults must come after required ones.
# def greet(message="Hello", name):
#     print(message, name)
# greet("Alice")          # Error: missing 1 required positional argument: 'name'