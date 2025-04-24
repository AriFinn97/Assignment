import sys
import math


if len(sys.argv) < 2:
    print("Usage: python test.py <radius>")
    sys.exit(1)

# Convert the first command-line argument to a float.
try:
    height = float(sys.argv[1])
    width = float(sys.argv[2])
except ValueError:
    print("Invalid input. Please provide a numerical value for the height.")
    sys.exit(1)


height = float(input( "please enter the height of your rectangle:"))
width = float(input( "please enter the width of your rectangle:"))
area = height * width
perimeter = 2 * ( height + width )
print (f" your rectangle has a area of {area:.2f} and a perimeter of {perimeter:.2f}")
