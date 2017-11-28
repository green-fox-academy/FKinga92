# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was

n = int(input("Please enter a number: "))
for i in range(n):
    if i==0 or i==(n-1):
        print("%"*(n-1))
    else:
        print("%" + " "* (n-3) + "%")