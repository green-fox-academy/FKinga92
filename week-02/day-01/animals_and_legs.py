# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chickens = int(input("Please enter a number: "))
pigs = int(input("Please enter another number: "))
legs = chickens * 2 + pigs * 4

print("The animals have " + str(legs) + " legs.")
