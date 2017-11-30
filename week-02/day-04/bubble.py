# Sort that list
# Create a function that takes a list of numbers as parameter
# Returns a list where the elements are sorted in ascending numerical order
# Make a second boolean parameter, if it's true sort that list descending
# Example

# input [34, 12, 24, 9, 5]
# output [5, 9, 12, 24, 34]

def sort_list(alist, b):
    if b is False:
        for reverse_index in range(len(alist) - 1, 0, -1):
            for i in range(reverse_index):
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
    else:
        for reverse_index in range(len(alist) - 1, 0, -1):
            for i in range(reverse_index):
                if alist[i] < alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
    return alist
