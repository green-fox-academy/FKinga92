# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def number_adder(n):
    if n < 2:
        return 1
    else:
        return n + (number_adder(n - 1))

