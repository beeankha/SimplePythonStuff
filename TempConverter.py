x=int(32)
y=int(5)
z=int(9)

#print('Let\'s figure out the temperature in celsius!')

#f = int(input('What is the temperature in farenheit? '))

def temp_converter(f):
    if type(f) not in [int, float]:
        raise TypeError("The temperature must be a number.")
    else:
        return (f - x) * y / z

#temp_converter(f)

# Test calculator
#temps = [f]
#message = "The temperature (in farenheit) of {temps} in celsius is {convtemp}."

#for f in temps:
#    F = temp_converter(f)
#    print(message.format(temps=f, convtemp=F))
