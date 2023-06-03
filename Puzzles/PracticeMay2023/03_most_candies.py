# There are n kids with candies. You are given an integer array of candies,
# where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that
# you have.

# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies, they will have the greatest
# number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

import numpy as np
from types import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sorted_list = sorted(candies)
        highest_number = sorted_list[-1]
        determination = []
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= highest_number:
                determination.append(True)
                continue
            if (candies[i] + extraCandies) < highest_number:
                determination.append(False)
                continue
        return determination


class BetterSolution:
    # A better solution than the above 🤯
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return np.array(candies) + extraCandies >= np.array(candies).max()
