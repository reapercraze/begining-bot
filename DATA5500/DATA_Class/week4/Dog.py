class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
class Dog():
    def __init__(self, name, breed, gender, wieght, age, owner_name, owner_age):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.wieght = wieght
        self.age = age
        
        self.owner = Owner(owner_name, owner_age)
        
    def owner_info(self):
        self.info = [self.owner.name, self.owner.age]
        
        for i in self.info:
            print(i)
        return ""
        
        
    def __str__(self):
        return "Dog: " + str(self.name)
    
    def birth_year(self, current_year):
        return current_year - self.age
    
    def get_owner(self):
        return self.owner
    

dog1 = Dog("Abby", "Border Collie and Australian Sheperd mix", "F", 55, 2, "Tyler", 19)
dog2 = Dog("Mona", "American Staffordshire Terrier", "F", 55, 5, "Hailee", 17)
dog3 = Dog("Nina", "Unknown", "F", 65, 6, "Laura", 25)

print(Dog.owner_info(dog3))