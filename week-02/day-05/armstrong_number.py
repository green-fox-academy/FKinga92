# Exercise
# Write a simple program to check if a given number is an armstrong number. The program should ask for a number. 
# E.g. if we type 371, the program should print out: The 371 is an Armstrong number.

number = input("Please enter a number: ")
list_of_numbers = []
for i in range(len(number)):
    list_of_numbers.insert(len(list_of_numbers), int(number[i]))
sum = 0
for i in list_of_numbers:
    sum += i ** len(list_of_numbers)
print("The " + str(number) + " is an Armstrong number." if int(number) == sum 
      else "The " + str(number) + " isn't an Armstrong number.")

