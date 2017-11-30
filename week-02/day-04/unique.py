# Create a function that takes a list of numbers as a parameter
# Returns a list of numbers where every number in the list occurs only once
# Example

# input: [1, 11, 34, 11, 52, 61, 1, 34]
# output: [1, 11, 34, 52, 61]

def unique_sort(alist):
    for reverse_index in range(len(alist) - 1, 0, -1):
        for i in range(reverse_index):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
    for reverse_index in range(len(alist) - 1, 0, -1):
        for i in range(reverse_index):
            if i < (len(alist) - 1):
                if alist[i] == alist[i + 1]:
                    alist.remove(alist[i])
    return alist

