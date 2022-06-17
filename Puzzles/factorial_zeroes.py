# Write an algorithm which computes the number of trailing zeroes in `n` factorial.

# Step 1: Figure out if the number is a number and also not "0"
# Step 2: Get the result of `n` factorial
# Step 3: Put that result in a list, separated by a ","
# Step 4: Check the last digit in the list, and if it's a 0, add to a tally and also
#         check the next number to see if it's a zero, etc.
# Step 5: Get the tally of zeroes, print it out as the result

# Normally can import `math` modules, but we'll use a custom function here.

def factorial_calculator(x):
    if x <= 0:
        return 0
    factorial = 1
    for i in range(1, x + 1):
        factorial = factorial * i
    return factorial

def factorial_zeroes(n):
    factorial = []

    if isinstance(n, str):
        print("This function only takes numbers, not strings!")
        return None
    if n > 0:
        result = factorial_calculator(n)
        print(f"The factorial of {n} is {result}.")
        result = str(result)
        factorial[:0]=result
        factorial = [int(x) for x in factorial]
    else:
        print("This function takes only whole integers larger than 0.")
        return None

    tally = []
    while len(factorial) > 1:
        last_digit = factorial[-1]
        if last_digit == 0:
            tally.append(0)
            factorial.pop()
        else:
            break

    print(f"The number of trailing zeroes in the factorial of {n} is {len(tally)}.")


factorial_zeroes(0)
factorial_zeroes("some string")
factorial_zeroes(3)
factorial_zeroes(10)
factorial_zeroes(15)
factorial_zeroes(20)
factorial_zeroes(27)
factorial_zeroes(49)
factorial_zeroes(56)
factorial_zeroes(68)
# factorial_zeroes(103)
# factorial_zeroes(205)

# There is a pattern emerging here!! 👀
