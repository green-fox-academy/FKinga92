# Write a function, that takes a string as an argument and returns a
# dictionary  with all letters in the string as keys, and numbers as
# values that shows how many occurrences there are.
# Create a test for that.

def count_letters(a_string):
    dictionary_of_letters = {}
    for letter in a_string.replace(" ", ""):
        if letter in dictionary_of_letters.keys():
            dictionary_of_letters[letter] += 1
        else:
            dictionary_of_letters[letter] = 1
    return dictionary_of_letters
