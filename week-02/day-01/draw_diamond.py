# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

n = int(input("Please enter a number: "))
if n% 2 == 1:
    for i in range(n//2 + 1):
        print(" " * (n//2-i) + "*" * (2*i+1) + " " *(n//2-i))
    for i in reversed(range(n//2)):
        print(" " * (n//2-i) + "*" * (2*i+1) + " " *(n//2-i))
else:
    for i in range(n//2):
        print(" "*(n//2-1-i) + "*"*(2*i+1) + " "*(n//2-1-i))
    for i in reversed(range(n//2)):
        print(" "*(n//2-1-i) + "*"*(2*i+1) + " "*(n//2-1-i))


