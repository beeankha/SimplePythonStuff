# Write a function that determines if a number is a prime number or not

def find_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return f"Sorry, {n} is not a prime number."
    return f"Yay, {n} is a prime number!"

print(find_prime(7))
print(find_prime(8))


# Bonus! The below are functions that test if a number is prime, and a function that
# returns all prime numbers within a specified range

def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes(r):
    # change the range number to get more or fewer primes!
    for n in range(r):
        if is_prime(n):
            print(n, end=' ', flush=True)
    print()

list_primes(1500)
