#Inherited Class
from DebugBase import DebugBase

class DebugInherit(DebugBase):
    def __init__(self, _name_, the_age):
        self.name = _name_
        self.age = the_age
    def bark(self):
        print("bark")
    def get_age(self):
        print(self.age)
    def meow(self):
        print("Meow meow")

