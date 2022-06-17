# Misc. Interview Questions and Puzzles

## Binary Tree Traversal

Shows what a binary tree traversal would look like when written in Python.

## Binary Search

Take an input value and find at what index it occurs in a given list. If an integer
is not the value input, a helpful message gets printed.

## Collatz Conjecture

From [Popular Mechanics](https://www.popularmechanics.com/science/math/a29033918/math-riddle-collatz-conjecture/):
```
Take any natural number. There is a rule, or function, which we apply to that number, to get the next number.
We then apply that rule over and over, and see where it takes us. The rule is this: If the number is even,
then divide it by 2, and if the number is odd, then multiply by 3 and add 1.

Start with numbers other than 10, and you’ll still inevitably end at 1... we think. That’s the Collatz Conjecture.
```

This script takes any whole number input over `0` and returns the number of steps it takes to get that number to `1`.

## Corridor Puzzle

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

## Factorial Zeroes

Write an algorithm which computes the number of trailing zeroes in `n` factorial.

## Fibonacci Sequence

Print the `n`th number in a Fibonacci sequence.

## FizzBuzz

A classic! Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz”
if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.

## Linked List

Not necessarily solving a puzzle, per se, just a script that shows what a linked list object
would look like when written in Python.

## Longest Palindrome

Finds and outputs the longest palindrome in any given string. If multiples are found of
the same length, the latest one is output as the result.

## LRU Redis Cache

Implement an LRU cache with the use of Redis!

**Things to Note:**

Python comes with the LRU cache decorator!
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

Note: setting the `maxsize` to None will allow the cache to grow indefinitely!

AN LRU cache in Python is implemented using:
- `HashSeq`, which is essentially a hash table that maps the function and its parameter to the return value
- Doubly Linked list, which allows `O(1)` insertion and deletion from the front and back ends of the queue/list.

For more information about data types in Redis: https://redis.io/topics/data-types

## Min Stack/Max Stack

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum/maximum element in constant time.

- `push(x)` - Push element `x` onto stack
- `pop()` - Removes the element on top of the stack
- `top()` - Get the top element (sometimes referred to as "peek")
- `get_min()`/`get_max()` - Retrieve the minimum/maximum element in the stack

## Palindrome Proof

This module determines if any given string can be a palindrome or not. All capitalization and
spaces are disregarded; also, all non-alphabet characters (like punctuation and emojis) are
removed from the string!

## Pancake Sort

Given an array and an index number, flip all elements that are from index 0 to the specified index number.

```
Input:
array = [1, 2, 3, 4, 5, 6]
flip_index = 2

Output:
[3, 2, 1, 4, 5, 6]
```

## Prime Number Proof

Write a function that determines if a number is a prime number or not.

## Reverse String

Write a function that reverses a string (he input string elements are given as an array of characters).

**Constraints:**

- Do not allocate extra space for another array; you must do this by modifying the input array in
  place with `O(1)` extra memory
- All of the elements are printable `ascii` characters (symbols, numbers, and alphabets)

## Sum to 100

Given an unsorted array, find all integer pairs that sum up to 100.

## Two Sum

Given an array of integers `nums` and an integer `target`, return the index position of
the two numbers such that they add up to `target`.

**Constraints:**

- Each input would have exactly one solution, and you may not use the same element twice
- You can return the answer in any order

## Word Existence:

Given a 2D grid of characters and a word, the task is to check if that word exists in
the grid or not. A word can be matched in 4 directions at any point.
The 4 directions are Horizontally Left and Right, Vertically Up and Down.

## Word Search

Given a 2D grid of characters and a word, find all occurrences of the given word in the grid. A word can be matched in all eight directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form).

The eight directions are, Horizontally Left, Horizontally Right, Vertically Up, Vertically Down and four Diagonal directions.
