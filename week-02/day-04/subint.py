# Find the part of int
# Create a function that takes a number and a list of numbers as a parameter
# Returns the indeces of the numbers in the list where the first number is part of
# Returns an empty list if the number is not part any of the numbers in the list
# Example

# input: [1, 11, 34, 52, 61], 1
# output: [0, 1, 4]

def find_part_of_int(alist, num1):
    string_list = ""
    for i in alist:
        string_list += str(i)
    if str(num1) in string_list:
        indeces = []
        for number in alist:
            number_index = next(index for index, num in enumerate(alist) if
                                num == number)
            if str(num1) in str(number):
                indeces.insert(len(indeces), number_index)
        return indeces
    return []

