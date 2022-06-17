# Given an array that contains strings, figure out if an input string is an anagram
# of any of those strings in the array.

import re

def find_anagram(list, string):
    string = re.sub('[\W_]+', '', string)
    sorted_string = sorted(string.lower())
    string = "".join(sorted_string).strip()
    for s in list:
        s = re.sub('[\W_]+', '', s)
        if len(s) == len(string):
            sorted_s = sorted(s.lower())
            s = "".join(sorted_s).strip()
            if s == string:
                return "Hooray, your input string is an anagram of something in the list!"
            else:
                pass
    return "Sorry, no matching anagram was found in your list."

input_list = ["Hello", "Cat", "skdfjwiosdf!herlkjsdilofKASKNFEilkskfj kjsdf", "Hi, this is me!", "world", "apple#$&*^"]
input_string = "Dr. Low"
another_string = "Pa Peel*"
print(find_anagram(input_list, input_string))  # should return True
print(find_anagram(input_list, another_string))  # should return False
