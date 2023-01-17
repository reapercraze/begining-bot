import numpy as np
#10.1 and 10.2
class Person():
    def __init__(self, height):
        self.height = height
        
    def avg(self):
        return np.mean(self.height)
    
    def set_height(self, height):
        self.height = height

p1 = Person([60,65,68,73])
print(p1.height)
print(p1.avg())
p1.set_height([65,68,73,74])
print(p1.height)
print(p1.avg())

#10.5
class Student():
    def __init__(self, name, a_number):
        self.name = name
        self.__a_number = a_number
        
    def get_a_number(self):
        return self.__a_number
    
    def set_a_number(self, a_number):
        self.__a_number = a_number
        
    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name
        
s1 = Student("Tyler Gale", "A02334309")
print(s1.name)
print(s1.get_a_number())
