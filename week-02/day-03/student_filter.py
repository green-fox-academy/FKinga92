students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def many_candies(*args):
    list1 = [*args]
    for i in list1:
        student = str(i)
        student_index = next(index for (index, d) in enumerate(students) if d["name"] == student)
        list2 = []
        if int(students[student_index]['candies']) > 4:
            list2.insert(len(list2), student)
    print(list2, "has/have got more than 4 candies.")


def average_candies(*args):
    list1 = [*args]
    sum= 0
    for i in list1:
        student = str(i)
        student_index = next(index for (index, d) in enumerate(students) if d["name"] == student)
        sum += int(students[student_index]['candies'])
    print("They have " + str(sum/len(list1)) + " candies on average.")

