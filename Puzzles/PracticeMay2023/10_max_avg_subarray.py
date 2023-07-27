class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return 0
        if k == 0:
            return 0
        if not nums:
            return 0
        get_max = []
        index1 = 0
        index2 = k
        while index2 <= len(nums):
            get_max.append(sum(nums[index1:index2]))
            index1 += 1
            index2 += 1
        if get_max:
            biggest = max(get_max)
            print(biggest)
            result = (biggest / k)
            print(result)
            return result
        else:
            return 0

class BetterSolution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return 0
        if k == 0:
            return 0
        if not nums:
            return 0
        index1 = 0
        index2 = k
        biggest = sum(nums[index1:index2])
        while index2 <= len(nums):
            if sum(nums[index1:index2]) > biggest:
                biggest = sum(nums[index1:index2])
            index1 += 1
            index2 += 1
        if biggest:
            result = (biggest / k)
            return result
        else:
            return 0
