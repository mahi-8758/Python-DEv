import math
print("DISTANCE BETWEEN TWO POINTS")
x1, y1 = float(input("Enter x1: ")), float(input("Enter y1: "))
x2, y2 = float(input("Enter x2: ")), float(input("Enter y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Distance: {distance:.2f}")
