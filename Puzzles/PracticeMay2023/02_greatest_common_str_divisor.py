# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides
# both str1 and str2.

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)<=len(str2):
            temp = str1
        else:
            temp = str2
        m = len(temp)
        x = 1
        res=[""]
        while x <= m:
            if m % x == 0 and temp[:x] * (len(str1)//x) == str1 and temp[:x] * (len(str2)//x) == str2:
                res.append(temp[:x])
                x+=1
        return res[-1]


class BetterSolution:
    # A better version of the above
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return ''
        # Take the greatest common divisor of the lengths of the two strings
        # and return that slice of string 🤯
        return str1[:math.gcd(len(str1), len(str2))]
    
# Read more about math.gcd() here: https://docs.python.org/3/library/math.html#math.gcd
