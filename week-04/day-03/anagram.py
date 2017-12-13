# Write a function, that takes two strings and returns a boolean value based on 
# if the two strings are Anagramms or not.
# Create a test for that.

def is_anagram(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    if sorted(string1.lower()) == sorted(string2.lower()):
        return True
    return False
