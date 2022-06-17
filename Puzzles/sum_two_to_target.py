# Initial solution, O(n^2)
# def sum_to(number_list, target):
#     sum_100 = []
#     while len(number_list) > 1:
#         first = number_list[0]
#         number_list.pop(0)
#         if len(number_list) > 1:
#             for x in number_list:
#                 if first + x == 100:
#                     sum_list = []
#                     number_list.remove(x)
#                     sum_list.append(first)
#                     sum_list.append(x)
#                     sum_100.append(sum_list)
#                     break
#                 else:
#                     pass
#     else:
#         pass
#     return sum_100


# Second attempt, sorting and removing elements
def sum_to(number_list, target):
    number_list.sort()
    print(number_list)
    sum_pairs_list = []
    while len(number_list) > 1:
        last_index = -1
        first = number_list[0]
        last = number_list[last_index]
        if first + last == target:
            sum_pairs = []
            sum_pairs.append(first)
            number_list.remove(first)
            sum_pairs.append(last)
            number_list.remove(last)
            sum_pairs_list.append(sum_pairs)
        elif first + last > target:
            number_list.remove(last)
            last_index -= 1
        else:
            number_list.remove(first)

    return sum_pairs_list

arr1 = [1, 50, 99, 46, 50, 37, 4, 96, 37, 7, 54, 1, 63, 99, 46, 50, 54, 1, 50, 99, 46, 50, 54, 49]
arr2 = [50, 50, 50, 50, 50]
arr3 = [46, 38, 1, 2, 9, 35, 27, 59, 19, 57, 89, 11, 34, 50, 50, 50, 29, 61, 56, 20, 38, 81, 80, 40, 42, 75, 39, 75, 25, 20]

print(sum_to(arr1, 83))
print(sum_to(arr2, 100))
print(sum_to(arr3, 100))
