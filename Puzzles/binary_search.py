# Take an input value and find at what index it occurs in a given list.

def binary_search(list, val):
    if not isinstance(val, int):
        return "Your value needs to be an integer, silly!"
    else:
        list_size = len(list) - 1
        index_0 = 0
        index_n = list_size

        # Find the middle-most value
        while index_0 <= index_n:
            middleval = (index_0 + index_n) // 2
            if list[middleval] == val:
                return f"Your value of {val} was found at index {middleval}!"
            # Compare the value with the middle-most value
            elif val > list[middleval]:
                index_0 += 1
            else:
                index_n -= 1
        return f"Your value of {val} was not in the array."
        
# Initialize the list
list = [2,7,19,34,53,72]

print(binary_search(list, 72))
print(binary_search(list, 11))
print(binary_search(list, 2))
print(binary_search(list, "a"))
print(binary_search(list, [1, 2, 3]))
print(binary_search(list, 19))
