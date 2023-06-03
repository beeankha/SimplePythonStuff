# You have a long flowerbed in which some of the plots are planted,
# and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means
# empty and 1 means not empty, and an integer n, return true if n new flowers
# can be planted in the flowerbed without violating the no-adjacent-flowers
# rule and false otherwise.

import numpy as np
from types import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True
        elif len(flowerbed) == 1:
            if flowerbed == [0]:
                return True
            else:
                return False
        # Create an array that is 1 where a is 0, and pad each end with an extra 0.
        iszero = np.concatenate(([0], np.equal(flowerbed, 0).view(np.int8), [0]))
        absdiff = np.abs(np.diff(iszero))
        # Runs start and end where absdiff is 1.
        ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
        for [x, y] in ranges:
            difference = y - x
            if difference == 2:
                # if the plot size is 2 but at either edge, then a flower
                # can be planted there
                if x == 0 or y == len(flowerbed):
                    n = n - 1
                else:
                    pass
            elif difference <= 2:
                # if the potential plot is 2 or smaller but not at the edge,
                # the automatic answer is "can't plant a flower here"
                pass
            elif (difference % 2) == 0:
                # this takes care of even-numbered cases larger than 4
                if x == 0 or y == len(flowerbed):
                    d = difference // 2
                    n = n - d
                else:
                    d = difference // 2
                    d = d - 1
                    n -= d
            elif (difference % 2) != 0:
                # this takes care of odd-numbered cases larger than 3
                if x == 0 or y == len(flowerbed):
                    d = difference // 2
                    d = d + 1
                    n -= d
                else:
                    d = difference // 2
                    n -= d
            else:
                d = difference // 2
                n -= d
        if n <= 0:
            return True
        else:
            return False
