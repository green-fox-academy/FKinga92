# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#

n = 1
while n < 9:
    if n % 2 ==0:
        print(" % % % %")
        n += 1
    else:
        print("% % % % ")
        n += 1