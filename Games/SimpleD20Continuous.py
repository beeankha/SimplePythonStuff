from random import randint
import sys
import os

print('Input any key to roll!')
do_roll = input()

roll = (randint(1,20))
if roll == 1:
    print(f"You rolled a {roll}, CRITICAL MISS!")
elif roll == 20:
    print("You rolled a NATURAL TWENTY!")
else:
    print(f"Your roll is {roll}.")

os.execl(sys.executable, sys.executable, *sys.argv)
