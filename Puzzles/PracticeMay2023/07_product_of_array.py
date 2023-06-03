from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        target_list = []
        list_size = len(nums)
        if list_size:
            for index in range(list_size):
                target_list.append(reduce((lambda x, y: x * y), nums[:index] + nums[index + 1:]))
        return target_list
