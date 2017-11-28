# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

n = int(input("Please enter a number: "))
for i in range(n):
    if n%2 ==0:
        if i == 0 or i == n-1:
            print("%"*(n-1))
        elif i <= n/2:
            print("%"+(i-1)*" " + "%" + (n-3-i)* " " + "%")
        else:
            print("%" + (n-3)* " " + "%")
    else:
        if i == 0 or i == n-1:
            print("%"*(n-1))
        elif i <= (n/2 + 1):
            print("%"+(i-1)*" " + "%" + (n-3-i)* " " + "%")
        else:
            print("%" + (n-3)* " " + "%")
