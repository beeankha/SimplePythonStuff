# List comprehension info:
# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# https://calmcode.io/comprehensions/introduction.html

def fizz_buzz(n):
    numbers = [x for x in range(1, n)]  # list comprehension!!

    for x in numbers:
        if (x / 3).is_integer() and (x / 5).is_integer():
            print("fizzbuzz!")
        elif (x / 3).is_integer():
            print("fizz")
        elif (x / 5).is_integer():
            print("buzz")
        else:
            print(x)

fizz_buzz(100)
