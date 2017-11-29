students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies

def candies(*args):
    list1 = [*args]
    sum_of_candies = 0
    for i in list1:
        student = str(i)
        student_index = next(index for (index, d) in enumerate(students) if d["name"] == student)
        sum_of_candies += students[student_index]['candies']
    print("The students have " + str(sum_of_candies) + " candies.")


def sum_of_ages(*args):
    list1 = [*args]
    sum = 0
    for i in list1:
        student = str(i)
        student_index = next(index for (index, d) in enumerate(students) if d["name"] == student)
        if int(students[student_index]['candies']) < 5:
            sum += float(students[student_index]['age'])
    print("The sum of the age of people who have less than 5 candies: " + str(sum))
