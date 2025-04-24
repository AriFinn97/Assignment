import sys
import math


if len(sys.argv) < 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

# Convert the first command-line argument to a float.
try:
    radius = float(sys.argv[1])
except ValueError:
    print("Invalid input. Please provide a numerical value for the radius.")
    sys.exit(1)

circumference = 2 * math.pi * radius    
area = math.pi * (radius ** 2)
print(f"Your circle's circumference is {circumference:.2f} and area is {area:.2f}")
