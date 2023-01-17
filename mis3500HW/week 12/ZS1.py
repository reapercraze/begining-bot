#programming activity 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calcAread(self):
        return self.width * self.height
    
rect1 = Rectangle(4, 5)
print(rect1.calcAread())

#programming activity 2
class Cube:
    def __init__(self, length):
        self.length = length
        
    def calcVolum(self):
        return self.length ** 3
        
    def calcSurfaceArea(self):
        return self.length ** 2 * 6
        
cube1 = Cube(6)
print(cube1.calcVolum())
print(cube1.calcSurfaceArea())