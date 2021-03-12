import csv
from datetime import datetime

import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    # Because we’ve already read the header row, the loop will begin at the second 
    # line where the actual data begins. On each pass through the loop, we pull 
    # the data from index 5, which corresponds to the header TMAX, and assign it 
    # to the variable high. We use the int() function to convert the data, which 
    # is stored as a string, to a numerical format so we can use it. We then append 
    # this value to highs.
    print(highs)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    
    # Format plot.
    # ax.set_title("Daily high temperatures in Sitka, Alaska (July 2018)", fontsize=24)
    ax.set_title("Daily high temperatures in Sitka, Alaska during 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    # The above function call draws the date labels diagonally to prevent them 
    # from overlapping
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # The enumerate() function returns both the index of each item and the value 
    # of each item as you loop through a list

    # print(header_row)
