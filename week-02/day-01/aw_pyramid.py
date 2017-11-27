# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

n = int(input("Please enter a number: "))
for i in reversed(range(n)):
    print(" " * i + "*" * (2 * n - 1 - 2 * i) + " " * i) 
