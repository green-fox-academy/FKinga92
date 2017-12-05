# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0


def divider(num):
    try:
        result = 10 / num
        print(result)
    except ZeroDivisionError:
        print("fail")
