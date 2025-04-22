import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

print("Choose a shape: 1.Circle 2.Rectangle 3.Triangle")
choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle:", area_circle(r))
elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle:", area_rectangle(l, w))
elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of Triangle:", area_triangle(b, h))
else:
    print("Invalid choice")
