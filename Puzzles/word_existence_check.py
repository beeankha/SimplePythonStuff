# Given a 2D grid of characters and a word, the task is to check if that word exists in
# the grid or not. A word can be matched in 4 directions at any point.
# The 4 directions are, Horizontally Left and Right, Vertically Up and Down. 
# 
# Examples: 
# Input:  grid[][] = {"axmy",
#                     "bgdf",
#                     "xeet",
#                     "raks"};
# Output: Yes
# 
# a x m y
# b g d f
# x e e t
# r a k s
# 
# Input: grid[][] = {"axmy",
#                    "brdf",
#                    "xeet",
#                    "rass"};
# Output : No

# Python3 program to check if the word
# exists in the grid or not
 
# Function to check if a word exists
# in a grid starting from the first
# match in the grid level: index till 
# which pattern is matched x, y: current
# position in 2D array

def find_match(mat, pat, x, y, nrow, ncol, level):

    l = len(pat)

    # Pattern matched
    if (level == l):
        return True

    # Out of boundary
    if (x < 0 or y < 0 or x >= nrow or y >= ncol):
        return False

    # If the grid matches with a letter while recursion
    if (mat[x][y] == pat[level]):

        # Marking this cell as visited
        temp = mat[x][y]
        mat[x].replace(mat[x][y], "#")

        # Finding subpatterns in four directions
        res = (find_match(mat, pat, x - 1, y, nrow, ncol, level + 1) |
               find_match(mat, pat, x + 1, y, nrow, ncol, level + 1) |
               find_match(mat, pat, x, y - 1, nrow, ncol, level + 1) |
               find_match(mat, pat, x, y + 1, nrow, ncol, level + 1))

        # Marking this cell as unvisited again
        mat[x].replace(mat[x][y], temp)
        return res

    else:  # Not matching, then false
        return False

# Function to check if the word exists in the grid or not
def check_match(mat, pat, nrow, ncol):

    l = len(pat)

    # If total characters in matrix is less than pattern length
    if (l > nrow * ncol):
        return False

    # Traverse in the grid
    for i in range(nrow):
        for j in range(ncol):

            # If first letter matches, then recur and check
            if (mat[i][j] == pat[0]):
                if (find_match(mat, pat, i, j, nrow, ncol, 0)):
                    return True
    return False

rows = 4
columns = 4

# Driver Code
if __name__ == "__main__" :

    grid = ["axmy", "bgdf",
            "xeet", "eaks"]

    # Function to check if word
    # exists or not
    if (check_match(grid, "geeks", rows, columns)) :
        print("Yes, that word exists in this grid!")
    else :
        print("That word doesn't exist in this grid.")
