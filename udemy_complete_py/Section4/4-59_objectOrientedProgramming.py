# more about classes and objects

my_student = {
    'name': "Rolf Smith",
    'grades': [70, 88, 90, 99],
    'average': None #todo create
}

def avg_grade(student):
    return sum(student['grades']) / len(student['grades'])

class Student:
    # a class stores some data and some actions that relate to it.
    # allows us to encapsulate and hold all relevant functionality in the same structure.
    def __init__(self, new_name, new_grades) -> None:
        self.name = new_name
        self.grade = new_grades
        
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70,88,90,99])
print(student_one.name)

student_two = Student('Jose', [50,60,99,100])
print(student_two.name)