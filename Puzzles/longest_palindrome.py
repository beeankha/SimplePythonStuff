class Solution:
    def longest_palindrome(self, s: str) -> str:
        result = ""
        
        for i in range(len(s)):
            word1 = self._check_palindrome(s, i, i)
            word2 = self._check_palindrome(s, i, i+1)
            
            if len(word1) >= len(word2):
                longest = word1
            else:
                longest = word2
            if len(longest) >= len(result):
                result = longest
            else:
                result = result
        return result

    def _check_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        
        return s[left+1:right]
        
obj = Solution()
results = obj.longest_palindrome("atsdkjhfcataxyx")
print(results)
