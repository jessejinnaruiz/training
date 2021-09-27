# more examples on @classmethod and @staticmethod

#most of community is against the static method. most prefer the classmethod.
#use classmethod whenever you want to create a method that doesnt use self
#cls allows all the methods from the parent class to be used in the child class.

class FixedFloat:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __repr__(self) -> str:
        return f'<FixedFloat {self.amount:.2f}>'

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)

    def from_sum_b4_change(self, value1, value2):
        #this class doesnt use self so its not really that useful
        return FixedFloat(value1 + value2)

    @classmethod #make sure to add this @classmethod
    def from_sum_cls(cls, value1, value2):
        # change the method to cls instead of FixedFloat
        return cls(value1 + value2)

number = FixedFloat(18.5746)
new_number = number.from_sum(19.575, 0.789)
print(number)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount) -> None:
        super().__init__(amount)
        self.symbol = 'e'
    
    def __repr__(self) -> str:
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro(18.587)
print(money)

money_add = Euro.from_sum(16.758, 9.999)
#the from_sum method is inherited from FixedFloat class.
print(money_add)
#but the class type that is returned for this money_add object is read as "FixedFloat"
#and we dont want this... so we can change the staticmethod to a classmethod to create the correct reference to the class

money_add_with_classmethod = Euro.from_sum_cls(16.758, 9.999)

print(money_add_with_classmethod)