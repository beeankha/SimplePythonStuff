# True = open
# False = closed

doors = [False] * 101  # ignore index 0

for i in range(1, 101):
    # for the second pass, x = 2, so we start at door 2, for the 3rd pass we start at door 3 etc.
    for j in range(i, 101, i):
        doors[j] = not doors[j]

# This bit prints out just the positions of the open doors
for i in range(1, 101):
    if doors[i]:
        print(i)

print(doors)
print(doors.count(True))
