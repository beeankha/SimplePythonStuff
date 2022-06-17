# Given an array and an index number, flip all elements that are from index 0
# to the specified index number
# Example:
#
# Input:
# array = [1, 2, 3, 4, 5, 6]
# flip_index = 2
#
# Output:
# [3, 2, 1, 4, 5, 6]

def pancake_flip(list, index):
    if not isinstance(index, int):
        print("Specified index is not an integer!")
        return
    if index <= 0:
        print("Please input an integer that is 1 or larger.")
        return
    else:
        index_counter = index
        insert_index = 0
        while index_counter >= 0:
            pancake = list[index]
            list.remove(pancake)
            list.insert(insert_index, pancake)
            insert_index += 1
            index_counter -= 1
        print(list)

to_flip = [1, 2, 3, 4, 5, 6, 7]
flip_where = 3

pancake_flip(to_flip, flip_where)

flip_error = "flip!"
pancake_flip(to_flip, flip_error)

flip_nonexist = -2
pancake_flip(to_flip, flip_nonexist)

letter_flip = ['e', 'h', 'l', 'l', 'o']
flip_letter = 1

pancake_flip(letter_flip, flip_letter)
