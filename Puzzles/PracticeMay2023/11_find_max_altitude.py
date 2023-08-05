class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        starting = [0]
        for a in gain:
            starting.append(starting[-1] + a)
        return max(starting)
