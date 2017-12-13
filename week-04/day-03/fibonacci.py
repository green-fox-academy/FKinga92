# Write a function that computes a member of the fibonacci sequence by a given index
# Create tests that covers all types of input (like in the previous workshop exercise)

def fibonacci(n):
    try:
        if n < 0:
            return "Index cannot be a negative number."
        elif  n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except TypeError:
        return "You can only enter a number."
