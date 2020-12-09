#!/usr/bin/env python3

message = 'This is the SMOOV test'

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your score?"))

# if input value was higher or equal to 25
if score >= 90:
    message = message + ('A')
elif score >= 80:
    message = message + ('B')
elif score >= 70:
    message = message + ('C')
else:
    message = message + ('Sorry, you failed the SMOOV test :(')
print(message)

