# Create a method that decrypts encoded-lines.txt
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
       "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
       "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
       "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", ",", "-", ".",
       "/", "'", "(", "*", "+", "!", '"' ]
def decrypt(file_name):
    new_lines = ""
    with open(file_name, "r") as f:
        for line in f:
            for i in line:
                if i in abc:
                    letter_index = next(index for (index, letter) in enumerate(abc) if i == letter)
                    new_lines += abc[(letter_index - 1)]
                else:
                    new_lines += i
    with open(file_name, "w") as f2:
        f2.write(new_lines)

decrypt("encoded-lines.txt")
