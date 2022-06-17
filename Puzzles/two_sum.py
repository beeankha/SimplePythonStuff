from typing import List

# Given an array of integers `nums` and an integer `target`, return the index position of
# the two numbers such that they add up to `target`.
#
# Constraints:
# - Each input would have exactly one solution, and you may not use the same element twice
# - You can return the answer in any order

def two_sum(nums: List[int], target: int) -> List[int]:
    store = {}
    for i in range(len(nums)):
        if nums[i] in store:
            return [store[nums[i]], i]
        else:
            store[target-nums[i]] = i

print(two_sum([2, 7, 11, 15], 9))
