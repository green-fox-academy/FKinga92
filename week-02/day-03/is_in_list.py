# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def list_contains(list1):
    if 4 in list1 and 8 in list1 and 12 in list1 and 16 in list1:
        print("True")
    else:
        print("False")

list_contains(list_of_numbers)