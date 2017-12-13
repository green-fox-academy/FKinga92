# Create a sum method in your class which has a list of integers as parameter
# It should return the sum of the elements in the list
# Follow these steps:
# Add a new test case
# Instantiate your class
# create a list of integers
# use the assertEquals to test the result of the created sum method
# Run it
# Create different tests where you
# test your method with an empyt list
# with a list with one element in it
# with multiple elements in it
# with a null
# Run them
# Fix your code if needed

class Numbers(object):

    def __init__(self):
        pass
    
    def summa(self, numbers):
        self.numbers = numbers
        if self.numbers == None:
            return "Not a list"
        sum_of_all_numbers = 0
        for number in self.numbers:
            sum_of_all_numbers += number
        return sum_of_all_numbers
