class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
p1=person("RP",19)
p1.greet()