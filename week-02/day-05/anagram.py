# Create a function named is anagram following your current language's style guide. 
# It should take two strings and return a boolean value depending on whether its an anagram or not.
# Examples:
# input 1	input 2	output
# "dog"	"god"	true
# "green"	"fox"	false

def is_anagram(string1,string2):
    if len(string1) == len(string2):
        list_of_char1 = []
        list_of_char2 = []
        for i in string1:
            list_of_char1.insert(len(list_of_char1), i)
        for j in string2:
            list_of_char2.insert(len(list_of_char2), j)
        if sorted(list_of_char1) == sorted(list_of_char2):
            return True
    return False
