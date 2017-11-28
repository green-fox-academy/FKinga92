# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`

aj = [3, 4, 5, 6, 7]
for i in range(len(aj)//2 +1):
    if i != len(aj)//2:
        aj[i] += aj[len(aj)-i -1]
        aj[len(aj)-i -1] = aj[i] - aj[len(aj)-i -1]
        aj[i] -= aj[len(aj)-i -1]
print(aj)

