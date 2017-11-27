# Write a program that asks for two numbers and prints the bigger one

a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
if a > b:
    print(a)
elif a == b:
    print("The numbers are equal.")
else:
    print(b)
    