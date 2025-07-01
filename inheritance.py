"""class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

d=Dog()
d.speak
d.bark"""

class Class1:
    def m(self):
        print("in class 1")
class Class2(Class1):
    def m(self):
        print("in class 2")
class Class3(Class1):
    def m(self):
        print("in class 3")
class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()
        