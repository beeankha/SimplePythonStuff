class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given a string s, reverse only all the vowels in the string and return it.
        """
        # list all possible vowels (in lower case)
        vowels = ['a', 'e', 'i', 'o', 'u']
        # make input string lower case so it can be validated against the list
        to_replace = []
        index = []
        # iterate over every letter in s to see if it's a vowel;
        # if it is, store it in reverse order in a placeholder list
        for i in range(len(s)):
            if s[i].lower() in vowels:
                to_replace.append(s[i])
                index.append(i)
            else:
                pass
        # reverse the list of vowels
        to_replace.reverse()
        # iterate over the list of vowels and replace the vowels in s
        # with the reversed vowels
        for i in range(len(to_replace)):
            s = s[:index[i]] + to_replace[i] + s[index[i]+1:]
        return s
    