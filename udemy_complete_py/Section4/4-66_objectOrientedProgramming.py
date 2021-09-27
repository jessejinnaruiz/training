# the @classmethod and @staticmethod

# an instance method is one that takes the caller object as the first argument (ie self).
# two other types of methods:
# 2. takes a class as the first argument.
# 3. takes nothing as the first argument.
# this syntax is used so that you can modify what the method takes in.

class Foo:
    @classmethod
    def hi(cls):
        # the first arg is define as cls or class
        print(cls.__name__)

my_object = Foo()
my_object.hi()
# prints out Foo. because cls.__name__ gives the name of the class.


class Bar:
    @staticmethod
    def hi():
        print("Hello I dont take any parameters.")

another_object = Bar()
another_object.hi()

# class Student:
#     #create a class
#     def __init__(self, name, school) -> None:
#         self.name = name
#         self.school = school
#         self.marks = []

#     def average(self):
#         return sum(self.marks) / len(self.marks)


# rolf = Student('Rolf', 'MIT')

# rolf.marks.append(78)
# rolf.marks.append(99)

# print(rolf.average())