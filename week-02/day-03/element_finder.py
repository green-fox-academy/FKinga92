# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8]
contains = ""
for i in numbers:
    number = int(i)
    if  number == 7:
        contains = "Hoorray"
        break
    else:
        contains = "Noooooo"
print(contains)
