# Print the nth number in a Fibonacci sequence (where n is the given argument in the function)
def fibonacci_calculator(n):
    number = 0
    iterator = 1
    fibonacci = [0]
    while len(fibonacci) <= n:
        iterator = iterator + number
        number += iterator
        fibonacci.append(iterator)
        fibonacci.append(number)
    if (n % 2) == 0:
        print(f"F{n} is {fibonacci[-1]}")
    else:
        print(f"F{n} is {fibonacci[-2]}")

fibonacci_calculator(0)
fibonacci_calculator(1)
fibonacci_calculator(3)
fibonacci_calculator(8)
fibonacci_calculator(13)
fibonacci_calculator(19)
fibonacci_calculator(20)
fibonacci_calculator(200)
fibonacci_calculator(1000)
