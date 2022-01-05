# Read a description about this math problem here:
# https://www.popularmechanics.com/science/math/a29033918/math-riddle-collatz-conjecture/

x = int(input("Enter a number: "))

def collatz_conjecture(x):
    original_value = x
    counter = 0
    if x <= 0:
        print("Sorry, you need a number larger than zero for this problem.")
    if isinstance(x, float):
        print("Sorry, only whole numbers work for this problem.")
    if not isinstance(x, int):
        print("Please input a whole number with a value greater than 0!")
    else:
        while x > 1:
            if (x % 2) == 0:
               x = x // 2
               counter += 1
            else:
               x = (x * 3) + 1
               counter += 1
    print(f"The number of steps it takes to get {original_value} to 1 via the Collatz Conjecture is {counter}")

collatz_conjecture(x)
