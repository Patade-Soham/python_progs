import math

print("Choose shape: 1. Circle 2. Rectangle 3. Triangle")
choice = input("Enter choice: ")

if choice == '1':
    r = float(input("Enter radius: "))
    area = math.pi * r ** 2
elif choice == '2':
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
elif choice == '3':
    base = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * base * h
else:
    area = None
    print("Invalid choice.")

if area is not None:
    print("Area:", area)
