"""x=10
y=0
try:
    print(x/y)
except ZeroDivisionError:
    print("can't divide by zero")
    
try:
    num = int(input("Enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("can't divide by zero")
except ValueError:
    print("Please enter a valid number")"""
    #Try-else-except
"""
try:
    result = 10/2
except ZeroDivisionError:
    print("Error!") 
else:
    print("Success:", result)"""

#Finally
try:
    f= open("data.txt")
    data = f.read()
    
except:
    FileNotFound:(
        print("File not found!"))
    
finally:
    print("Closing file")
    