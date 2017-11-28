# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

n= int(input("Please enter a number: "))
if n > 10:
    print("Please enter a number between 1 and 10")
else:
    sum = 0
    for i in range(n):
        m = int(input("Please enter a number: "))
        sum += m
    print("Sum: " + str(sum) + ", Average: " + str(sum/2))
