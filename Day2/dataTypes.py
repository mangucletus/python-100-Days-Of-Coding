# primitive data types(string, integers, float, boolean ..etc)

#strings
from decimal import DivisionByZero
from signal import pthread_sigmask
from winreg import ExpandEnvironmentStrings


print("387" + "59577")
print("Hannah"[2])

#integer
print(1234 + 2358)

#float
x = 3.149

#boolean 
True
False

#some mathematical opeations
# PEMDAS:
# parentheses     ()
# Exponents       **
# Multiplication   *
# Division         /
# Substraction     -


# number manipulation
print(round(7/2, 3)) # round the result to three decimal places
print(9//4) # convert to integer value straight 

#f-string: allows to print different datatypes in a string
score = 0
height = 2.6
isRolling = True
print(f"your score is {score} and your height is {height}, you are rolling is {isRolling} ")


name = len(input("Please enter your name: "))
print(type(name))
num_char = str(name)
print(type(num_char))
print("Your name has " + num_char + "number of characters")


a = 145
print(type(a))

b= float(896)
print(type(b))

print(30 + float(49.92))
print(float(457.2) + float(132.0))