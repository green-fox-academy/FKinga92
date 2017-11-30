# Find part of an integer
# Create a function that takes two strings as a parameter
# Returns the starting index where the second one is starting in the first one
# Returns -1 if the second string is not in the first one
# Example

# input: "this is what I'm searching in", "searching"
# output: 17

def find_substring(string1, string2):
    index = 0
    if string2 in string1:
        a = string2[0]
        for letter in string1:
            if letter == a:
                if string1[index:index+len(string2)] == string2:
                    return index
            index += 1 
    return -1

