# Create a method that find the 5 most common lottery numbers otos.csv
# def fix_csv():
#     corrected_lines = ""
#     with open("otos.csv", "r") as f:
#         for line in f:
#             corrected_lines += line.replace(";", ",")
#     with open("otos.csv", "w") as f2:
#         f2.write(corrected_lines)

# fix_csv("otos.csv")

def five_most_frequent():
    dict1 = {}
    with open("otos.csv", "r") as f:
        for line in f:
            x = (line.replace("\n", "")).split(",")
            lottery_numbers = x[-5: ]
            for num in lottery_numbers:
                if num in dict1.keys():
                    dict1[num] += 1
                else:
                    dict1[num] = 1
    print(sorted(dict1, key=dict1.get)[-5: ])


five_most_frequent()