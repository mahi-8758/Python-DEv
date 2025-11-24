import math

def ball_collide(ball1, ball2):
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance <= (r1 + r2)

print("BALL COLLISION DETECTION")


balls = []
for i in range(1, 4):
    print(f"\nEnter Ball {i} coordinates (x, y, radius):")
    x = float(input(f"Enter x{i}: "))
    y = float(input(f"Enter y{i}: "))
    r = float(input(f"Enter radius{i}: "))
    balls.append((x, y, r))

for i, ball in enumerate(balls, 1):
    print(f"Ball {i}: {ball}")


print()
for i in range(len(balls)):
    for j in range(i + 1, len(balls)):
        result = ball_collide(balls[i], balls[j])
        print(f"Ball {i + 1} and Ball {j + 1} collide: {result}")

