"""li = ['RP', 'Ahemdabad', 19, 30.06, True]
print(li)
print(li[2])
li[1]="Gujarat"
print(li)"""

"""fruits = ["Apple", "Mango","Grapes", "Peach", "Mango"]
print(fruits)
fruits.append("Kiwi")
print(fruits)
fruits.insert(1,"Banana")
print(fruits)
fruits.extend(["Pineaple","litchi"])
print(fruits)"""
"""fruits.remove("Mango")
print(fruits)
fruits.pop(3)
print(fruits)
fruits.clear()
print(fruits)"""
"""len(fruits)
print(fruits[1:4])
print(fruits.index("Grapes"))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)"""
"""
#Tuples
Veggies = ("Tomato", "Onion", "Celery")
print(Veggies)
print(len(Veggies))

Pulses = ("moong", "rajma", "chana")
print(Pulses)
print(len(Pulses))
print(Veggies + Pulses)

person = ("RP", 19, "Engineer")
Name, Age, Profession = person
print(Name)
print(Age)
print(Profession)
print(person.count(19))
print(person.index("Engineer"))"""
"""
#Sets
numbers = {1,2,3,4,5,6,7,8,9}
print(numbers)
numbers.add(10)
print(numbers)
numbers.remove(10)
print(numbers)
print(len(numbers))
print(4 in numbers)
alphabets ={'a','b','c','d','e','f','g','h'}
print(alphabets)
print(numbers.union(alphabets))
"""
"""
#Dictionary
dict = {"Name":"RP", "Age": 19, "Professsion": "Engineer"}
print(dict)"""
"""
person = dict('name'="RP", 'age'=19, 'profession'="Engineer")
print(person)"""

student = {
    "name": "RP",
    "age":20,
    "course": "Python"
}
print(student["name"])
print(student.get("age"))
student["age"]=21
student["city"]="NewYork"
print(student)
student.pop("course")
print(student)
#student.clear()
#print(student)

students={
    "101":{"name":"Rushil", "grade": "A"},
     "102":{"name":"jenil", "grade": "A"}
}
print(students)
print(students["101"]["name"])