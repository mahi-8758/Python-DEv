"""Implement a program that classifies a given angle (input in degrees)
into categories such as acute, right, obtuse, or invalid."""
angle = int(input("Enter angle in degrees: "))
if 0 < angle < 90:
    print("Acute angle")
elif angle > 0 and angle ==90:
    print("Right angle")
elif 180 > angle > 90:
    print("Obtuse angle")
else:
    print("Invalid angle")
