# Create a method that decrypts reversed-lines.txt

def decrypt(file_name):
    try:
        new_lines = ""
        with open(file_name, "r") as f:
            for line in f:
                for i in range(len(line)):
                    if line[i] == "\n":
                        line = line.replace("\n", "")
                new_lines += (line[: :-1] + "\n")
        with open(file_name, "w") as f2:
            f2.write(new_lines)
    except:
        print("Cannot find or write:", file_name)
    
                
decrypt("reversed-lines.txt")