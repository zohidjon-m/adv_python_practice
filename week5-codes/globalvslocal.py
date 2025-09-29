#Local x hides (shadows) the global one.
# When you create a variable inside a function with the same name as a global variable, 
# the one inside the function takes priority while the function is running.
# The global variable is still there, but it’s hidden (shadowed) by the local one.
##########Examples
x = 100   # global

def func():
    x = 20   # local x (shadows the global x)
    print(x)

func()
print(x)
#Key points to remember:
# If a variable name exists both globally and locally, 
# the local version “wins” inside the function — it shadows the global one.