from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, die.num_sides+1))
# Plotly doesn’t accept the results of the range() function directly, so we
# need to convert the range to a list explicitly using the list() function.
data = [Bar(x=x_values, y=frequencies)]
# The class Bar must be wrapped in square brackets, because a data set can have
# multiple elements.

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
# The offline.plot() function needs a dictionary containing the data and layout
# objects, and it also accepts a name for the file where the graph will be saved.

# print(frequencies)
