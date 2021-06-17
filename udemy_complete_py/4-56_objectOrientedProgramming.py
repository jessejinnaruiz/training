# intro to object-oriented programming with python

my_student = {
    'name': "Rolf Smith",
    'grades': [70, 88, 90, 99],
    'average': None #todo create
}

def avg_grade(student):
    return sum(student['grades']) / len(student['grades'])

class Student:
    def __init__(self, new_name, new_grades) -> None:
        self.name = new_name
        self.grade = new_grades
        
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70,88,90,99])
print(student_one.name)