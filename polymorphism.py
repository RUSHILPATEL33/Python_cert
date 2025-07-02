"""class Bird:
    def sound(self):
        print("chirp")
class Cat:
    def sound(self):
        print("Meow")
def make_sound(ANIMAL):
    ANIMAL.sound()
b=Bird()
c=Cat()
make_sound(b)
make_sound(c)"""
"""
class parent:
    def show(self):
        print("Parent's Method")
        
class child:
    def show(self):
        print("Child's Method")
        
obj = child()
obj.show()"""

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Point(self.x +other.x, self.y + other.y)
p1=Point(1, 2)
p2=Point(3, 4)
p3 = p1+p2
print(p3.x, p3.y)
        
        