# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# # Should print out:
# # ["n", "g", "r", "m"]

def unique_characters(string):
    list_of_unique_characters = []
    for char in string.replace(" ", ""):
        if string.lower().count(char) == 1:
            list_of_unique_characters.append(char)
    return list_of_unique_characters

# print(unique_characters("anagram"))