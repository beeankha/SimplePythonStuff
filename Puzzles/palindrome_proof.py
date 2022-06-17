# ⚠️ 🚧 Some bits were commented out but left in, to show slightly different approaches I took. 🚧 ⚠️
# Determine if a given string can be a palindrome or not.
# Disregard capitalization and spaces.
# BONUS: Remove all non-alphabet characters from the string!

# import itertools
import re

def convert(string):
    new_string = re.sub('[\W_]+', '', string)
    list = []
    list[:0]=new_string.lower()
    list.sort()
    return list

# def compare(a, b):
#     return (a > b) - (a < b)

def palindrome_check(list):
    print(f'Your original text is: "{list}"')
    list = convert(list)
    # if len(list) <= 1:
    #     print("Yep, one single letter is technically a palindrome!")
    pairs = []
    remainders = []
    while len(list) > 1:
        # for a, b in itertools.combinations(list, 2):
        #     compare(a, b)
        # https://docs.python.org/3/library/itertools.html#itertools.combinations
        a = list[-1]
        b = list[-2]
        if a == b:
            pairs.append(a)
            pairs.append(b)
            list.remove(a)
            list.remove(b)
        else:
            remainders.append(a)
            list.remove(a)

    if len(remainders) > 1:
        return "Sorry, no palindrome here. 🤔\n"
    # elif len(remainders) == 1 and len(list) == 1:
    #     return "Sorry, no palindrome here. 😖\n"
    else:
        return "Yay, that is a possible palindrome! 😁\n"

str1 = "Tat coca"
print(palindrome_check(str1))

str2 = "a"
print(palindrome_check(str2))

str3 = "Hannah XYZ!"
print(palindrome_check(str3))

str4 = "Hi madam, I'm Adam"
print(palindrome_check(str4))

str5 = "Able was I ere I saw Elba!"
print(palindrome_check(str5))

str6 = "A man, a plan, a canal – Panamas!!"
print(palindrome_check(str6))

str7 = "Never odd or even 😄"
print(palindrome_check(str7))

str7 = "Ghghteyruizxs,kxcnmxcvk&^%&*"
print(palindrome_check(str7))
