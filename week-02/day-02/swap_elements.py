# - Create a variable named `abc`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `abc`

abc = ["first", "second", "third"]
# abc[0], abc[2] = abc[2], abc[0]

abc[0] = abc[0] + abc[2]
abc[2] = abc[0][0:int(len(abc[0]) - len(abc[2]))]
abc[0] = abc[0][int(len(abc[2])): ]
