# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

file_name = "my-file.txt"
try:
    f = open(file_name, "r")
    for line in f:
        print(line.rstrip())
    f.close()
except IOError:
    print("Unable to read file: ", file_name)
