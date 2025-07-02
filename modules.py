import math
radius = float(input("Enter radius:"))
if radius<0:
    print("invalid")
else:
    area= (math.pi)*radius*radius
    print("Area of Circle:",area)
