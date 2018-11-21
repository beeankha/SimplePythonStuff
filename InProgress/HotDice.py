from random import randint
import sys
import os

# This file will display 6 randomly rolled d6s.
# It will also calculate the score (with no rerolls) according to the rules of hot dice.

#The below "input" section is in lieu of a button.
print("Let's play hot dice!")
print("Press any key + 'Enter' to roll.")
do_roll = input()

roll1 = (randint(1,6))
roll2 = (randint(1,6))
roll3 = (randint(1,6))
roll4 = (randint(1,6))
roll5 = (randint(1,6))
roll6 = (randint(1,6))

print(f"{roll1}, {roll2}, {roll3}, {roll4}, {roll5}, {roll6}")



os.execl(sys.executable, sys.executable, *sys.argv)

# ------------------------------------------------------------
# How to sort a Python dict by value
# (== get a representation sorted by value)

>>> xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

>>> sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

>>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
