# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_remove(string1):
    if string1 == "":
        return string1
    elif string1[0] == "x":
        return "" + x_remove(string1[1:])
    else:
        return string1[0] + x_remove(string1[1:])
