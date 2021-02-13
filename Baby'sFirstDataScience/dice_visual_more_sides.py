from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D10 and a D20
die_1 = Die(10)
die_2 = Die(20)

# Make some rolls, and store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
# The class Bar must be wrapped in square brackets, because a data set can have
# multiple elements.

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D10 and D20 dice 50,000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d10_d20.html')
# The offline.plot() function needs a dictionary containing the data and layout
# objects, and it also accepts a name for the file where the graph will be saved.

# print(frequencies)
