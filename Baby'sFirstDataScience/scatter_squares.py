import matplotlib.pyplot as plt

# First version of this file:

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=100)
#
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # Set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()


# Second versino of this file:

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# ^^ To define a color, pass the c argument a tuple with three decimal values
# (one each for red, green, and blue in that order), using values between 0 and 1.
# Values closer to 0 produce dark colors, and values closer to 1 produce lighter colors.

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ^^ This method of color mapping produces a gradient of color depending on the y value.

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
# ^^ Replacing the plt.show() line with the above will save the resulting graph
# to a file.
