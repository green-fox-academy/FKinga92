# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def stars_in_string(string1):
    if string1 == "":
        return ""
    elif len(string1) == 1:
        return string1
    else:
        return string1[0] + "*" + stars_in_string(string1[1:])
