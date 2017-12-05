# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    try:
        new_lines = ""
        with open(file_name, "r") as f:
            for line in f:
                for i in range(0, len(line), 2):
                    letter = line[i]
                    new_lines += letter       
        with open(file_name, "w") as f2:
            f2.write(new_lines)
    except:
        print("Cannot find file")
    
decrypt("duplicated-chars.txt")