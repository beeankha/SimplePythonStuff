class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        reversed = []
        reversed_string = ""
        for word in word_list:
            if word:
                reversed.append(word)
        reversed.reverse()
        for i in reversed:
            reversed_string = reversed_string + " " + i
        return reversed_string.strip()

# This is a better solution than the above 🤯
class BetterSolution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])