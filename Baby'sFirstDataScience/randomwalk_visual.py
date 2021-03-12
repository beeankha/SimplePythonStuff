import matplotlib.pyplot as plt

from random_walk import RandomWalk

# First iteration of this file:

# # Make a random walk
# rw = RandomWalk()
# rw.fill_walk()
#
# # Plot the points in the walk
# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()


# Second iteration of this file, as a while-loop:

# Keep making new walks, as long as the program is active
while True:

    # Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    # The figsize parameter takes a tuple, which tells Matplotlib the dimensions
    # of the plotting window in inches (matplotlib assumes that your screen resolution
    # is 100 pixels per inch)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)

    # Emphasize the first and last num_points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_facecolor((0.5, 0.1, 0.2))

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
