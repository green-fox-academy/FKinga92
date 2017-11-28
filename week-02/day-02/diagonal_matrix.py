# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output
li = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(len(li)):
    li[i][i] = 1
    for a in range(len(li[i])):
        if a > 0 and a%(len(li)-1) == 0:
            print(li[i][a], end='\n')
        else:
            print(li[i][a], " ", end='')
