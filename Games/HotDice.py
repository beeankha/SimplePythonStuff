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
