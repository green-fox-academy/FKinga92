# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

def printer(*args):
    list1 = [*args]
    for i in list1:
        print(i)
