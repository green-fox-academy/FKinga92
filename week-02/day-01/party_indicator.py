# Write a program that asks for two numbers
# Thw first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

girls = int(input("Please enter the number of girls attending: "))
boys = int(input("Please enter the number of boys attending: "))
people = girls + boys

if girls == boys and people > 20:
    print("The party is excellent!")
elif (girls != boys) and (girls > 0) and (people > 20):
    print("Quite cool party!")
elif people < 20:
    print("Average party...")
elif girls == 0:
    print("Sausage party")
else:
    print("20 people are coming, including girls.")