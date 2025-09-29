#recursion

def factorial(n):
    print(n,";")
    if n== 0:
        return 1
    return n* factorial(n-1)

# print(factorial(9))


#lambda 
square = lambda x:x*x
# print(square(5))



# Write a function that takes a list of numbers and returns their sum.
def simple_sum(numbers):
    sum = 0
    for i in numbers:
        sum +=i
    return sum

from functools import reduce
def functional_sum(nums):
    return reduce(lambda x, y: x+y, nums)

numbers = [1,23,4,5,64,645,22]
nums = [1,2,3]
print(simple_sum(numbers))
print(functional_sum(numbers))


# Write a function is_prime(n) that checks if a number is prime.

# Write a recursive function to compute Fibonacci numbers.

# Write a function that takes a string and returns it reversed.
def string_reverse(string):
    chars = list(string)
    l=0
    r = len(chars)-1
    while l<r:
        chars[l],chars[r]= chars[r], chars[l]
        l+=1
        r-=1
    return ''.join(chars)

print(string_reverse("apple and banana"))

# Write a function that takes another function as input and applies it twice.