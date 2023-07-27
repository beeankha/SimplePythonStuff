class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m == 0:
            return True
        elif n == 0:
            return False
        elif m == n:
            if s == t:
                return True
            else:
                return False
    
        index = 0
        for l in s:
            new_index = t.find(l)
            if new_index > 0 and new_index == index:
                return False
            elif new_index >= index:
                index = new_index
                continue
            elif index > new_index:
                new_index = t[slice(index, len(t), 1)].find(l)
                if new_index < 0:
                    return False
                else:
                    continue
            else:
                return False
        if index:
            return True
        else:
            return False
        

class BetterSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        s_index = 0
        for l in t:
            if l == s[s_index]:
                s_index += 1
                if s_index == len(s):
                    return True
        return False