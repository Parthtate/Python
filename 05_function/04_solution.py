import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return [math.trunc(area), math.trunc(circumference)]

a, c = circle_stats(2)

print("Area:", a, "Circumference:", c)

# formula:
# area = pi * r2
# circumference = 2 * pi * r

# math.trunc is same as math.floor