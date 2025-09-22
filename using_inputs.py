#import random
# from random import randint #import specific function
#number = random.randint(0, 10)
# number = random.random(0, 10) # for float
#print(number)


import os  # built-in: interact with the operating system (e.g., paths, directories)
import sys  # built-in: access Python runtime details (e.g., executable, argv)
import random  # built-in: generate random numbers
import matplotlib.pyplot as plt  # external: create plots and visualizations
import pyfiglet  # external & obscure: generate ASCII art text
import redLUIT_Python.ec2randomName_foundational as ec2randomName_foundational  # custom: a user-defined module (must exist in your project)

# Show some OS info
print(
    "Current working directory:", os.getcwd()
)  # prints the folder where this script is running
print(
    "Python executable:", sys.executable
)  # prints the path of the Python interpreter being used

# Generate random numbers
numbers = [
    random.randint(0, 10) for _ in range(10)
]  # list of 10 random integers between 0 and 10
print("Random numbers:", numbers)  # print the list of random numbers

# Plot with matplotlib
plt.plot(
    numbers, marker="o", linestyle="-", color="purple"
)  # line plot with circular markers
plt.title("Random Numbers Plot")  # title of the plot
plt.xlabel("Index")  # x-axis label
plt.ylabel("Value")  # y-axis label
plt.show()  # display the plot in a separate window

# Use obscure library: pyfiglet
ascii_banner = pyfiglet.figlet_format(
    "Python Rocks!"
)  # generate ASCII art for the text
print(ascii_banner)  # print the ASCII art banner

# Use custom module
ec2randomName_foundational.say_hello()  # call a function from your custom hello_world module
