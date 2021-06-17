# the property decorator
# at property decorator turns a method into a property

class Student:
    #create a class
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary_b4_dec(self):
        #create a method (ie a function inside a class). no arguments besides self.
        # functions perform an action. but this does not really perform an action.
        #change weekly salary to a property of the object ... eg from rolf.weekly_salary() to rolf.weekly_salary
        return self.salary * 36

    @property
    def weekly_salary(self):
        # this is just calculating a value from the objects properties.
        return self.salary * 36

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)

rolf.marks.append(80)
rolf.marks.append(90)
rolf.marks.append(78)
print(rolf.average())
print(rolf.weekly_salary())
