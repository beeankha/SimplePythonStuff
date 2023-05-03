# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is
# longer than the other, append the additional letters onto the end of
# the merged string.

# Return the merged string.

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_list = list(word1.strip(" "))
        word2_list = list(word2.strip(" "))
        merged_list = []
        while len(word1_list) or len(word2_list) > 0:
            if len(word1_list) == 0:
                # merged_list.append(word2_list[:])
                for x in range(len(word2_list)):
                    merged_list.append(word2_list.pop(0))
                break
            elif len(word2_list) == 0:
                # merged_list.append(word1_list[:])
                for x in range(len(word1_list)):
                    merged_list.append(word1_list.pop(0))
                break
            merged_list.append(word1_list.pop(0))
            merged_list.append(word2_list.pop(0))
        word = "".join(map(str, merged_list))
        return word

class BetterSolution:
    # a better solution than the above
    def mergeAlternately(self, word1, word2):
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

print(BetterSolution.mergeAlternately(BetterSolution, "abc", "pqr"))
    