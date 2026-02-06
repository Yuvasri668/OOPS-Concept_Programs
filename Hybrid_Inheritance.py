#Hybrid Inheritance

class Person:
    def __init__(self, name):
        self.name = name
    def display_person(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id
    def display_student(self):
        print("Student ID:", self.student_id)

class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        Person.__init__(self, name)
        self.sport_name = sport_name
    def display_sports_player(self):
        print("Sport:", self.sport_name)

class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name
    def display_college_student(self):
        print("College:", self.college_name)


c = CollegeStudent("Yuva", 101, "Cricket", "MRIT")

c.display_person()
c.display_student()
c.display_sports_player()
c.display_college_student()
