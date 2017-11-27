# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

n = 8
x = 0
while (n-x) != 0:
    x = int(input("Guess the number: "))
    if n > x:
        print("The stored number is higher.")
    elif n < x:
        print("The stored number is lower.")
    else:
        print("You found the number: 8")
        break

