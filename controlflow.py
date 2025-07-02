"""age=int(input("Enter your Age:"))
print(age)
if age>=18 and age<65:
    print("You're an Adult")
elif age>=65:
        print("You're an senior citizen")
else:
    print("you're a child")"""

#For Loop
"""
for i in range(1,9):
    print(i)
for letter in "HELLO":
    print(letter)
    """

#While loop
"""
count=1
while count<=10:
    print(count)
    count = count+1

age = int(input("Enter your Age:"))

if age>=18 and age<40:
    print("You are eligible for voting")
elif age>=40 and age<75:
    print("You are a actual voter")
elif age>=75:
    print("you are a retired voter")
else:
    print("you are not eligible for voitng") """

#break
"""
for i in range(1,10):
    if i==5:
        break
    print(i)"""

#Continue
"""
for i in range(1,5):
    if i == 3:
        continue
    print(i)"""
for i in range(1,30):
    if i % 3==0:
        continue
    print(i)
        