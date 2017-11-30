# Find the substring in the list
# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list
# Example

# input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
# output: 4

def substring_index(string1, alist):
    string_list = ""
    for i in alist:
        string_list += i
    if string1 in string_list:
        for word in alist:
            if string1 in word:
                string_index = next(index for index, w in enumerate(alist) if
                                    w == word)
                return string_index 
    return -1

