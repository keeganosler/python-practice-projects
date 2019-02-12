#!/bin/python3

# area calculator computes and prints the area of shapes

option = input("Enter C for circle or T for triangle: ")

if option == "C":
    shape = "circle"
    radius = float(input("Please enter the radius of your circle: "))
    area = 3.14159*(radius**2)
elif option == "T":
    shape = "triangle"
    base = float(input("Please enter the base of your triangle: "))
    height = float(input("Please enter the height of your triangle: "))
    area = 0.5*base*height
else:
    print("Invalid shape selected!")

print("Your shape is a " + shape + " and it's area is %s" %(area))