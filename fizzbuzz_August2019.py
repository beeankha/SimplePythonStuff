numbers = [x for x in range(1, 101)]

for x in numbers:
    if (x / 3).is_integer() and (x / 5).is_integer():
        print("fizzbuzz!")
    elif (x / 3).is_integer():
        print("fizz")
    elif (x / 5).is_integer():
        print("buzz")
    else:
        print(x)
