import math
# Imports the math library for the power and square root predefined functions.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
# User input for the coordinates of the two points.
d = math.sqrt(math.pow((x2 - x1), 2) + (math.pow((y2 - y1), 2)))
# The formula to calculate the distance between the two points.
print ("The distance between the two points is:", (round(100*d))/100)
# Outputs the final value of the distance, rounded to the nearest hundreths.
