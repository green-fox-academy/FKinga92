# Create a method that decrypts reversed-order.txt


def decrypt(file_name):
    new_lines = ""
    with open(file_name, "r") as f:
        for line in f:
            new_lines = line + new_lines
    with open(file_name, "w") as f2:
        f2.write(new_lines)

decrypt("reversed-order.txt")

