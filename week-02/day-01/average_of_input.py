# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

a = int(input("Please enter an integer: "))
b = int(input("Please enter an integer: "))
c = int(input("Please enter an integer: "))
d = int(input("Please enter an integer: "))
e = int(input("Please enter an integer: "))

sum = a + b + c + d + e
average = sum / 5

print("Sum: " + str(sum) + ", " + "Average: " + str(average))
