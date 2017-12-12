class Person(object):
    def __init__(self, name="Jane Doe", age=30, gender="female"):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return "Hi, I'm {}, a {} year old {}".format(self.name, str(self.age), self.gender)
    def introduce(self):
        print(self.__str__() + ".")
    def get_goal(self):
        print("My goal is: Live for the moment!")
    
class Student(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female",
                previous_organization="The School of Life"):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = 0
    def introduce(self):
        print(super().__str__() +
              " from {} who skipped {} days from the course already."
              .format(self.previous_organization, str(self.skipped_days)))
    def get_goal(self):
        print("My goal is: Be a junior software developer.")
    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

class Mentor(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", level="intermediate"):
        super().__init__(name, age, gender)
        self.level = level
    def introduce(self):
        print(super().__str__() + " {} mentor.".format(self.level))
    def get_goal(self):
        print("My goal is: Educate brilliant junior software developers.")

class Sponsor(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", company="Google"):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = 0
    def introduce(self):
        print(super().__str__() + " who represents {} and hired {} students so far."
              .format(self.company, str(self.hired_students)))
    def get_goal(self):
        print("My goal is: Hire brilliant junior software developers.")
    def hire(self):
        self.hired_students += 1

class PallidaClass():
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.mentors = []
    def add_student(self, Student):
        self.students.append(Student)
    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)
    def info(self):
        print("Pallida {} has {} students and {} mentors."
              .format(self.class_name, str(len(self.students)), str(len(self.mentors))))

people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
people.append(sponsor)
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()

badass = PallidaClass('BADA55')
badass.add_student(student)
badass.add_student(john)
badass.add_mentor(mentor)
badass.add_mentor(gandhi)
badass.info()