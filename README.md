# Simple Stuff

## Misc. simple Python 3 projects for teaching myself basic concepts.


### **DrawCircle**

Draws a circle.


### **PrimeNumberGenerator**

Generates prime numbers up to a specified range.


### **TempConverter**

A very simple temperature converter script.


### **FizzBuzz**

A much famous test.


### **Lunch Randomizer**

Helps select where to go to lunch in downtown Durham, NC.


### **Magic 8 Ball**

Ask a yes or no question and get an answer!


### **PrimeNumberGenerator**

Find all prime numbers within a specified range.


### **Image Changer**

Run `image_changer.py` on any JPEG image to stylize it like so:

_Before:_

![Original Photo](images/august_marshmallows.jpg)

_After:_

![Altered Photo](images/cartoonized_august_marshmallows.jpg)

> When the stylized image pops up, press any key to activate the `Save the image? [y]/[n]` prompt

Dependencies include [`cv2`](https://pypi.org/project/opencv-python/) and `numpy`. Based on the excellent tutorial found [here](https://dev.to/stokry/how-to-cartoonize-an-image-with-python-1e01)


### **Collatz Conjecture**

From [Popular Mechanics](https://www.popularmechanics.com/science/math/a29033918/math-riddle-collatz-conjecture/):
```
Take any natural number. There is a rule, or function, which we apply to that number, to get the next number.
We then apply that rule over and over, and see where it takes us. The rule is this: If the number is even,
then divide it by 2, and if the number is odd, then multiply by 3 and add 1.

Start with numbers other than 10, and you’ll still inevitably end at 1... we think. That’s the Collatz Conjecture.
```

This script takes any whole number input over `0` and returns the number of steps it takes to get that number to `1`.



### **Corridor Puzzle**

Description from [101 Computing.net](https://www.101computing.net/the-school-lockers-puzzle/):

```
On the first day of school, the principal of Locker High school decides to conduct an experiment. The school has exactly
100 students and 100 lockers all lined up alongside the main corridor of the school.

- The principal asks the first student to walk down the main corridor of the school to close all the lockers.
- The principal then asks the second student to walk down the main corridor and open every other locker.
- The principal then asks the third student to walk down the main corridor and either open every third locker if it is closed, or close it if it is open.
- The fourth student will then repeat the same process for every fourth locker.

And so on, till the last of the 100 students repeats this process for every 100th locker, so in fact, just opening the
100th locker if it's closed, or close it if it is already open.
At the end of this experiment the principal decides to count the number of lockers which are closed.
```

The corresponding Python file uses True/False booleans to figure out which lockers are closed and which are open.
