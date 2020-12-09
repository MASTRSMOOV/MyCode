#!/usr/bin/env python3

message = 'This is the SMOOV test! '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your score?"))

# if input value was higher or equal to 90
if score >= 90:
    message = ('Oh, you SMOOV SMOOV!')
elif score >= 80:
    message = ('You SMOOV AF')
elif score >= 70:
    message = ('You SMOOV')
else:
    message = message + ('Sorry, you failed the SMOOV test :(')
print(message)

