from typing import List


# Write a function that reverses a string (he input string elements are given as an array of characters).
# 
# Constraints:
# - Do not allocate extra space for another array; you must do this by modifying the input array in place with O(1) extra memory
# - All of the elements are printable ascii characters (symbols, numbers, and alphabets)
def reverse_string(s: List[str]) -> None:
	"""
	Do not return anything, modify `s` in-place instead.
	"""
	
	left = 0
	right = len(s) - 1
	
	while left < right:
		s[left], s[right] = s[right], s[left]
		
		left += 1
		right-= 1
		
string = ['t', 'i', 'h', 's', 'y', 'l', 'o', 'h']
string2 = ['😄', 'e', 'e', 'w', '😎']
reverse_string(string)
print(string)
reverse_string(string2)
print(string2)
