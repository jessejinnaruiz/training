# inheritance in python

class Student:
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudentB4Inh:
    def __init__(self, name, school, salary) -> None:
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 36

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)

rolf.marks.append(57)
print(rolf.average())
# print(rolf.weekly_salary())

# anna = Student("Anna", "Oxford")
# print(anna.weekly_salary())