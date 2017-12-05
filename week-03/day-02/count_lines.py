# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def number_of_lines(file_name):
    num_of_lines = 0
    try:
        f = open(file_name, "r")
        for line in f:
            num_of_lines += 1
        f.close()
        return num_of_lines
    except IOError:
        return 0

