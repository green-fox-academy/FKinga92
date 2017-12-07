# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def x_replace(string1):
    if string1 == "":
        return string1
    elif string1[0] == "x":
        return "y" + x_replace(string1[1:])
    else:
        return string1[0] + x_replace(string1[1:])
