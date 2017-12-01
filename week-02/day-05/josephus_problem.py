# Exercise
# Write a function to solve Josephus Problem. The program should ask for a number,
# this number represents how many people are in the "game". The return value should be the number of the "winning" seat.
# Examples
# number of people	number of the winning seat
# 1	                            1
# 2	                            1
# 3	                            3
# 7	                            7
# 12	                        9
# 41	                        19

# f(n) = 1 + 2 * (num - 2^([log2(n)]))

import math

def josephus(num):
    if num != 1:
        k = math.floor(math.log2(num))
        survivor = 2 * (num - math.pow(2, k)) + 1
        return int(survivor)
    return 1

