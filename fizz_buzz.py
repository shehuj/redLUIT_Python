#!/usr/bin/env python3.7
# fizz_buzz.py
upper_limit = int(input("How many values should we process?: \n"))
for number in range(1, upper_limit + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#    print(number)